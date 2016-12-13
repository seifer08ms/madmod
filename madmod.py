#!/usr/bin/env python
import optparse
import yaml
def main():
    """ Runs program and handles command line options """
    p = optparse.OptionParser(
        description= 'module manager for madlib',
        prog='madmod',
        version='madmod 0.1',
        usage='%prog [init|add|remove|list]')
    p.add_option('-i','--init',action='store_true',help='initialize the destination folder of module')
    p.add_option('-d','--add',action='store_true',help='add the destination folder of module')
    p.add_option('-l','--list',action='store_true',help='list all modules in configure file')
    p.add_option('-p','--prefix',action='store_true',help='set the prefix of path for config file')
    options,arguments = p.parse_args()
    if len(arguments) < 1:
        print "Warning:Missing arguments! Please check the usage:"
        p.print_help()
    else:
        if len(arguments) == 1 :
            print (arguments)
        if options.prefix:
            print arguments
            
if __name__ == '__main__':
    main()
