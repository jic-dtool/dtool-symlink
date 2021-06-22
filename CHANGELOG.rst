CHANGELOG
=========

This project uses `semantic versioning <http://semver.org/>`_.
This change log uses principles from `keep a changelog <http://keepachangelog.com/>`_.

[Unreleased]
------------

Added
^^^^^


Changed
^^^^^^^


Deprecated
^^^^^^^^^^


Removed
^^^^^^^


Fixed
^^^^^


Security
^^^^^^^^


[0.3.1] - 2021-06-23
--------------------

Fixed
^^^^^

- Licence file now included in release thanks to Jan Janssen (https://github.com/jan-janssen)


[0.3.0] - 2018-07-31
--------------------

Fixed
^^^^^

- Make ``SymlinkStorageBroker`` compatible with dtoolcore 3.4.0


[0.2.0] - 2018-02-09
--------------------

Changed
^^^^^^^

- Simplified the way to specify the symbolic link path in the
  SymLinkStorageBroker


[0.1.2] - 2017-10-25
--------------------

Fixed
^^^^^

- Fixed issue where the symbolic link was not fully resolved


[0.1.1] - 2017-10-25
--------------------

Fixed
^^^^^

- More graceful exit if one presses Cancel in file browser
- Data directory now falls back on click command line prompt if TkInter has issues
