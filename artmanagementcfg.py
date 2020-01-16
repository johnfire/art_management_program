#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 11:28:41 2019

@author: christopher
"""
dirlist = {"displate","mainphoto","society6","xcftype","pngtype","jpgtype","cr2type","info","oldcanon","oldCameraPics"}
galleryList = ["mysite","buzzart","deviant","saatchi","soc6"]

basicPathDir = "/home/christopher/Pictures/myPaintings"
workingDir = '/home/christopher/Pictures/myPaintings/finishedWorks-forSale7:30-09-09-19' # this is the path to the active directory

#DO NOT CHANGE ANYTHING BELOW HERE FOR YOUR SET UP

myworkingFolder = "" #the name of the active painting directorysubDirList = []

subDirPaths = []
paintingPaths = []

paintingList = []
paintingDic = {}
myData = {}

catDir = {}
mylibListOfPaintings = {}
mylibOfSubdirectories = {}
dirOfCatandPaintings = {}
mylibOfSubPaintings = {}

gallery1 = galleryList[0]
gallery2 = galleryList[1]
gallery3 = galleryList[2]
gallery4 = galleryList[3]
gallery5 = galleryList[4]

listSubs = []
totalSubs = 0
catIndex = 1
currentCat = ""
listPtngs = []
totalPtngs = 0
ptngIndex = 0
dispPainting = ""

nameOfPaintingfile = "none"
nameOfCatagory = "none"
nameOfPainting = "none"
datePainted = "none"
wherePainted = "none"
idnum = "0"
secid = "0"
Dims = "none"
hDims = "none"
materialsUsed = "none"
description = "none"
gallery1Val = "0" 
gallery2Val = "0"
gallery3Val = "0"
gallery4Val = "0"
gallery5Val = "0"



