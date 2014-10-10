from setuptools import setup, find_packages

setup(
    packages = find_packages(), #['http', 'yieldfrom.http'],
    package_dir = {'yieldfrom': 'yieldfrom'},
    version = '0.1',
    namespace_packages = ['yieldfrom'],
    name = 'yieldfrom.http.client',
    description = 'asyncio version of http.client',
    install_requires = ['setuptools',],
    )