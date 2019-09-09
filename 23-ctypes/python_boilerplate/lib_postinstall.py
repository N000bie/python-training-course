import distutils.sysconfig
import os
import shutil
import sys
import time
import pkg_resources


def verify_destination(location):
    if not os.path.isdir(location):
        raise argparse.ArgumentTypeError("Path \"{}\" does not exist!".format(location))
    return location


try:
    # When this script is run from inside the bdist_wininst installer,
    # file_created() and directory_created() are additional builtin
    # functions which write lines to Python23\pywin32-install.log. This is
    # a list of actions for the uninstaller, the format is inspired by what
    # the Wise installer also creates.
    file_created
    is_bdist_wininst = True
except NameError:
    is_bdist_wininst = False  # we know what it is not - but not what it is :)


    def file_created(file):
        pass


    def directory_created(directory):
        pass


def install(destinations):
    my_dll = pkg_resources.resource_listdir('python_boilerplate', "dlls")
    target = os.path.dirname(sys.executable)

    print('post-install script, install dest:', destinations)
    print('python exe:', sys.executable)

    for dll in my_dll:
        dll_path = pkg_resources.resource_filename('python_boilerplate', os.path.join("dlls", dll))
        print('dll source path:', dll_path)
        print('dll dest path:', target)
        print('copying dll file...')
        shutil.copy2(dll_path, target)


def uninstall(destinations):
    my_dll = pkg_resources.resource_listdir('python_boilerplate', "dlls")
    target = os.path.dirname(sys.executable)

    print('post-install script, uninstall dest:', destinations)
    print('python exe:', sys.executable)

    for dll in my_dll:
        dll_path = os.path.join(target, dll)
        print('installed dll path:', dll_path)
        print('deleting dll file...')
        os.remove(dll_path)


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
                                     description="""A post-install script for the pywin32 extensions.
    * Typical usage:
    > python lib_postinstall.py -install
    If you installed lib via a .exe installer, this should be run
    automatically after installation, but if it fails you can run it again.
    If you installed lib via PIP, you almost certainly need to run this to
    setup the environment correctly.
    Execute with script with a '-install' parameter, to ensure the environment
    is setup correctly.
    """)
    parser.add_argument("-install",
                        default=False,
                        action='store_true',
                        help="Configure the Python environment correctly for pywin32.")
    parser.add_argument("-remove",
                        default=False,
                        action='store_true',
                        help="Try and remove everything that was installed or copied.")
    parser.add_argument("-wait",
                        type=int,
                        help="Wait for the specified process to terminate before starting.")
    parser.add_argument("-silent",
                        default=False,
                        action='store_true',
                        help="Don't display the \"Abort/Retry/Ignore\" dialog for files in use.")
    parser.add_argument("-quiet",
                        default=False,
                        action='store_true',
                        help="Don't display progress messages.")
    parser.add_argument("-destination",
                        default=distutils.sysconfig.get_python_lib(plat_specific=1),
                        type=verify_destination,
                        help="Location of the lib installation")

    args = parser.parse_args()

    if not args.quiet:
        print("Parsed arguments are: {}".format(args))

    if not args.install ^ args.remove:
        parser.error("You need to either choose to -install or -remove!")

    if args.wait is not None:
        try:
            os.waitpid(args.wait, 0)
        except AttributeError:
            # Python 2.2 - no waitpid - just sleep.
            time.sleep(3)
        except os.error:
            # child already dead
            pass

    silent = args.silent
    verbose = not args.quiet

    if args.install:
        install(args.destination)

    if args.remove:
        if not is_bdist_wininst:
            uninstall(args.destination)
