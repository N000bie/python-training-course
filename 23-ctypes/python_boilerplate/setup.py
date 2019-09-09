#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import subprocess
import sys

from setuptools.command.install import install

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ["requests"]

setup_requirements = []

test_requirements = []

post_install_script = 'lib_postinstall.py'


class MyInstall(install):
    def run(self):
        install.run(self)
        # Custom script we run at the end of installing - this is the same script
        # run by bdist_wininst
        # This child process won't be able to install the system DLLs until our
        # process has terminated (as distutils imports win32api!), so we must use
        # some 'no wait' executor - spawn seems fine!  We pass the PID of this
        # process so the child will wait for us.
        # XXX - hmm - a closer look at distutils shows it only uses win32api
        # if _winreg fails - and this never should.  Need to revisit this!
        # If self.root has a value, it means we are being "installed" into
        # some other directory than Python itself (eg, into a temp directory
        # for bdist_wininst to use) - in which case we must *not* run our
        # installer
        if not self.dry_run and not self.root:
            # We must run the script we just installed into Scripts, as it
            # may have had 2to3 run over it.
            filename = os.path.join(self.install_scripts, post_install_script)
            if not os.path.isfile(filename):
                raise RuntimeError("Can't find '%s'" % (filename,))
            print("Executing post install script...")
            # What executable to use?  This one I guess.
            subprocess.Popen([
                sys.executable, filename,
                "-install",
                "-destination", self.install_lib,
                "-quiet",
                "-wait", str(os.getpid()),
            ])


cmdclass = {
    'install': MyInstall,
}

setup(
    author="j",
    author_email='audreyr@example.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="Python Boilerplate contains all the boilerplate you need to create a Python package.",
    install_requires=requirements,
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='python_boilerplate',
    name='python_boilerplate',
    packages=find_packages(include=['python_boilerplate']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/audreyr/python_boilerplate',
    version='0.1.0',
    zip_safe=False,

    cmdclass=cmdclass,
    options={"bdist_wininst":
                 {"install_script": post_install_script,
                  "title": "pywin32-%s" % ('0.1.0',),
                  "user_access_control": "auto",
                  },
             "bdist_msi":
                 {"install_script": post_install_script,
                  },
             },

    scripts=[post_install_script, ],
    package_data={
        # If any package contains *.txt or *.rst files, include them:
        '': ['*.dll',],
    }
)
