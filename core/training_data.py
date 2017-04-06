#!/usr/bin/env python3

import pandas

# Attributes ( Input )
attr_data = pandas.read_csv( 'data/training_input.csv', skipinitialspace=True )

# Type ( Output )
type_data = pandas.read_csv( 'data/training_output.csv', skipinitialspace=True )
