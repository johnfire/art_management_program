#!/home/christopher/anaconda3/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 11:24:43 2019

this is the main foto management proram.
@author: christopher rehm

note this program uses the wxPython and wxWidgets for GUI development,
both must be installed for usage of the GUI

things to do:

2. creat new subfolders in all painting folders --NOT TESTED
3. rename all cr2 and jpg files by the name of the painting and a number. a date?
4. organize all the info sheets in one folder so that you can collate them easily

"""

import os
import pprint
import wx 
#import sys
import shutil

basicPathDir = "/home/christopher/Pictures/myPaintings"
workingDir = "" # this is the path to the active directory

subDirList = []
paintingList = []
subDirPaths = []
paintingPaths= []
paintingDic = {}

myworkingFolder ="" #the name of the active painting directory
answer = "2"  # 1 is the terminal version 2 is the gui version

dirlist = {"displate","mainphoto","society6","xcftype","pngtype","jpgtype","cr2type","info","oldcanon","oldCameraPics"}

##################################################################################

##################################################################################

##################################################################################
    
def addNewSubfolder(newSubFolder = "test"):
    os.chdir(workingDir)
    for each in os.getcwd():
        os.chdir(workingDir + "/" + each)
        for each1 in os.getcwd():
            os.chdir(workingDir + "/" + each + "/" + each1)
            os.mkdir(newSubFolder)  
        ### need reflective code here to add to basic dir list. 
    print("Task Completed\n")
     
##################################################################################
     
def makeList():
    global workingDir
    os.chdir("./info") #enter info dir, where we keep all info files
    if "./finishedPaintings.txt" == None:
        os.remove("./finishedPaintings.txt")
    fh = open("./finishedPaintings.txt", "w+")
    
    mylist ={}
    print("in the make list function")
    print(workingDir)
    print("did the working dir print?")
    mylist["all"] = searchLevel(workingDir)
    for k, v in mylist.items():
        #dicname = str(k)
        fh.write(str(k) + ' >>>\n')
        print(k)
        #pp.pprint("....." + str(v))
        for k1, v1 in v.items():
            #dic1name = str(k1)
            fh.write("..." + str(k1) + ' >>>\n')
            try:
                for k2, v2 in v1.items():
                    fh.write("......" + str(k2) +'>>>\n')
#                    try:
#                        for k3, v3 in v2.items():
#                            #fh.write("...**--" + str(k3) + ' >>> '+ str(v3) + ' >>>\n ')
#                            fh.write("...**--" + str(k3) + ' >>> \n')
#                    except:
#                        fh.write("\n")
##                        try:
##                            for k4, v4 in v3.items():
##                                fh.write("...**-->" + str(k4) + ' >>> '+ str(v4) + ' >>>\n ')
##                        except:
##                            fh.write("\n")
            except:
                fh.write("\n")
    #pp = pprint.PrettyPrinter(indent=4)
    #pp.pprint(mylist)
    fh.close()
    os.chdir("..")
        
##################################################################################

def createAllSubfolders():
    ##homedir = "/home/christopher/Pictures/myPaintings/finishedWorks _forSale"
    #dirlist = {"displate","mainphoto","society6","xcftype","pngtype","jpgtype","cr2type","info","oldcanon","oldCameraPics"}
    os.chdir(workingDir)
    
    print(os.getcwd())
    
    mylist= os.listdir()
    
    for each in mylist:
        chkdir = workingDir + "/" + str(each)
        print(str(each))
        if os.path.isdir(each) is True:
            os.chdir(chkdir)
            mylist1= os.listdir()
            for each1 in mylist1:
                chkdir1 = chkdir + "/" + str(each1)
                if os.path.isdir(each1) is True:
                    os.chdir(chkdir1)
                    print(str(os.getcwd()+"\n"))
                    
                    for every in dirlist:   
                        newdir = chkdir + "/" + str(each1) + "/" + str(every)
                        print(newdir)
                        #q = input("does it look right")
                        if os.path.isdir(newdir) is False:
                            os.mkdir(newdir)
                        
                        print(str(os.getcwd()+ "\n"))
                    os.chdir("..")
                    print(str(os.getcwd()+ "\n"))
            os.chdir("..")
            print(str(os.getcwd()+ "\n"))
    
##################################################################################
    
def moveAllPhotos():
   for each in paintingPaths:
       os.chdir(each)
       listOfFilesToMove = os.listdir(".")
       for each in listOfFilesToMove:
           if each.endswith(".CR2"):
               shutil.move("./"+each, "./cr2type/"+ each)
           elif each.endswith(".JPG"):
               shutil.move("./"+each, "./jpgtype/"+ each)
           elif each.endswith(".jpg"):
               shutil.move("./"+each, "./oldCamerPics/"+ each)
           else:
               pass
    
#######################################################
    
def collateAll():
    pass

##################################################################################
def renameFotos():
    pass
    
    #if oldName.startswith("IMG") or oldName.startswith("DSC"):
        
    #    newName = paintingName + todayDate + index 
   
##################################################################################
    
#### recursion search function #####
def searchLevel(myLevel):
    tableofitems ={}
    print(str(os.getcwd()))
    print(myLevel)
    thisdirlist = os.listdir(myLevel)
    print(thisdirlist)
    countoffiles = 1
    for each in thisdirlist:
        if os.path.isdir(myLevel +"/" + each) is True:
            mynewlevel = myLevel +"/" + each 
            tableofitems[each] = searchLevel(mynewlevel)
        else:
            tableofitems[countoffiles] = each
            countoffiles +=1
    return tableofitems

##################################################################################
##################################################################################
#GUI APP 
   
class mainMenu(wx.Frame):
    global workingDir

    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'Menus', size=(800, 400))
        menuBar = wx.MenuBar()
        menu1 = wx.Menu()
        menu2 = wx.Menu()
        menu3 = wx.Menu()
        menu4 = wx.Menu()
        menuItemLoad = menu1.Append(-1, "&Load dir")
        menuItemClose = menu1.Append(-1, "&Close dir")
        menuItemExit = menu1.Append(-1, "&Exit...")
        
        menuItemNewPainting = menu2.Append(-1,"&New Painting")
        menuItemNewSubfolder = menu2.Append(-1,"Create New Subfolder")
        menuItemMakeListAll = menu2.Append(-1, "List all works")
        menuItemCreateAllSubfolders = menu2.Append(-1,"Make All Subfolders")
        menuItemMoveFotosToFolders = menu2.Append(-1, "Move Fotos to Subfolders")
        menuItemColate = menu2.Append(-1, "Collate all Info Sheets")
        menuItemRenameAll = menu2.Append(-1, "Rename All Fotos")
        #menuItemBlank = menu2.Append(-1, "Blank, future use")
        
        menuItemDisplayWork = menu3.Append(-1, "Display a Work")
        menuItemDisplayAll = menu3.Append(-1, "Display All Works")
        
        menuItemHelp = menu4.Append(-1,"Help")
        menuItemPref = menu4.Append(-1, "Preferences")
        menuItemAbout = menu4.Append(-1, "&About me")
        
        menuBar.Append(menu1, "&File")
        menuBar.Append(menu2, "&Actions")
        menuBar.Append(menu3, "&Display")
        menuBar.Append(menu4, "&Info")
        
        panel = wx.Panel(self)
        button = wx.Button(panel, label="End Program", pos=(100, 320),size=(400,50))
        
        self.SetMenuBar(menuBar)
        self.CreateStatusBar()
        self.SetStatusText("Welcome to art business management")
        
        self.Bind(wx.EVT_BUTTON, self.OnCloseMe, button)
        
        self.Bind(wx.EVT_MENU, self.OpenFile, menuItemLoad)
        self.Bind(wx.EVT_MENU, self.CloseFile, menuItemClose)
        self.Bind(wx.EVT_MENU, self.OnCloseMe, menuItemExit)
        
        self.Bind(wx.EVT_MENU, self.NewPainting, menuItemNewPainting)
        self.Bind(wx.EVT_MENU, self.AddNewSubFolder, menuItemNewSubfolder)
        self.Bind(wx.EVT_MENU, self.MakeListAllWorks, menuItemMakeListAll)
        self.Bind(wx.EVT_MENU, self.CreateAllSubfolders, menuItemCreateAllSubfolders)
        self.Bind(wx.EVT_MENU, self.MoveFotosToFolders, menuItemMoveFotosToFolders)
        self.Bind(wx.EVT_MENU, self.ColateAllInfoSheets, menuItemColate)
        self.Bind(wx.EVT_MENU, self.RenameAllFotosPicDateNum, menuItemRenameAll)
        
        self.Bind(wx.EVT_MENU, self.DisplayWork, menuItemDisplayWork)
        self.Bind(wx.EVT_MENU, self.DisplayAll, menuItemDisplayAll)
        
        self.Bind(wx.EVT_MENU, self.GetHelp, menuItemHelp)
        self.Bind(wx.EVT_MENU, self.SetPreferences, menuItemPref)
        self.Bind(wx.EVT_MENU, self.OnAbout, menuItemAbout)
    
    #here are the actions for above code from menu
    
    #SHOULD BE WORKING
    def OpenFile(self,event):
        
        global workingDir
        global subDirList
        global paintingList
        global subDirPaths
        global paintingPaths
        global paintingDic
        
        listOfPaintings = []
        self.SetStatusText("Opens the database")
        dialog = wx.DirDialog(None, "Choose a directory to work with: ", style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
        if dialog.ShowModal() == wx.ID_OK:
            #print(dialog.GetPath())
            workingDir = str(dialog.GetPath())
            os.chdir(str(dialog.GetPath()))
        dialog.Destroy()
        subDirList = os.listdir(workingDir)
        subDirList.remove("info")
        #print(subDirList)
        for each in subDirList:
            listOfPaintings =[]
            #print(each)
            #print(workingDir + "/" + each)
            if True == os.path.isdir(workingDir + "/" + each):
                subDirPaths.append(workingDir + "/" + each)
                os.chdir(workingDir + "/" + each)
                listOfPaintings = os.listdir(os.getcwd())
                for eachone in listOfPaintings:
                    paintingList.append(eachone)
                    paintingPaths.append(workingDir + "/" + each + "/" + eachone)
                    paintingDic[eachone] = workingDir + "/" + each + "/" + eachone
#        pp = pprint.PrettyPrinter(width=41, compact=True)        
#        pp.pprint(subDirList)
#        print("\n")
#        pp.pprint(subDirPaths)
#        print("\n")
#        pp.pprint(paintingList)
#        print("\n")
#        pp.pprint(paintingPaths)
#        pp.pprint(paintingDic)
        
        
    def CloseFile(self,event):
        self.SetStatusText("Closes the database")
        wx.MessageBox("This closes the file ",
                      "fileloader", wx.OK | wx.ICON_INFORMATION, self)
        
    def OnAbout(self, event):
        self.SetStatusText("About me")
        wx.MessageBox("This program manages all the art stuff inn the computer",
                      "About Art Biz Manager", wx.OK | wx.ICON_INFORMATION, self)
        
    def OnCloseMe(self, event):
        self.Close() 
    
    def OnQuit(self, event):
        self.Close()  
    
    #SHOULD BE WORKING
    def NewPainting(self, event): #SHOULD BE WORKING
        
        self.SetStatusText("Create a New Painting")
        dialog = wx.DirDialog(None, "Choose a directory for your painting: ", style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
        if dialog.ShowModal() == wx.ID_OK:
            print(dialog.GetPath())
            os.chdir(str(dialog.GetPath()))
        dialog.Destroy()
        
        dlg = wx.TextEntryDialog(None, "What is the new painting named",'Name of new painting', 'new painting')
        if dlg.ShowModal() == wx.ID_OK:
            response = dlg.GetValue()
            os.mkdir("./" + response)
            os.chdir("./" + response)
            for each in dirlist:
                os.mkdir("./" + each)   
                
    #SHOULD BE WORKING
    def AddNewSubFolder(self, event):
        self.SetStatusText("Add a Subfolder to all Paintings")
        dlg = wx.TextEntryDialog(None, "What is the new folder named",'Name of new folder', 'new folder')
        if dlg.ShowModal() == wx.ID_OK:
            response = dlg.GetValue()
            addNewSubfolder(response)
            
    #SHOULD BE WORKING        
    def MakeListAllWorks(self, event):
        self.SetStatusText("Make a list of all works")
        makeList()
        
        
    def CreateAllSubfolders(self, event):
        self.SetStatusText("Create all subfolders, not normally used")
        createAllSubfolders()
        
    #Should be working not tested yet
    def MoveFotosToFolders(self, event):
        self.SetStatusText("Move fotos to correct picture folders")
        moveAllPhotos()
        
    #these should be the next functions to work on. 
    def ColateAllInfoSheets(self,event):
        self.SetStatusText("Collate all info sheets in one folder")
        for each in paintingPaths:
            os.chdir(each + "/info")
            for eachone in os.listdir():
                if eachone.endswith(".odt"):
                    shutil.copy(eachone, workingDir + "/info/odtfiles")
                elif eachone.endswith("lr.pdf"):
                    shutil.copy(eachone, workingDir + "/info/lrpdffiles")
                else:
                    shutil.copy(eachone,workingDir + "/info/pdffiles")
    
    def RenameAllFotosPicDateNum(self, event):
        self.SetStatusText("Rename all fotos to name date index")
        renameFotos()
    
    def DisplayWork(self,event):
        self.SetStatusText("Display a work")
        pass
    
    def DisplayAll(self, event):
        mybuttons = []
        self.SetStatusText("Display all works")
#        for each in paintingDic:
#            mybutton(each) = wx.Button(panel, label=each, pos=(100, 320),size=(400,50))
#            
#        
#        pass
        
    def GetHelp(self, event):
        self.SetStatusText("Help")
        pass
    
    def SetPreferences(self, event):
        self.SetStatusText("Set up preferences")
        pass
        
##################################################################################
    
class App(wx.App):
    
    def OnInit(self):
         self.frame = mainMenu(parent=None, id = -1)
         self.frame.Show()
         self.SetTopWindow(self.frame)
         #self.frame.OpenFile()
         return True
##################################################################################
##################################################################################

answer = 2
app = App()
app.MainLoop()
print("Ending program.")
        
##################################################################################