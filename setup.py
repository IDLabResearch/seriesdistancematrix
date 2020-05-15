from setuptools import setup
from setuptools import find_packages

setup(name='distancematrix',
      version='0.2',
      description='Library for dealing with distance matrix related calculations.',
      url='https://github.com/IDLabResearch/seriesdistancematrix',
      author='Dieter De Paepe',
      author_email='dieter.depaepe@ugent.be',
      license='All rights reserved',
      packages=find_packages(exclude=["distancematrix.tests*"]),
      classifiers=(
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          'Operating System :: OS Independent'
      ), install_requires=['numpy', 'scipy', 'pandas'])
