"""Function module that contains all custom functions used.

    Author: Moritz Scharff
    E-Mail: moritz.scharff@pucp.edu.pe
    ORCID:  0000-0002-1581-7668
"""

import numpy as np
from scipy import signal
from scipy.fft import fft, fftfreq
import matplotlib.pyplot as plt


def fun_test(x):
    """Use the test fun to check how Sphinx and Python work.

        :param x: x is a input variable
        :type x: float
        :return: this is the output of the function
        :rtype: float vector

        .. note::

            This can be used to highlight anything...

        """
    z = x + 1
    return z
