#!/usr/bin/env python3

from pandas import DataFrame
import core.config as CFG

attr_data = DataFrame([[1,1,1,1], [2,2,2,2], [3,3,3,3], [4,4,4,4]], columns=CFG.ATTRIBUTES)

type_data = DataFrame([[1,1,1], [2,2,2], [3,3,3], [4,4,4]], columns=CFG.TYPES)
