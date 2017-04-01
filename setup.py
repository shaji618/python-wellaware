import sys
from setuptools import setup, find_packages

#next time:
#python setup.py register
#python setup.py sdist upload

version = open('wellaware/VERSION', 'r').readline().strip()
develop_requires = ['Sphinx==1.5.3',
    'coverage==4.3.4',
    'detox==0.10.0',
    'mock==2.0.0',
    'nose==1.3.7',
    'python-coveralls==2.9.0',
    'python-jose==1.3.2',
    'pytz==2016.10',
    'responses==0.5.1',
    'requests==2.13.0',
    'six>=1.10.0',
    'sphinx-rtd-theme==0.2.4',
    'tox==2.6.0',
    'watchdog==0.8.3',
    'wheel>=0.24.0']

long_desc = """
wellaware is an API Client to the WellAware API: https://api.wellaware.us/docs

`Documentation <https://wellaware.readthedocs.org/en/latest/>`_

`Report a Bug <https://github.com/wellaware/python-wellaware/issues>`_
"""

setup(
    name='wellaware',
    version=version,
    description='WellAware API Client',
    dependency_links=['https://github.com/wellaware/python-wellaware/archive/{0}.tar.gz#egg=wellaware-{0}'.format(version)],
    long_description=long_desc,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Environment :: Other Environment",
        "Environment :: Plugins",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Natural Language :: English",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: Implementation",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords='wellaware',
    install_requires=['six>=1.10.0',
                      'python-jose==1.3.2',
                      'pytz>=2016.10',
                      'requests==2.13.0'],
    extras_require={
        'develop': develop_requires,
        'docs': ['Sphinx>=1.5.3', 'sphinx-rtd-theme>=0.2.4', 'watchdog>=0.8.3'],
    },
    test_suite='nose.collector',
    tests_require=develop_requires,
    author='Cody Lee',
    author_email='codylee@wellaware.us',
    maintainer='Cody Lee',
    maintainer_email='codylee@wellaware.us',
    url='https://github.com/wellaware/python-wellaware',
    license='Apache Software License 2.0',
    packages=find_packages(),
    include_package_data=True,
)
