from distutils.core import setup

setup(
    name='scriptable',
    packages=['scriptable'],
    version='0.1.0',
    license='APACHE2',
    description='Scriptable is a sand-boxed scripting engine which can be used in an embedded environment.',
    author='x-and-y',
    author_email='christian.weber@leftshift.one',
    url='https://github.com/c7nw3r/scriptable',
    download_url='https://github.com/c7nw3r/scriptable/archive/refs/tags/v0.1.0.tar.gz',
    keywords=['scripting-engine'],
    install_requires=[
        'antlr4-python3-runtime'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Scripting Engine',
        'License :: OSI Approved :: APACHE2 License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
