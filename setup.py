
from setuptools import setup

setup(
    name='projconverter',
    version='0.0.1',
    author='Andrew Yushkevich',
    author_email='andrew.yushkevich@emlid.com',
    packages=['projconverter'],
    install_requires=['pyproj'],
    license = 'BSD-3-Clause',
    url='https://github.com/andrewyushkevich/projconverter',
    description='Pyproj Converter for terminal',
    long_description=open('README.md').read(),
    entry_points = {
        'console_scripts': [
            'projconverterr = projconverter.projconverter:main',
        ],
    },
)
