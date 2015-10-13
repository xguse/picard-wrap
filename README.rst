======
pycard
======

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |appveyor|
        | |codecov|
    * - package
      - |version| |downloads|

.. |docs| image:: https://readthedocs.org/projects/pycard/badge/?style=flat
    :target: https://readthedocs.org/projects/pycard
    :alt: Documentation Status

.. |travis| image:: https://img.shields.io/travis/xguse/pycard/master.svg?style=flat&label=Travis
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/xguse/pycard

.. |appveyor| image:: https://img.shields.io/appveyor/ci/xguse/pycard/master.svg?style=flat&label=AppVeyor
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/xguse/pycard


.. |codecov| image:: https://img.shields.io/codecov/c/github/xguse/pycard/master.svg?style=flat&label=Codecov
    :alt: Coverage Status
    :target: https://codecov.io/github/xguse/pycard


This script facilitates calling `/path/to/picard.jar`. Its purpose is to allow you to call picard without providing
or even knowing the full path to the executable far file.

* Free software: MIT license

=====
Usage
=====

To use pycard in a from the command line::

    $ pycard --help
    Usage: pycard [OPTIONS] COMMAND [ARGS]...

      This script facilitates calling `/path/to/picard.jar`.

      Its purpose is to allow you to call picard without providing or even
      knowing the full path to the executable far file.

    Options:
      --use-path PATH  Provide a path to override the default picard.jar location.
      --version        Show the version and exit.
      --help           Show this message and exit.

    Commands:
      do    runs picard
      help  shows the picard.jar help text


::

    $ pycard do --help
    Usage: pycard do [OPTIONS] [PICARD_ARG]...

      This command actually calls picard.

      PICARD_ARG          These will be passed directly to picard.

      The help text for picard can be accessed by providing zero PICARD_ARGs.


      Example usages:

          picard do PicardCommandName OPTION1=value1 OPTION2=value2...
          picard do --jvm-args '-Xmx6g' PicardCommandName OPTION1=value1 OPTION2=value2...
          picard do PicardCommandName OPTION1=value1 OPTION2=value2... --jvm-args '-Xmx6g'

    Options:
      --jvm-args TEXT  a quoted string that contains the args you wish to pass to
                       the java virtual machine.  [default: '-Xmx2g']
      --help           Show this message and exit.




Installation
============

.. danger::
    There is a ``PyCard`` on PyPI but that is **NOT** this package!

    Do **NOT** simply ``pip install pycard`` or you will end up with that address card program!

::

    git clone https://github.com/xguse/pycard.git
    cd pycard
    pip install .


Or via conda::

    conda install pycard -c http://xguse.github.io/conda-package-repo/pkgs/channel/

Documentation
=============

https://pycard.readthedocs.org/

Development
===========

To run the all tests run::

    tox
