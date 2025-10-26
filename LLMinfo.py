import sys
import os
def option_a(filename):
    with open(filename, 'r') as file:
        print("Models:")
        for line in file:
            line = line.strip()          
            if not line:                 
                continue
            parts = line.split(',')      
            print(parts[0])             

def main():
    input_list = sys.argv[1:]
    #test input
    #print(input_list)
    #print(len(input_list))
    if len(input_list) < 2:
        print("it misses the argument file")
        sys.exit(1)
    else:
        filename  = input_list[-1].lower()
        options = input_list[0].lower()
        #test fileneme and options correct
        #print(options, filename)
    if options == "-s" and len(input_list) != 3:
        print("it misses the size argument")
        sys.exit(1)
    elif options == "-c" and len(input_list) != 3:
        print("it misses the company argument")
        sys.exit(1)
    elif options not in["-a", "-r", "-c", "-s", "-v"]:
        print("this option doesn't exist")
        sys.exit(1)
    
    option_a(filename)  


if __name__ == "__main__":
    main()
