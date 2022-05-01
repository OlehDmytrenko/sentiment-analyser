#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 12:52:08 2022

@author: dmytrenko.o
"""
import sys
stdOutput = open("outlog.log", "w")
sys.stderr = stdOutput
sys.stdout = stdOutput

from __modules__ import packagesInstaller
packages = ['os', 'fasttext']
packagesInstaller.setup_packeges(packages)

import os
import fasttext

def load_model_(modelsDir, model):
    try:
        print ("Loading <{0}.ftz> quantized model ...\n".format(model))
        print (os.path.join(modelsDir+'/models', model))
        model = fasttext.load_model((os.path.join(modelsDir+'/models', model)))
        print ("<{0}> quantized model successfully loaded!\n".format(model))
    except:
        print ("¯\_(ツ)_/¯ <{0}.ftz> quantized model can't be loaded!\n".format(model))
    return model
       
def load_models(modelsDir, langModels):
    models = dict()
    for lang in langModels.keys():
        models[lang] = load_model_(modelsDir,langModels[lang])
    return models