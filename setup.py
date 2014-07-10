from setuptools import setup, find_packages

version = '0.2.0'

setup(
    name='cmsplugin-plaintext',
    version=version,
    description='Adds a plaintext plugin for django-cms.',
    author='Xenofox, LLC',
    author_email='info@xenofox.com',
    url='http://bitbucket.org/xenofox/cmsplugin-plaintext/',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=[],
)
