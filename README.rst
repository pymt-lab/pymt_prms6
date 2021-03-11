=================
pymt_prms_surface
=================


.. image:: https://img.shields.io/badge/CSDMS-Basic%20Model%20Interface-green.svg
        :target: https://bmi.readthedocs.io/
        :alt: Basic Model Interface

.. image:: https://img.shields.io/badge/recipe-pymt_prms_surface-green.svg
        :target: https://anaconda.org/csdms-stack/pymt_prms_surface

.. image:: https://github.com/pymt-lab/pymt_prms_surface/actions/workflows/test.yml/badge.svg
        :target: https://github.com/pymt-lab/pymt_prms_surface/actions/workflows/test.yml

.. image:: https://github.com/pymt-lab/pymt_prms_surface/actions/workflows/flake8.yml/badge.svg
        :target: https://github.com/pymt-lab/pymt_prms_surface/actions/workflows/flake8.yml

.. image:: https://github.com/pymt-lab/pymt_prms_surface/actions/workflows/black.yml/badge.svg
        :target: https://github.com/pymt-lab/pymt_prms_surface/actions/workflows/black.yml

PyMT plugin for the PRMS6 Surface component


* Free software: MIT license
* Documentation: https://www.usgs.gov/software/precipitation-runoff-modeling-system-prms




=========== =====================================
Component   PyMT
=========== =====================================
PRMSSurface `from pymt.models import PRMSSurface`
=========== =====================================

---------------
Installing pymt
---------------

Installing `pymt` from the `conda-forge` channel can be achieved by adding
`conda-forge` to your channels with:

.. code::

  conda config --add channels conda-forge

*Note*: Before installing `pymt`, you may want to create a separate environment
into which to install it. This can be done with,

.. code::

  conda create -n pymt python=3
  source activate pymt

Once the `conda-forge` channel has been enabled, `pymt` can be installed with:

.. code::

  conda install pymt

It is possible to list all of the versions of `pymt` available on your platform with:

.. code::

  conda search pymt --channel conda-forge

----------------------------
Installing pymt_prms_surface
----------------------------

Once `pymt` is installed, the dependencies of `pymt_prms_surface` can
be installed. Start by appending `csdms-stack` to your channels with:

.. code::

  conda config --append channels csdms-stack

then install the dependencies with:

.. code::

  conda install bmi-fortran=2.0 prms prms_surface

To install `pymt_prms_surface`,

.. code::

  conda install pymt_prms_surface
