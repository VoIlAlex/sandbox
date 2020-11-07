from distutils.core import setup
from setuptools import find_packages
setup(
    name='sandbox',         # How you named your package folder (MyLib)
    packages=find_packages('.'),   # Chose the same as "name"
    # Start with a small number and increase it with every change you make
    version='1.0.0',
    # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    license='MIT',
    # Give a short description about your library
    description='Collection of generators for generating points of different distributions.',
    author='Ilya Vouk',                   # Type in your name
    author_email='ilya.vouk@gmail.com',      # Type in your E-Mail
    # Keywords that define your package best
    scripts=['bin/sandbox'],
    keywords=['sandbox'],
    install_requires=[            # I get to this in a second
    ],
    classifiers=[
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Development Status :: 3 - Alpha',
        # Define that your audience are developers
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering',
        'License :: OSI Approved :: MIT License',   # Again, pick a license
        # Specify which python versions that you want to support
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ]
)
