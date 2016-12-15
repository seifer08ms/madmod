#!/usr/bin/env python
import argparse
import yaml,os,pprint
p = argparse.ArgumentParser(
        description= 'module manager for madlib',
        prog='madmm')
subp = p.add_subparsers(help='commands')
path_module_yml=None
# sub-command function
def check_path(args):
    if not args.path_src_madlib:
        exit(p.print_usage())
    if not os.path.exists(args.path_src_madlib):
        exit("ERROR:path_src_madlib doesn't exist!\nPlease try again with correct parameters!")
    global path_module_yml
    if os.path.isfile(os.path.join(args.path_src_madlib,'config','Modules.yml')):
        path_module_yml = os.path.join(args.path_src_madlib,'config','Modules.yml')
    else:
        exit("ERROR:can't find Modules.yml!\nPlease try again with correct parameters!")

def subcmd_list(args):
    check_path(args)
    global path_module_yml
    fileobj = open(path_module_yml,'r')
    yy = yaml.load_all(fileobj)
#    print yaml.dump(yy,default_flow_style=False)
    for doc in yy:
        for key,v in doc.items():
            for vs in v:
                print 'module:%25s' % vs['name'],
                if vs.has_key('depends'):
                    print '\tdepends:',vs['depends'],
                print 
        print "\n",
def subcmd_create(args):
    print "create"
def subcmd_install(args):
    check_path(args)
    print "install"
def subcmd_uninstall(args):
    check_path(args) 
    print "uninstall"
def list_module(path):
    print "list_module"+path
# main function
def main():
    """ Runs program and handles command line options """
    path_src_madlib=os.environ.get('PATH_SRC_MADLIB',None)
    # A list command
    lp = subp.add_parser('list',help='List existing modules')
    lp.add_argument('-p','--path_src_madlib',default=path_src_madlib,action='store',help='src directory of MADlib.')
    lp.set_defaults(func=subcmd_list)
    # A create command
    cp = subp.add_parser('create',help='Create a module')
    cp.add_argument('dir',action='store',help='Create modules into target dir')
    cp.set_defaults(func=subcmd_create)
    # An install command
    ip = subp.add_parser('install',help='Install an existing module')
    ip.add_argument('dir',action='store',help='Install modules from dir')
    ip.add_argument('-p','--path_src_madlib',default=path_src_madlib,action='store',help='src directory of MADlib.')
    ip.set_defaults(func=subcmd_install)
    # An uninstall command
    up = subp.add_parser('uninstall',help='Remove an existing module')
    up.add_argument('modname',action='store',help='The module to uninstall')
    up.add_argument('-p','--path_src_madlib',default=path_src_madlib,action='store',help='src directory of MADlib.')
    up.set_defaults(func=subcmd_uninstall)
    # parse arguments
    args = p.parse_args()
    # call subcmd
    args.func(args)

if __name__ == '__main__':
    main()
