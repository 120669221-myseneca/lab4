#!/usr/bin/env python3
# Author ID: [seneca_id]

def is_digits(sobj):
    for char in sobj:
        if char < '0' or char > '9':
            return False
    return True



    '''x = 'x'
    
    if x in sobj:
        return False
    else:
        return True'''



    # place code here - loop through each character in sobj

if __name__ == '__main__':
    test_list = ['x3058','3058','8503x','8503']
    for item in test_list:
        if is_digits(item):
            print(item,'is an integer.')
        else:
            print(item,'is not an integer.')