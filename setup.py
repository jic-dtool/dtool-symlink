from setuptools import setup

url = "https://github.com/jic-dtool/dtool-symlink"
version = "0.1.0"
readme = open('README.rst').read()

setup(
    name="dtool-symlink",
    packages=["dtool_symlink"],
    version=version,
    description="Add ability to create dataset where data directory is a symlink",
    long_description=readme,
    include_package_data=True,
    author="Tjelvar Olsson",
    author_email="tjelvar.olsson@jic.ac.uk",
    url=url,
    install_requires=[],
    entry_points={
        "dtool.storage_brokers": [
            "SymLinkStorageBroker=dtool_symlink.storagebroker:SymLinkStorageBroker",
        ],
    },
    download_url="{}/tarball/{}".format(url, version),
    license="MIT"
)
