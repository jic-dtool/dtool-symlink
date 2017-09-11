"""Test the dtool_symlink package."""


def test_version_is_string():
    import dtool_symlink
    assert isinstance(dtool_symlink.__version__, str)
