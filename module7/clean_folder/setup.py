from setuptools import setup, find_packages


setup(
    name='clean_folder',
    version='0.1.0',
    packages=find_packages(include=['clean_folder', 'clean_folder.*']),
    entry_points={'console_scripts': ['clean-folder = clean_folder.sort:main']}
)