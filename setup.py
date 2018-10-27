from setuptools import find_packages, setup

REQUIRED_PACKAGES = ['tensorflow>=1.8']

setup(
	name='artiBlue',
	version='0.1',
	install_requires=REQUIRED_PACKAGES,
	packages=find_packages(),
	include_package_data=True,
	description='my first model'
)