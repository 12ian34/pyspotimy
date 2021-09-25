from setuptools import find_packages, setup

setup(name='pyspotimy',
      version='0.1',
      packages=find_packages(),
      install_requires=[
          'requests==2.25.1',
          'autopep8==1.5.7',
      ])
