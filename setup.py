from setuptools import setup, find_packages, Command
import os

from weed.version import __version__

DESCRIPTION = "A python module for weed-fs"

LONG_DESCRIPTION = None
try:
    LONG_DESCRIPTION = open('README.md').read()
except:
    pass


CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Internet',
    'Topic :: Software Development :: Libraries :: Python Modules',
]


class PyTest(Command):
    ''' class for py.test '''
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import sys,subprocess
        # "test.pytest.py" is a file generated by command:
        #   "  py.test --genscript=test.pytest.py  "
        pytest_file = 'weed/_test_weed_pytest.py'
        errno = subprocess.call([sys.executable, pytest_file])
        raise SystemExit(errno)


setup(name='python-weed',
      version=__version__,
      packages=find_packages(),
      author='darkdarkfruit',
      author_email='darkdarkfruit@gmail.com',
      url='https://github.com/darkdarkfruit/python-weed',
      license='MIT',
      include_package_data=True,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      platforms=['any'],
      classifiers=CLASSIFIERS,
      install_requires=['requests'],
      requires=['requests'],
      cmdclass = {'test' : PyTest},
#      test_suite='py.test',
)
