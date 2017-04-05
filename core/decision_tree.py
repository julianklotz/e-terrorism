#!/usr/bin/env python3

from abstract_classifier import AbstractClassifier
from sklearn import tree
import numpy as np
import config

class DecisionTreeClassifier(AbstractClassifier):
    'Classifier based on decision trees'

    def __init__(self, tr_inpt, tr_outpt ):
        self.tree = []
        self.tr_inpt = tr_inpt
        self.tr_outpt = tr_outpt

        for i in range(0, len( tr_outpt.columns )):
            self.tree.append( tree.DecisionTreeRegressor() )
            self.tree[i].fit( tr_inpt, tr_outpt[tr_outpt.columns[i]] )

    def classify( self, attributes ):
        res = []
        for i in range(0, len( self.tr_outpt.columns )):
            res.append( self.tree[i].predict( attributes ))
        res = np.hstack( res )
        res = DataFrame( [ res ], columns=list(self.tr_outpt.columns) )
        return res;


if __name__ == '__main__':

    import training_data
    from pandas import DataFrame
    
    test = DecisionTreeClassifier( training_data.attr_data, training_data.type_data )
    a = test.classify(DataFrame( [[1,1,1,1]], columns=config.ATTRIBUTES ))
    print(a)
