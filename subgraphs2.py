from sys import argv
inp = argv[1]
def main():
    try:
        with open(inp+'.graph', 'r') as file:
            l = file.readline()
            vertices = int(l.split(" ")[0])
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
                k=0
                for i in range(0, vertices):
                    if(int(lines[i]) > 0):
                        k+=1

                for i in range( 0, vertices):
                    if (int(lines[i]) > 0):
                        # print(lines[i])
                        k-=1
                        with open(inp+'.mapping', 'a') as file2:
                            file2.write(str(int(lines[i])) +" ") if k>0 else file2.write(str(int(lines[i])))

    except FileNotFoundError:
        print("Input file not found.")

if __name__ == "__main__":
    main()