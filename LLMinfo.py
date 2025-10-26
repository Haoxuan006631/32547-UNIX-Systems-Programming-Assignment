'''
Assignment - UNIX Systems Programming
Name: Haoxuan Jin
Student ID: 25167901
Github link: https://github.com/Haoxuan006631/32547-UNIX-Systems-Programming-Assignment.git
'''
import sys
import os

def option_a(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        if not lines:
            print("No models in this file")
            return
    with open(filename, 'r') as file:
        print("Models:")
        for line in file:
            line = line.strip()          
            parts = line.split(',')   
            #print(parts)   
            print(parts[0])             

def optopm_r(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        if not lines:
            print("No remote models in this file")
            return
    with open(filename, 'r') as file:
        count = 0
        for line in file:
            line = line.strip()          
            parts = line.split(',')
            #print(parts)   
            if parts[-1].lower() == "remote":
                if count == 0:
                    print("Remote models:")
                print(parts[0])
                count += 1
            else:
                continue
    if count == 0:
        print("No remote models in this file")

def option_c(filename, company):
    with open(filename, 'r') as file:
        lines = file.readlines()
        if not lines:
            print(f"No models from {company} in this file")
            return
    with open(filename, 'r') as file:
        count = 0
        for line in file:
            line = line.strip()          
            parts = line.split(',')
            #print(parts)   
            if parts[1].lower() == company.lower():
                if count == 0:
                    print(f"Models from {company}:")
                print(parts[0])
                count += 1
            else:
                continue
    if count == 0:
        print(f"No models from {company} in this file")
def option_s(filename, size):
    with open(filename, 'r') as file:
        lines = file.readlines()
        if not lines:
            print("No models with up to {s}B parameters in this file".format(s=size))
            return
    count = 0
    with open(filename, 'r') as file:
        try:
            size_limit = float(size)
        except ValueError:
            print(f"No models with up to {size}B parameters in this file")
            sys.exit(1)
        for line in file:
            line = line.strip()          
            parts = line.split(',')
            #print(parts)   
            if len(parts) < 3:
                continue
            line_3 = parts[2].lower()
            # print(line_3)
            try:
                model_size = float(line_3)
            except ValueError:
                continue

            if model_size <= size_limit:
                if count == 0:
                    print(f"Models with up to {size}B parameters:")
                print(parts[0])
                count += 1
        if count == 0:
            print(f"No models with up to {size}B parameters in this file")
def option_v(filename):
    print("Name:Haoxuan Jin\nStudent ID: 25167901\nCourse: 32547-UNIX Systems Programming\nfinished date: 2025-10-26\ngithub link:https://github.com/Haoxuan006631/32547-UNIX-Systems-Programming-Assignment.git")

def main():

    input_list = sys.argv[1:]
    #test input
    #print(input_list)
    #print(len(input_list))
    if len(input_list) < 2:
        print("it misses the argument file")
        sys.exit(1)
    else:
        filename  = input_list[-1]
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
    if not os.path.isfile(filename) or not os.access(filename, os.R_OK):
        print("Error: file not found")
        sys.exit(1)
    '''
    test 
    option_a(filename)  
    optopm_r(filename) 
    '''
    if options == "-a":
        option_a(filename)  
    elif options == "-r":
        optopm_r(filename) 
    elif options == "-c":
        company = input_list[-2]
        #print(company)
        option_c(filename, company)
    elif options == "-s":
        size = input_list[-2]
        #print(size)
        option_s(filename, size)
    elif options == "-v":
        option_v(filename)

if __name__ == "__main__":
    main()
