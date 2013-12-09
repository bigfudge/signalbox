import os
from pip.req import parse_requirements
from setuptools import setup, find_packages

reqs = parse_requirements("requirements.txt")
install_reqs = [str(ir.req) for ir in reqs]
scripts = ['bin/heroku_install_signalbox', ]

setup(
    name='signalbox',
    version='0.2.2',
    author='Ben Whalley',
    author_email='benwhalley@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    scripts=scripts,
    url='http://pypi.python.org/pypi/signalbox/',
    license='LICENSE.txt',
    description='Run longitudinal studies and randomised trials over the web and telephone.',
    long_description=open('README.txt').read(),
    install_requires=install_reqs,
    entry_points={
            'console_scripts': [
                'make_s3_bucket = signalbox.utilities.bootstrap:make_s3_bucket',
                'make_secret_key = signalbox.utilities.bootstrap:make_secret_key',
            ]
    }
)
