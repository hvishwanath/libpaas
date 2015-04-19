__author__ = 'hvishwanath'

from setuptools import setup
#from distutils.core import setup
import sys, os
import platform


basedir = os.path.abspath(os.path.dirname(__file__))
reqfile = os.path.join(basedir, "requirements.txt")
if os.path.isfile(reqfile):
    install_requires = file(reqfile).read().split("\n")
else:
    install_requires = []

kwargs = {}
if sys.version_info[0] >= 3:
    from setuptools import setup
    kwargs['use_2to3'] = True

classifiers = [
    'Development Status :: 1 - Beta',
    'Environment :: Console',
    'Intended Audience :: Developers',
    'License :: Free',
    'Operating System :: POSIX',
    'Operating System :: MacOS :: MacOS X',
    'Programming Language :: Python :: 2.7',
    'Topic :: Utilities',
]

long_description = """paascli is a command line utility built using libpaas"""

setup(name='paascli',
      version='0.1',
      packages=['libpaas', 'libpaas.camp', 'libpaas.drivers', 'libpaas.paascli'],
      entry_points={
          'console_scripts': ['paascli = libpaas.paascli.paascli:paascli']
      },
      description="iox-client is a tool that helps in creating and managing applications for Cisco's IOx platforms",
      long_description=long_description,
      author='hvishwanath',
      author_email='harish.shastry@gmail.com',
      maintainer='hvishwanath',
      maintainer_email='harish.shastry@gmail.com',
      url='http://hvishwanath.net',
      license='Free',
      platforms='UNIX',
      classifiers=classifiers,
      install_requires=install_requires,
      **kwargs
      )
