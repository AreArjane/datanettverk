#TASK 1 & TASK 2
import sys
import ast
import math


def jains_fairness_index(throughputs):
    '''
        Description
           Define the function to calculate Jain's Fairness Index (JFI) 
    '''
    N = len(throughputs) 
    sum_of_throughputs = sum(throughputs)
    sum_of_squares = sum(x**2 for x in throughputs)
    if sum_of_squares == 0: 
        return 0
    JFI = (math.pow(sum_of_throughputs,2)) / (N * sum_of_squares)
    return JFI

def kb_convertor(value, unit):
    ''' Description
            function to convert all unite in thoughtput_values.txt into kbps
            Param
            Value, unit 
    '''
    if unit == "Kbps":
        return value
    elif unit == "Mbps":
        return value * 1000
    else:
        return 0
    
def read_fil(fil):
    '''
        Description
        This function read from the file excat defined with one value and one unit
        then it return a list of this value in float and kbps

    '''
    value_kb = []
    with open(fil, 'r') as file:
        for line in file:
            parts = line.split() 
            if len(parts) == 2: 
                value, unit = parts
                try:
                    value = float(value)
                    value_in_kb = kb_convertor(value, unit)
                    value_kb.append(value_in_kb)
                except ValueError as e:
                    print(f"error{e}")
            else:
                print(f"Error line format{line.strip()}")
    return value_kb



#Main program 
if __name__ == "__main__":
    #check of command line less than 2 args output msg and exit the proccess
    if len(sys.argv) < 2:
        print("Use the command python3 [jain.py -input] {list/path}")
        sys.exit(1)

    input_args = sys.argv[1]
    #for the index command TASK 1
    if input_args.startswith('['):
        try:
            
            throughputs_index = ast.literal_eval(sys.argv[1])
            jfi = jains_fairness_index(throughputs_index)
            print(jfi)

        except (ValueError, SyntaxError) as e:
            print(f"Error occure during proccessing the list: {e}")
    #for reading from file TASK 2
    else:
        try:
            throughputs = read_fil(input_args)
            if not throughputs:
                raise ValueError("No File assosicated with this name")
            jfi_2 = jains_fairness_index(throughputs)
            print(jfi_2)
        except (ValueError, SyntaxError) as e:
            print(f"Error handling file: {e}")
            sys.exit(1)