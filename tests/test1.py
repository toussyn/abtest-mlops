import sys
import os
import unittest
import numpy as np
import pandas as pd
import pandas.api.types as ptypes

from ..scripts.data_info_and_preprocessing import dataInfo
from ..scripts.data_info_and_preprocessing import data_preprocessing

class TestCases(unittest.TestCase):

    def test_class_creation(self):
        data_Info = dataInfo(self.df)
        self.assertEqual(self.df.info(), data_Info.df.info())

    def test_remove_duplicates(self):
        data_preprocess = data_preprocessing(self.df)
        data_preprocess.remove_duplicates()
        self.assertEqual(data_preprocess.df.shape[0], self.df.shape[0])