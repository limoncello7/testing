from setuptools import setup, find_packages

setup(
    name='comp0035-testing',
    version='1.0',
    author='Sarah Sanders',
    url='https://github.com/nicholsons/comp0035-testing',
    python_requires='>=3.10',
    packages=find_packages(),
    install_requires=[
        'pytest',
        'pytest-cov'
    ],
)
