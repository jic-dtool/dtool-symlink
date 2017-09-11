"""Test the dtool_symlink.storagebroker.SymLinkStorageBroker class."""

import os

import pytest

from . import tmp_dir_fixture  # NOQA
from . import TEST_SAMPLE_DATA


def test_SymLinkStroageBoker_functional(tmp_dir_fixture):  # NOQA

    from dtool_symlink.storagebroker import SymLinkStorageBroker

    def get_data_dir():
        return TEST_SAMPLE_DATA

    uri = os.path.join(tmp_dir_fixture, "test_storage_broker")

    symlink_storage_broker = SymLinkStorageBroker(
        uri=uri,
        config_path=None)

    # Ensure it is not possible to overwrite data in it.
    with pytest.raises(NotImplementedError):
        symlink_storage_broker.put_item("dummy.txt", "dummy.txt")

    symlink_storage_broker.create_structure(get_data_dir_func=get_data_dir)

    assert os.path.islink(symlink_storage_broker._data_abspath)
