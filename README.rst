=================
pymt_prms_surface
=================


.. image:: https://img.shields.io/badge/CSDMS-Basic%20Model%20Interface-green.svg
        :target: https://bmi.readthedocs.io/
        :alt: Basic Model Interface

.. image:: https://img.shields.io/badge/recipe-pymt_prms_surface-green.svg
        :target: https://anaconda.org/csdms-stack/pymt_prms_surface

.. image:: https://img.shields.io/travis/csdms/pymt_prms_surface.svg
        :target: https://travis-ci.org/pymt-lab/pymt_prms_surface

.. image:: https://readthedocs.org/projects/pymt_prms-surface/badge/?version=latest
        :target: https://pymt_prms-surface.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
        :target: https://github.com/csdms/pymt
        :alt: Code style: black


PyMT plugin for the PRMS6 Surface component


* Free software: MIT license
* Documentation: https://prms-surface.readthedocs.io.




=========== =====================================
Component   PyMT
=========== =====================================
PRMSSurface `from pymt.models import PRMSSurface`
=========== =====================================

---------------
Installing pymt
---------------

*Note*: Before installing `pymt`, you may want to create a separate environment
into which to install it. This can be done with,

.. code::

  conda create -n pymt python=3 -c conda-forge
  source activate pymt

Install `pymt` with:

.. code::

  conda install pymt -c conda-forge

It is possible to list all of the versions of `pymt` available on your platform with:

.. code::

  conda search pymt -c conda-forge

----------------------------
Installing pymt_prms_surface
----------------------------

Once `pymt` is installed, the dependencies of `pymt_prms_surface` can
be installed with:

.. code::

  conda install bmi-fortran=2.0 prms prms_surface -c conda-forge -c csdms-stack

To install `pymt_prms_surface`,

.. code::

  conda install pymt_prms_surface -c conda-forge -c csdms-stack
