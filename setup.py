import os
from setuptools import setup, find_packages
import backdrop

requires = [
    "Flask==0.9",
    "Flask-Negotiate",
    "pymongo==2.5",
    "python-dateutil==2.1",
    "pytz==2013b",
]

readme_path = os.path.join(os.path.dirname(__file__), 'README.rst')
long_description = open(readme_path).read()

setup(
    # Package metadata
    name=backdrop.__title__,
    version=backdrop.__version__,
    description='The backend applications for the Performance Platform',
    long_description=long_description,
    author=backdrop.__author__,
    author_email='none@nowhere',
    url='https://github.com/alphagov/backdrop',
    license='https://github.com/alphagov/backdrop/master/LICENCE.txt',

    # Package configuration
    packages=find_packages(exclude=['tests*', 'features*']),
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
)
