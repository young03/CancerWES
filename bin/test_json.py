import sys
import json

def check_json(input_str):
    with open(input_str) as load_f:
        try:
            load_dict = json.load(load_f)
#            print load_dict
            return True
        except:
            return False

def print_result(input_str):
    if check_json(input_str):
        print "This is a valid json."
    else:
        print "Not a valid json."



if __name__ == '__main__':
    if (len(sys.argv) < 2):
        print "Usage:   python " + str(sys.argv[0]) + " <input_json>"
    else:
        print_result(str(sys.argv[1]))
