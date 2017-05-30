# Begin: Python 2/3 compatibility header small
# Get Python 3 functionality:
from __future__ import\
    absolute_import, print_function, division, unicode_literals
from future.utils import raise_with_traceback, raise_from
# catch exception with: except Exception as e
from builtins import range, map, zip, filter
from io import open
import six
# End: Python 2/3 compatability header small


###############################################################################
###############################################################################
###############################################################################


from . import base


__all__ = [
    "log_reg",

    "mlp_1dense",
    "mlp_2dense",

    "cnn_1convb_1dense",
    "cnn_2convb_1dense",
    "cnn_2convb_2dense",
    "cnn_3convb_2dense",
]


###############################################################################
###############################################################################
###############################################################################


__input_shape__ = [None, 1, 28, 28]
__output_n__ = 10


###############################################################################
###############################################################################
###############################################################################


def log_reg(nonlinearity):
    return base.log_reg(__input_shape__, __output_n__, nonlinearity)


###############################################################################
###############################################################################
###############################################################################


def mlp_1dense(nonlinearity):
    return base.mlp_1dense(__input_shape__, __output_n__, nonlinearity,
                           dense_units=512, dropout_rate=0.25)


def mlp_2dense(nonlinearity):
    return base.mlp_2dense(__input_shape__, __output_n__, nonlinearity,
                           dense_units=512, dropout_rate=0.25)


###############################################################################
###############################################################################
###############################################################################


def cnn_1convb_1dense(nonlinearity):
    return base.cnn_1convb_1dense(__input_shape__, __output_n__, nonlinearity,
                                  dense_units=512, dropout_rate=0.25)


def cnn_2convb_1dense(nonlinearity):
    return base.cnn_2convb_1dense(__input_shape__, __output_n__, nonlinearity,
                                  dense_units=512, dropout_rate=0.25)


def cnn_2convb_2dense(nonlinearity):
    return base.cnn_2convb_2dense(__input_shape__, __output_n__, nonlinearity,
                                  dense_units=512, dropout_rate=0.25)


def cnn_3convb_2dense(nonlinearity):
    return base.cnn_3convb_2dense(__input_shape__, __output_n__, nonlinearity,
                                  dense_units=512, dropout_rate=0.25)