#!/usr/bin/env python
import optparse

def main():
    """ Runs program and handles command line options """
    p = optparse.OptionParser(
        description= 'module manager for madlib',
        prog='madmod',
        version='madmod 0.1',
        usage='%prog [init|add|remove]')
    p.add_option('-i','--init',help='initialize the destination folder of module')
    p.add_option('-d','--add',help='add the destination folder of module')
    options,arguments = p.parse_args()
    if len(arguments) == 1 :
        print (arguments)

if __name__ == '__main__':
    main()
