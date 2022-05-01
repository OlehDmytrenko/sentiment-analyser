#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 13:12:17 2022

@author: dmytrenko.o
"""

import sys
stdOutput = open("outlog.log", "w")
sys.stderr = stdOutput
sys.stdout = stdOutput


def predict_emotion(text, model, predictLimit):
    try:
        predict = model.predict(text)
        if (predict[0][0] == '__label__pos') and (predict[1][0] >= predictLimit):
            sys.stdout = sys.__stdout__
            print ("Good")
            sys.stdout = stdOutput
        elif (predict[0][0] == '__label__neg') and (predict[1][0] >= predictLimit):
            sys.stdout = sys.__stdout__
            print ("Bad" )
            sys.stdout = stdOutput
        else:
            sys.stdout = sys.__stdout__
            print (None)
            sys.stdout = stdOutput
    except:
        sys.stdout = sys.__stdout__
        print (None)
        sys.stdout = stdOutput
        print ("¯\_(ツ)_/¯ Unexpectable Error while emotion predicting!")  
        pass
    return