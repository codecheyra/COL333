
from sys import argv
inp = argv[1]
def main():
    try:
        with open(inp+'.graph', 'r') as file:
            l = file.readline()
            vertices ,k1,k2= int(l.split(" ")[0]),int(l.split(" ")[2]),int(l.split(" ")[3])
    except FileNotFoundError:
        print("Input file not found.")

    try:
        with open(inp+'.satoutput', 'r') as file:
            line = file.readlines()
            if(line[0] == 'UNSAT\n'):
                with open(inp+'.mapping', 'w') as file2:
                    file2.write('0')
            else:
                lines = line[1].split(" ")
                with open(inp+'.mapping', 'w') as file2:
                    file2.write('#1\n')
                temp1=k1;temp2=k2
                for i in range(vertices):
                    if(int(lines[i]) > 0):
                        k1-=1
                        with open(inp+'.mapping', 'a') as file2:
                            file2.write(lines[i] + " ") if k1>0 else file2.write(lines[i])
                # print("i", i)

                with open(inp+'.mapping', 'a') as file2:
                    file2.write('\n#2\n')
                for i in range( vertices, 2*vertices):
                    if (int(lines[i]) > 0):
                        k2-=1
                        with open(inp+'.mapping', 'a') as file2:
                            file2.write(str(int(lines[i])-vertices) +" ") if k2>0 else file2.write(str(int(lines[i])-vertices))

    except FileNotFoundError:
        print("Input file not found.")

if __name__ == "__main__":
    main()