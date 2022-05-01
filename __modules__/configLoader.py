#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Config.json loader
"""
import os
from __modules__ import packagesInstaller
packages = ['json']
packagesInstaller.setup_packeges(packages)

import json

def dir_below():
    curFolder = os.path.abspath(os.getcwd()).replace(os.path.dirname(os.path.abspath(os.curdir)),"")
    dirBelow = os.path.abspath(os.curdir).replace(curFolder, "")
    return dirBelow

def default_value(configPath, key):
    try:
        with open(configPath+"/config.json", "r") as configFile:
            jsonConfig = json.load(configFile)
            value = float(jsonConfig[key])
            configFile.close()
    except:
        print ("¯\_(ツ)_/¯ Error! Value can't be reading! Please, check a key {0} in config.json".format(key))
        value = 0.9
        pass
    return value

def load_default_languages(configPath):
    try:
        with open(configPath+"/config.json", "r") as configFile:
            jsonConfig = json.load(configFile)
            try:
                langModels = {list(langModel.keys())[0] : langModel[list(langModel.keys())[0]]
                                for langModel in jsonConfig["langModels"]}
            except AttributeError:
                pass
            configFile.close()
    except:
        print ("¯\_(ツ)_/¯ Error! Default languages can't be reading! Please, check a field {0} in config.json".format("langModels"))
        langModels = {"uk":"uk.ftz", "ru":"ru.ftz", "en":"en.ftz"}
        pass
    return langModels
