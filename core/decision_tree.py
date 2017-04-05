#!/usr/bin/env python3

import numpy
from sklearn import tree as Tree
from pandas import DataFrame

from core.abstract_classifier import AbstractClassifier

class DecisionTreeClassifier(AbstractClassifier):
    'Classifier based on decision trees'

    def __init__(self, tr_inpt, tr_outpt ):
        self.tree = []
        self.tr_inpt = tr_inpt
        self.tr_outpt = tr_outpt

        for i in range(0, len( tr_outpt.columns )):
            self.tree.append( Tree.DecisionTreeRegressor() )
            self.tree[i].fit( tr_inpt, tr_outpt[ tr_outpt.columns[ i ]])

    def classify( self, attributes ):
        res = []
        for i in range(0, len( self.tr_outpt.columns )):
            res.append( self.tree[i].predict( attributes ))
        res = numpy.hstack( res )
        res = DataFrame( [ res ], columns=self.tr_outpt.columns.values )
        return self.rank( res );

    def rank( self, result, ascending=False ):
        res = result.sort_values( [0], ascending=ascending, axis=1 )
        cols = res.columns.values
        return filter( lambda x: res[x][0] != 0, cols )

