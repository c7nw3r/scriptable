# read the contents of your README file
from pathlib import Path

from setuptools import find_packages, setup

long_description = Path(__file__).with_name("README.md").read_text()

setup(
    name='scriptable',
    packages=find_packages(exclude=("__tests__",)),
    version='0.1.5',
    license='Apache Software License',
    description='Scriptable is a sand-boxed scripting engine which can be used safely in an embedded environment.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='x-and-y',
    author_email='christian.weber@leftshift.one',
    url='https://github.com/c7nw3r/scriptable',
    download_url='https://github.com/c7nw3r/scriptable/archive/refs/tags/v0.1.5.tar.gz',
    keywords=['scripting-engine'],
    setup_requires=['setuptools_scm'],
    include_package_data=True,
    install_requires=[
        'antlr4-python3-runtime'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Interpreters',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
