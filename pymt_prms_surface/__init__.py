#! /usr/bin/env python
import pkg_resources

__version__ = pkg_resources.get_distribution("pymt_prms_surface").version


from .bmi import PRMSSurface

__all__ = [
    "PRMSSurface",
]
