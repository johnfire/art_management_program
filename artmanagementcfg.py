#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 11:28:41 2019

@author: christopher
"""
dirlist = {"displate","mainphoto","society6","xcftype","pngtype","jpgtype","cr2type","info","oldcanon","oldCameraPics"}
galleryList = ["mysite","buzzart","deviant","saatchi","soc6"]

basicPathDir = "/home/christopher/Pictures/myPaintings"
workingDir = "/home/christopher/Pictures/myPaintings/finishedWorks-forSale7:30-09-09-19" # this is the path to the active directory
myworkingFolder = "/home/christopher/Pictures/myPaintings/finishedWorks-forSale7:30-09-09-19" #the name of the active painting directorysubDirList = []

#DO NOT CHANGE ANYTHING BELOW HERE FOR YOUR SET UP

currentCat = "" # this is always the active catagory
dispPainting = "" # this is always the active painting

totalSubs = 0 #total number of catagories
catIndex = 0  #index used to page thru catagories
totalPtngs = 0 #total number of paintings in data base after loading
ptngIndex = 0 #index used topage thru paintings
totalPtngsinlist = 0  # used to hold temp amount of paintings in a list locally

subDirPaths = []
paintingPaths = []
subDirList = []   #holds list of names of active subdirectories at load database time, only used in openData currently
listSubs = []  # used outside of openData to list catagories
paintingList = []
listPtngs = [] # current list of paintings used to display works in a catagory.

paintingDic = {}
#myData = {}
catDir = {} #master dictionary of everything loaded into the program from database. not currently used for anything important

mylibOfSubdirectories = {}
mylibListOfPaintings = {}
dirOfCatandPaintings = {} # dictionary of painting catagories and contents-- the paintings in each catagory
mylibOfSubPaintings = {}

gallery1 = galleryList[0]
gallery2 = galleryList[1]
gallery3 = galleryList[2]
gallery4 = galleryList[3]
gallery5 = galleryList[4]

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



