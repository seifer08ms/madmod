#!/usr/bin/env python
import argparse
import yaml
def main():
    """ Runs program and handles command line options """
    p = argparse.ArgumentParser(
        description= 'module manager for madlib',
        prog='madmod',
        usage='%(prog)s [options]')
    p.add_argument('--init',action='store',help='initialize the destination folder of module')
    p.add_argument('--add',action='store',help='add the destination folder of module')
    p.add_argument('--list',action='store_true',help='list all modules in configure file')
    p.add_argument('--prefix',action='store',help='set the prefix of path for config file')
    p.parse_args()
#    p.print_help()
if __name__ == '__main__':
    main()
