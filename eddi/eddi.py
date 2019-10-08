# -*- coding: utf-8 -*-
"""
Tools for calculating the Evaporative Demand Drought Index (EDDI) from reference evapotransipiration data.
"""
import pandas as pd
import numpy as np
import bottleneck as bn
from statsmodels.sandbox.stats import stats_mstats_short as sms
from scipy import stats

class EDDI(object):
    """
    Object for managing input/output data and the calculation of
    Evaporative-Demand-Drought-Index

    """

    def __init__(self, df=None):
        if df is not None and not isinstance(df, pd.DataFrame):
            raise TypeError("Must assign a pandas.DataFrame object")
        self._df = df

        # may add options to initialize from a config path or xarray object

    @property
    def df(self):
        """
        :obj:`pandas.DataFrame` containing input time series data
        needed to run :obj:`EDDI` methods.
        """
        if isinstance(self._df, pd.DataFrame):
            return self._df

    @df.setter
    def df(self, df):
        if not isinstance(df, pd.DataFrame):
            raise TypeError("Must assign a pandas.DataFrame object")
        self._df = df


def eddi_1d(eto, ts):        
    """ 
    Compute the Evaporative Demand Drought Index (EDDI) from monthly
    reference evapotranspiration (eto). Step 1 is to compute the running
    sum of eto based on user defined time scale (ts). Step 2 is obtain the
    empirical probabilities from plotting positions. Step 3 is to transform
    probabilities using an inverse normal distribution.
    
    Arguments:
        eto (:obj:`numpy.ndarray`): time series of daily eto
        ts (int): time scale input as an integer (units in freq. of ``eto``)
    
    Returns:
        eddi (:obj:`numpy.ndarray`): 1-D of EDDI for period of record
    
    """
    print('calculating EDDI')
    
    # Compute running soms based on time scale (ts)
    acc = bn.move_sum(eto, ts)
    
    # Compute plotting positions to obtain daily CDF
    # First, reshape array back to day x year
    acc = np.reshape(acc, (len(acc)//365, 365))
    
    # Tukey plotting positions
    pp = sms.plotting_positions(
        acc, alpha=1./3., beta=1./3., axis=0, masknan=True
    )
    
    # Transformation through inverse normal
    eddi = stats.norm.ppf(pp)
    
    eddi = eddi.ravel()
    
    return eddi
