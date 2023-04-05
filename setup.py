from os.path import abspath, dirname, join
from setuptools import setup, find_packages

README_MD = open(join(dirname(abspath(__file__)), "README.md")).read()

if __name__ == '__main__':

    setup(
        name="quotapy", 
        version = "1.0",
        packages = find_packages(exclude='tests'),
        description = 'Quotas package',
        install_requires=[]
    )