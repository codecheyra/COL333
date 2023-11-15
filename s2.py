from sys import argv
def cnf_formulation(n, k1, k2, adj_matrix):
    x = []  # List of xi variables
    s = []  # List of si,j variables
    s1 = [] 
    count=0
    for i in range(1, n+ 1):
        count += 1
        x.append(count)
    
    clauses = []
    if k1<n:
        for i in range(n-1):
            s.append([0] * k1)
            s1.append([0] * (n-k1))
            # s1.append([0] * k1)
        for i in range(0, n-1):
            for j in range(0, k1):
                count+=1
                s[i][j] =count

        for i in range(0, n-1):
            for j in range(0, n-k1):
                count+=1
                s1[i][j] = count
        clauses.append(f'-{x[0]} {s[0][0]}' + ' 0' )
        print ()

        for j in range(2, k1 + 1):
            clauses.append(f'-{s[0][j-1]}' + ' 0')  
        for i in range(2, n):
            clauses.append(f'-{x[i - 1]} {s[i - 1][0]}' + ' 0')
        for i in range(2, n):
            clauses.append(f'-{s[i - 2][0]} {s[i - 1][0]}' +' 0')

        for i in range(2, n):
            for j in range(2, k1 + 1):
                clauses.append(f'-{x[i - 1]} -{s[i - 2][j-2]} {s[i-1][j-1]}' + ' 0')

        for i in range(2, n):
            for j in range(2, k1 + 1):
                clauses.append( f'-{s[i - 2][j-1]} {s[i-1][j-1]}' + ' 0')
        for i in range(2, n):
            clauses.append(f'-{x[i - 1]} -{s[i-2][k1-1]}' + ' 0')
        clauses.append(f'-{x[n-1]} -{s[n - 2][k1-1]}' + ' 0')

        # atmost one for xi
        clauses.append(f'{x[0]} {s1[0][0]}' + ' 0')
        for j in range(2, n-k1 + 1):
            clauses.append(f'-{s1[0][j-1]}' + ' 0')
        for i in range(2, n):
            clauses.append(f'{x[i - 1]} {s1[i - 1][0]}' + ' 0')
        for i in range(2, n):
            clauses.append(f'-{s1[i - 2][0]} {s1[i - 1][0]}' + ' 0')
        for i in range(2, n):
            for j in range(2, n-k1 + 1):
                clauses.append(f'{x[i - 1]} -{s1[i - 2][j-2]} {s1[i-1][j-1]}' + ' 0')

        for i in range(2, n):
            for j in range(2, n-k1+1):
                clauses.append( f'-{s1[i - 2][j-1]} {s1[i-1][j-1]}' + ' 0')
        for i in range(2, n):
            clauses.append(f'{x[i - 1]} -{s1[i-2][n-k1-1]}' + ' 0')

        clauses.append(f'{x[-1]} -{s1[n - 2][n-k1-1]}' + ' 0')
    else:
        for i in range(n):
            clauses.append(f'{x[i]}' + ' 0')

    matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i+1,n):
            count+=1
            matrix[i][j] = count
            # num += 1
            if adj_matrix[i][j] == 0:
                clauses.append(f'-{matrix[i][j]}' + ' 0')
            else:
                clauses.append(f'{matrix[i][j]}' + ' 0')  

    #complete constraints
    for i in range(n):
        for j in range(i+1,n):
            clauses.append(f'-{x[i]} -{x[j]} {matrix[i][j]}' + ' 0')
    
    # no common node
    # for i in range(n):
    #     clauses.append(f"-{x[i]} -{y[i]}" + ' 0')
    b=[]
    b.append(clauses)
    b.append(count)
    return b


def main():
    inp = argv[1]
    #print(argv[2])
    k1 = int(argv[2])
    k2 = int(argv[3])
    try:
        with open(inp+'.graph', 'r') as file:
            firstline = list(map(int, file.readline().split()))
            vertices = firstline[0]
            edges = firstline[1]
        
            adj_matrix = [[0 for i in range(vertices)] for j in range(vertices)]
            for line in file:
                # edge = file.readline()
                node1, node2 = map(int, line.split())

                if 1 <= node1 and node1 <= vertices and 1 <= node2 and node2 <= vertices:
                    adj_matrix[node1 - 1][node2 - 1] = 1
                    adj_matrix[node2 - 1][node1 - 1] = 1
                else:
                    print(f"Invalid edge: ({node1}, {node2})")

    except FileNotFoundError:
        print("Input file not found.")


    n=vertices
    a= cnf_formulation(n, k1, k2, adj_matrix)
    cnf_formula=a[0]
    count=a[1]
    try:
        with open(inp+".satinput", 'w') as output:
            output.write(f"p cnf {count} {len(cnf_formula)}\n")
            for i in cnf_formula:
                output.write(f"{i}\n")

        # print("File written successfully.")
    except IOError:
        print("Error in opening the file.")



if __name__ == "__main__":
    main()

