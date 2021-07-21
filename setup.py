from setuptools import setup, find_packages
from io import open
from os import path
import pathlib

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

with open(path.join(HERE, 'requirements.txt'), encoding='utf-8') as f:
    all_reqs = f.read().split('\n')

install_requires = [x.strip() for x in all_reqs if ('git+' not in x) and (
    not x.startswith('#')) and (not x.startswith('-'))]
dependency_links = [x.strip().replace('git+', '') for x in all_reqs \
                    if 'git+' not in x]

setup (
	name = 'always_updates',
	description = 'always_updates updates your system, always.',
	version = '25.1',
	packages = find_packages(), # list of all packages
	install_requires = install_requires,
	python_requires='>=3.0',
	entry_points='''
	    [console_scripts]
	    aupd=always_updates.__main__:main
	''',
	author="Always Updates",
	keyword="updates, packages, software",
	long_description=README,
	long_description_content_type="text/markdown",
	license='MIT',
	url='https://github.com/alwaysupdates/always_updates',
	download_url='https://aupd.19700101t000000z.com',
	dependency_links=dependency_links,
	author_email='alwaysupdates@sixsixsigma.com',
	classifiers=[
	    "License :: OSI Approved :: MIT License",
	    "Programming Language :: Python :: 3"
	]
)