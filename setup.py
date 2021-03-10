import pathlib
from setuptools import setup, find_packages

classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python::3.9'
]

setup(
    name='DEfitnessFunction',
    version='0.0.1',
    description='this library is besically for fitness function of DE',
    Long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.txt').read(),
    url='',
    author='Pawan Mishra',
    author_email='pawanmishra0532@gmail.com',
    license='MIT',
    classifiers='classifiers',
    keyword='Differential Evolution,Fitness function Code,Cost_function_library',
    packages=find_packages(),
    install_requires=[' ']
)