============
Installation
============

Via pip
-------

.. danger::
    There is a ``PyCard`` on PyPI but that is **NOT** this package!

    Do **NOT** simply ``pip install pycard`` or you will end up with that address card program!

From github::

    pip install -e git://github.com/xguse/pycard.git@v0.0.1#egg=pycard

or for the very latest::

    pip install -e git://github.com/xguse/pycard.git@master#egg=pycard

or for the very VERY latest::

    pip install -e git://github.com/xguse/pycard.git@develop#egg=pycard


Via conda
---------

Via my personal repo manually::

    conda install pycard -c http://xguse.github.io/conda-package-repo/pkgs/channel/


Or add the repo to your `.condarc` to search the repo whenever you do ``conda install``::

    conda config --add channels http://xguse.github.io/conda-package-repo/pkgs/channel/
    conda install pycard
