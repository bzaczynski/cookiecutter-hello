from setuptools import setup, find_packages


def load(filename):
    with open(filename, encoding='utf-8') as fp:
        return fp.read()


setup(
    name='{{ cookiecutter.project_name }}',
    version='{{ cookiecutter.version }}',
    author='{{ cookiecutter.author }}',
    license='MIT',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    scripts=[
        'bin/{{ cookiecutter.project_name }}_script.py'
    ],
    install_requires=load('requirements.txt').splitlines(),
    long_description=load('README.md'),
    long_description_content_type='text/markdown',
    test_suite='tests')
