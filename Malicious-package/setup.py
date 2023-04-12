import setuptools
from setuptools.command.install import install
from setuptools.command.develop import develop
import subprocess
#  python setup.py sdist --formats=gztar

#URL = "http://<YOUR IP:PORT>"


def  wfile():
    f = open("Hacked.txt", "a")
    f.write(" !!!!!")
    f.close()
    
#wfile()




class AfterInstall(install):
    def run(self):
        install.run(self)
        wfile()
        
    


setuptools.setup(
    name = "malicious-pip-package",
    version = "1.0.0",
    author = "Penguin.inc",
    author_email = "malactor@example.com",
    description = "A test package to demonstrate malicious pip packages",
    long_description = "long description",
    long_description_content_type = "text/markdown",
    url = "https://github.com/teja156/autobot-clipper",
    project_urls = {
        "Bug Tracker": "https://github.com/teja156/autobot-clipper/issues",
    },
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir = {"": "src"},
    packages = setuptools.find_packages(where="src"),
    python_requires = ">=3.6",
    cmdclass={
        'install': AfterInstall,
    },
)