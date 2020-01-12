#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 11:28:41 2019

@author: christopher
"""

basicPathDir = "/home/christopher/Pictures/myPaintings"
workingDir = "" # this is the path to the active directory
myworkingFolder = "" #the name of the active painting directorysubDirList = []

subDirPaths = []

paintingList = []
paintingPaths = []

paintingDic = {}
myData = {}

dirlist = {"displate","mainphoto","society6","xcftype","pngtype","jpgtype","cr2type","info","oldcanon","oldCameraPics"}

catDir = {}
mylibListOfPaintings = {}
mylibOfSubdirectories = {}
dirOfCatandPaintings = {}
mylibOfSubPaintings = {}

jsonData = {}
json1Data = {}

gallery1 = "mysite"
gallery2 = "buzzart"
gallery3 = "deviant"
gallery4 = "saatchi"
gallery5 = "soc6"

nameOfPaintingfile = "none"
nameOfCatagory = "none"

nameOfPainting = "none"
datePainted = "none"
wherePainted = "none"
idnum = 0
secid = 0
Dims = "none"
hDims = "none"
materialsUsed = "none"
description = "none"
gallery1Val = 0 
gallery2Val = 0
gallery3Val = 0
gallery4Val = 0
gallery5Val = 0

listSubs = []
totalSubs = 0
catIndex = 1
currentCat = ""
listPtngs = []
totalPtngs = 0
ptngIndex = 0
dispPainting = ""

