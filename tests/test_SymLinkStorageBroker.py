"""Test the dtool_symlink.storagebroker.SymLinkStorageBroker class."""

import os

import pytest

from . import tmp_dir_fixture  # NOQA
from . import TEST_SAMPLE_DATA


def test_SymLinkStroageBoker_functional(tmp_dir_fixture):  # NOQA

    from dtool_symlink.storagebroker import SymLinkStorageBroker

    uri = os.path.join(tmp_dir_fixture, "test_storage_broker")

    symlink_storage_broker = SymLinkStorageBroker(
        uri=uri,
        config_path=None)
    symlink_storage_broker.symlink_path = TEST_SAMPLE_DATA

    # Ensure it is not possible to overwrite data in it.
    with pytest.raises(NotImplementedError):
        symlink_storage_broker.put_item("dummy.txt", "dummy.txt")

    symlink_storage_broker.create_structure()

    assert os.path.islink(symlink_storage_broker._data_abspath)


def test_SymLinkStorageBroker_complete_cycle(tmp_dir_fixture):  # NOQA

    from dtool_symlink.storagebroker import SymLinkStorageBroker
    import dtoolcore

    name = "test_symlink_storage_broker"
    admin_metadata = dtoolcore.generate_admin_metadata(name)

    uri = "symlink:" + os.path.join(tmp_dir_fixture, name)

    symlink_storage_broker = SymLinkStorageBroker(
        uri=uri,
        config_path=None
    )
    symlink_storage_broker.symlink_path = TEST_SAMPLE_DATA
    symlink_storage_broker.create_structure()

    proto_dataset = dtoolcore.ProtoDataSet(uri, admin_metadata, None)
    proto_dataset._storage_broker = symlink_storage_broker

    proto_dataset.freeze()

    dataset = dtoolcore.DataSet.from_uri(uri)
    assert len(dataset.identifiers) == 7


def test_SymLinkStroageBoker_not_setting_symlink_path_attribute(tmp_dir_fixture):  # NOQA

    from dtool_symlink.storagebroker import SymLinkStorageBroker

    uri = os.path.join(tmp_dir_fixture, "test_storage_broker")

    symlink_storage_broker = SymLinkStorageBroker(
        uri=uri,
        config_path=None)

    with pytest.raises(AttributeError) as excinfo:
        symlink_storage_broker.create_structure()

    message = "The 'symlink_path' attribute needs to be added to the 'SymLinkStorageBroker' instance before calling the 'create_structure' method"  # NOQA
    assert excinfo.value.args[0] == message

def test_SymLinkStroageBoker_with_invalide_symlink_path(tmp_dir_fixture):  # NOQA

    from dtool_symlink.storagebroker import SymLinkStorageBroker

    uri = os.path.join(tmp_dir_fixture, "test_storage_broker")

    symlink_storage_broker = SymLinkStorageBroker(
        uri=uri,
        config_path=None)

    symlink_storage_broker.symlink_path = "/dont/exist"

    with pytest.raises(IOError) as excinfo:
        symlink_storage_broker.create_structure()

    message = "No such directory: '/dont/exist'"  # NOQA
    assert excinfo.value.args[0] == message
