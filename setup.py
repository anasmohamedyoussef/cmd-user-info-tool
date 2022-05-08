from setuptools import setup, find_packages
with open('README.md', encoding='UTF-8') as file:
    readme=file.read()
setup(
    name='cmdtool',
    version='1.0.0',
    description='cmd tool to get user info',
    author='Anas Mohamed',
    author_email='anasmohamedyoussef@gmail.com',
    packages=find_packages('src'),
    package_dir={'':'src'},
    install_requires=[],
    entry_points={
        'console_scripts': 'cmdtool=cmdtool.cli:main', #when installed create this executable
    },
)



