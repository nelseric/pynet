from setuptools import setup, find_packages

setup(
    name='pynet',
    version='0.0.1',
    packages = find_packages(),
    url='',
    license='',
    author='Eric Nelson',
    author_email='gauntletguy2@gmail.com',
    description='',
    entry_points = {
      'console_scripts': [
        'pynet = pynet.main:main',
      ]
    }
)
