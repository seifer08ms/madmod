#!/usr/bin/env python
import argparse
import yaml,os
# sub-command function
def subcmd_list(args):
    print "list"

def subcmd_create(args):
    print "create"

def subcmd_remove(args):
    print "remove"

def main():
    """ Runs program and handles command line options """
    p = argparse.ArgumentParser(
        description= 'module manager for madlib',
        prog='madmod')
    subp = p.add_subparsers(help='commands')
    # A list command
    lp = subp.add_parser('list',help='List existing modules')
    lp.add_argument('dirname',action='store',help='Directory to list')
    lp.set_defaults(func=subcmd_list)
    # A create command
    cp = subp.add_parser('create',help='Create a module')
    cp.add_argument('dirname',action='store',help='Directory to create module')
    cp.set_defaults(func=subcmd_create)
    # A remove command
    rp = subp.add_parser('remove',help='Remove an existing module')
    rp.add_argument('modname',action='store',help='The module to remove')
    rp.set_defaults(func=subcmd_remove)

    args = p.parse_args()
    #call subcmd
    args.fun(args)
    path_madlib_src = os.environ.get('PATH_MADLIB_SRC')
    if path_madlib_src != None:
        print path_madlib_src
if __name__ == '__main__':
    main()
