from distutils.core import setup
from setuptools import setup, find_packages
import py2exe


setup(
    console=['manage.py'],
    packages=find_packages(include=['htmx', 'htmx.*']),
    options={
        'py2exe': {
            'includes': ['django',],
            'excludes': ['Tkinter'],
            'packages': ['htmx', 'todo','film','media','templates',],
            'dist_dir': 'dist',
        }
    },
    data_files=[('.', ['manage.py', 'htmx/settings.py'])],
)