Python API Client
=================


To Deploy
---------

To deploy packages using the deploy script your must ammend your ~/.pypirc file:

    [distutils]
    index-servers = local
    [local]
    repository: http://artifactory.wellaware.us/artifactory/api/pypi/pypi
    username: <USERNAME>
    password: <PASSWORD>

then run the deploy_to_pypi.sh script

    ./deploy_to_pypi.sh


Install as Dependency
--------------------

To resolve packages you must add the following to your ~/.pip/pip.conf or add it as a resolver in the requirements.pip/requirements.txt

    [global]
    index-url = http://artifactory.wellaware.us/artifactory/api/pypi/pypi/simple

To install:

    pip install wellaware


