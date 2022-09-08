from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in simple_inventory/__init__.py
from simple_inventory import __version__ as version

setup(
	name="simple_inventory",
	version=version,
	description="Inventory",
	author="Nxweb",
	author_email="info@nxwebin",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
