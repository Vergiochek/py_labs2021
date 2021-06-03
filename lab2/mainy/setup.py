from setuptools import setup

setup(
    name='serializers',
    version='1.0',
    description='lab2',
    packages=['serializers'],
    author='Daniil Prokopovich',
    author_email='dendeskden@gmail.com',
    entry_points={
        'console_scripts': [
            'run = serializers.main:main'
        ]})
