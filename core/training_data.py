#!/usr/bin/env python3

from pandas import DataFrame
import config

attr_data = DataFrame([[1,1,1,1], [2,2,2,2], [3,3,3,3], [4,4,4,4]], columns=config.ATTRIBUTES)

type_data = DataFrame([[1,1,1], [2,2,2], [3,3,3], [4,4,4]], columns=config.TYPES)
