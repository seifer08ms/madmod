#!/usr/bin/env python
import argparse
import yaml,os
# sub-command function
def subcmd_list(args):
    print "list"

def subcmd_create(args):
    print "create"

def subcmd_install(args):
    print "install"

def subcmd_uninstall(args):
    print "uninstall"

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
    cp.add_argument('dirname',action='store',help='Create modules into dirname')
    cp.set_defaults(func=subcmd_create)
    # An install command
    ip = subp.add_parser('install',help='Install an existing module')
    ip.add_argument('dirname',action='store',help='Install modules from dirname')
    ip.set_defaults(func=subcmd_install)
    # An uninstall command
    up = subp.add_parser('uninstall',help='Remove an existing module')
    up.add_argument('modname',action='store',help='The module to uninstall')
    up.set_defaults(func=subcmd_uninstall)

    args = p.parse_args()
    #call subcmd
    args.func(args)
    path_madlib_src = os.environ.get('PATH_MADLIB_SRC')
    if path_madlib_src != None:
        print path_madlib_src
if __name__ == '__main__':
    main()
