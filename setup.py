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
    'License :: MIT',
    'Operating System :: POSIX',
    'Operating System :: MacOS :: MacOS X',
    'Programming Language :: Python :: 2.7',
    'Topic :: Utilities',
]

long_description = """paascli is a command line utility built using libpaas. It will help you manage CAMP compliant applications across multiple PaaS providers seamlessly"""

setup(name='paascli',
      version='0.1',
      packages=['libpaas', 'libpaas.camp', 'libpaas.drivers', 'libpaas.paascli'],
      entry_points={
          'console_scripts': ['paascli = libpaas.paascli.paascli:paascli']
      },
      description="paascli is a CLI toolbelt to manage CAMP compliant apps across multiple PaaS providers",
      long_description=long_description,
      author='Harish Vishwanath',
      author_email='harish.shastry@gmail.com',
      maintainer='Harish Vishwanath',
      maintainer_email='harish.shastry@gmail.com',
      url='https://github.com/hvishwanath/libpaas',
      download_url = "https://github.com/hvishwanath/libpaas/tarball/master",
      keywords = ['testing', 'logging', 'example'], # arbitrary keywords
      license='MIT',
      platforms='UNIX',
      classifiers=classifiers,
      install_requires=install_requires,
      **kwargs
      )
