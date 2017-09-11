"""Symbolic link storage broker module."""

import os
from dtoolcore.storagebroker import DiskStorageBroker


def _get_data_directory():
    pass


class SymLinkStorageBroker(DiskStorageBroker):
    """SymLinkStorageBroker class."""

    def __init__(self, uri, config_path=None):
        super(SymLinkStorageBroker, self).__init__(uri, config_path)
        self._essential_subdirectories = [
            self._dtool_abspath,
            self._overlays_abspath
        ]

    def create_structure(self, get_data_dir_func=_get_data_directory):
        super(SymLinkStorageBroker, self).create_structure()
        data_directory = get_data_dir_func()
        os.symlink(data_directory, self._data_abspath)

    def put_item(self, fpath, relpath):
        raise(NotImplementedError())
