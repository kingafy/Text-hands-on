# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 16:50:54 2018

@author: Anshuman_Mahapatra
"""

####My hands on Text

categories = ['alt.atheism', 'soc.religion.christian','comp.graphics', 'sci.med']
from sklearn.datasets import fetch_20newsgroups
twenty_train = fetch_20newsgroups(subset='train',categories=categories, shuffle=True, random_state=42)
