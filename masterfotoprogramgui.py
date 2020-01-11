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
#import sys
import os
import wx 
import shutil
import json
import artmanagementcfg as cfg

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
catIndex = 1
currentCat = ""
listPtngs = []
ptngIndex = 0
dispPainting = ""
totalSubs = 0
totalPtngs = 0

##################################################################################
     
def makeList():
    #this function makes a list of all paintings in the file of works
    os.chdir(cfg.basicPathDir)
    os.chdir("./info") #enter info dir, where we keep all info files
    
    if "./finishedPaintings.txt" != None:
        os.remove("./finishedPaintings.txt")
    fh = open("./finishedPaintings.txt", "w+")
    
    mylist ={}
    mylist["all"] = searchLevel(cfg.workingDir)
    for k, v in mylist.items():
        fh.write(str(k) + ' >>>\n')
        #print(k)
        for k1, v1 in v.items():
            fh.write("..." + str(k1) + ' >>>\n')
            try:
                for k2, v2 in v1.items():
                    fh.write("......" + str(k2) +'>>>\n')
            except:
                fh.write("\n")
    fh.close()
    os.chdir("..")   
##################################################################################

def createAllSubfolders():
    ##homedir = "/home/christopher/Pictures/myPaintings/finishedWorks _forSale"
    #dirlist = {"displate","mainphoto","society6","xcftype","pngtype","jpgtype","cr2type","info","oldcanon","oldCameraPics"}
    os.chdir(cfg.workingDir)
   # print(os.getcwd()) 
    mylist= os.listdir()
    for each in mylist:
        chkdir = cfg.workingDir + "/" + str(each)
        #print(str(each))
        if os.path.isdir(each) is True:
            os.chdir(chkdir)
            mylist1= os.listdir()
            for each1 in mylist1:
                chkdir1 = chkdir + "/" + str(each1)
                if os.path.isdir(each1) is True:
                    os.chdir(chkdir1)
                    #print(str(os.getcwd()+"\n"))
                    for every in cfg.dirlist:   
                        newdir = chkdir + "/" + str(each1) + "/" + str(every)
                        #print(newdir)
                        #q = input("does it look right")
                        if os.path.isdir(newdir) is False:
                            os.mkdir(newdir)
                        #print(str(os.getcwd()+ "\n"))
                    os.chdir("..")
                    #print(str(os.getcwd()+ "\n"))
            os.chdir("..")
            #print(str(os.getcwd()+ "\n"))  
##################################################################################
    
def moveAllPhotos():
   for each in cfg.paintingPaths:
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
##################################################################################
def renameFotos():
    pass
    
    #if oldName.startswith("IMG") or oldName.startswith("DSC"):
    #    newName = paintingName + todayDate + index 
##################################################################################
#### recursion search function #####
def searchLevel(myLevel):
    tableofitems ={}
    #print(str(os.getcwd()))
    #print(myLevel)
    thisdirlist = os.listdir(myLevel)
    #print(thisdirlist)
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
    
    def __init__(self, parent, id):

        wx.Frame.__init__(self, parent, id, 'Menus', size=(1200, 800))

        panel = wx.Panel(self, wx.ID_ANY)
        panel.SetBackgroundColour("blue")
        
        hboxMain =wx.BoxSizer(wx.HORIZONTAL)
        
        vboxBig = wx.BoxSizer(wx.VERTICAL)
        
        vbox1 = wx.BoxSizer(wx.VERTICAL)
       
        hbox0 = wx.BoxSizer(wx.HORIZONTAL)
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        hbox1a = wx.BoxSizer(wx.HORIZONTAL)
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        hbox4 = wx.BoxSizer(wx.HORIZONTAL)
        hbox5 = wx.BoxSizer(wx.HORIZONTAL)
        hbox6 = wx.BoxSizer(wx.HORIZONTAL)
        hbox7 = wx.BoxSizer(wx.HORIZONTAL)
       
        vbox2 = wx.BoxSizer(wx.VERTICAL)
        
        hboxr1 =wx.BoxSizer(wx.HORIZONTAL)
        hboxr2 = wx.BoxSizer(wx.HORIZONTAL)
 
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
    
        menuItemMakeListAll = menu3.Append(-1, "List all works")
        menuItemCreateAllSubfolders = menu3.Append(-1,"Make All Subfolders")
        menuItemMoveFotosToFolders = menu3.Append(-1, "Move Fotos to Subfolders")
        menuItemColate = menu3.Append(-1, "Collate all Info Sheets")
        menuItemRenameAll = menu3.Append(-1, "Rename All Fotos")

        menuItemHelp = menu4.Append(-1,"Help")
        menuItemPref = menu4.Append(-1, "Preferences")
        menuItemAbout = menu4.Append(-1, "&About me")
    
        menuBar.Append(menu1, "&File")
        menuBar.Append(menu2, "&Common Actions")
        menuBar.Append(menu3, "&Other Actions")
        menuBar.Append(menu4, "&Info")
    
        self.SetMenuBar(menuBar)
        self.CreateStatusBar()
        self.SetStatusText("Welcome to art business management")
    
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
    
        self.Bind(wx.EVT_MENU, self.GetHelp, menuItemHelp)
        self.Bind(wx.EVT_MENU, self.SetPreferences, menuItemPref)
        self.Bind(wx.EVT_MENU, self.OnAbout, menuItemAbout)
    
        workName ="Name of work"
        catName = "Current Catagory"
    
        self.b1 = wx.Button(panel, label = 'previous work') 
        hbox0.Add(self.b1, 1, wx.ALIGN_LEFT|wx.ALL,5)
    
        self.labelA = wx.StaticText(panel, -1, workName , style = wx.TE_CENTER)
        hbox0.Add(self.labelA, 1, wx.EXPAND|wx.ALIGN_CENTER|wx.ALL,5)
    
        self.b2 = wx.Button(panel, label = 'next work') 
        hbox0.Add(self.b2, 1, wx.ALIGN_LEFT|wx.ALL,5)
    
        self.b3 = wx.Button(panel, label = 'previous catagory') 
        hbox0.Add(self.b3, 1, wx.ALIGN_LEFT|wx.ALL,5)
    
        self.labelB = wx.StaticText(panel, -1, catName ,style = wx.TE_CENTER)
        hbox0.Add(self.labelB, 1, wx.EXPAND|wx.ALIGN_CENTER|wx.ALL,5)
    
        self.b4 = wx.Button(panel, label = 'next catagory') 
        hbox0.Add(self.b4, 1, wx.ALIGN_LEFT|wx.ALL,5)
    
        self.b5 = wx.Button(panel, label = 'EXIT PROGRAM') 
        hbox0.Add(self.b5, 1, wx.ALIGN_RIGHT|wx.ALL,5)
    
        self.b5.Bind(wx.EVT_BUTTON, self.OnQuit)  
        self.b1.Bind(wx.EVT_BUTTON, self.PrevPainting)
        self.b2.Bind(wx.EVT_BUTTON, self.NextPainting)
        self.b3.Bind(wx.EVT_BUTTON, self.PrevCat)
        self.b4.Bind(wx.EVT_BUTTON, self.NextCat)
    
        label1 = wx.StaticText(panel, -1, "Name of work")
        hbox1.Add(label1, 1, wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)
        
        self.t1 = wx.TextCtrl(panel,-1,size=(350,40))
        hbox1.Add(self.t1,1,wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)
    
        label2 = wx.StaticText(panel, -1, "Date painted")
        hbox2.Add(label2, 1, wx.ALIGN_LEFT|wx.ALL,5)
    
        self.t2 = wx.TextCtrl(panel,-1,size=(100,40))
        hbox2.Add(self.t2,1,wx.ALIGN_LEFT|wx.ALL,5)
        
        label2a = wx.StaticText(panel, -1, "id number")
        hbox2.Add(label2a, 1, wx.ALIGN_LEFT|wx.ALL,5)
    
        self.t2a = wx.TextCtrl(panel,-1,size=(50,40))
        hbox2.Add(self.t2a,1,wx.ALIGN_LEFT|wx.ALL,5)
        
        label2b = wx.StaticText(panel, -1, "count/year")
        hbox2.Add(label2b, 1, wx.ALIGN_LEFT|wx.ALL,5)
    
        self.t2b = wx.TextCtrl(panel,-1,size=(50,40))
        hbox2.Add(self.t2b,1,wx.ALIGN_LEFT|wx.ALL,5)
    
        label3 = wx.StaticText(panel, -1, "Where painted")
        hbox3.Add(label3, 1, wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)
        
        self.t3 = wx.TextCtrl(panel,-1,size=(350,40))
        hbox3.Add(self.t3,1,wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)
    
        label4 = wx.StaticText(panel, -1, "Vertical dim")
        hbox4.Add(label4, 1, wx.ALIGN_LEFT|wx.ALL,5)
        
        self.t4 = wx.TextCtrl(panel,-1,size=(50,40))
        hbox4.Add(self.t4,1,wx.ALIGN_LEFT|wx.ALL,5)
        
        label5 = wx.StaticText(panel, -1, "Horizontal dim")
        hbox4.Add(label5, 1, wx.ALIGN_LEFT|wx.ALL,5)
        
        self.t5 = wx.TextCtrl(panel,-1,size=(50,40))
        hbox4.Add(self.t5,1,wx.ALIGN_LEFT|wx.ALL,5)
    
        label10 = wx.StaticText(panel, -1, gallery1)
        hbox5.Add(label10, 1, wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)
        
        self.t10 = wx.TextCtrl(panel,-1,size=(50,40))
        hbox5.Add(self.t10,1,wx.ALIGN_LEFT|wx.ALL,5)
        
        label11 = wx.StaticText(panel, -1, gallery2)
        hbox5.Add(label11, 1, wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)
        
        self.t11 = wx.TextCtrl(panel,-1,size=(50,40))
        hbox5.Add(self.t11,1,wx.ALIGN_LEFT|wx.ALL,5)
        
        label12 = wx.StaticText(panel, -1, gallery3)
        hbox5.Add(label12, 1, wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)
        
        self.t12 = wx.TextCtrl(panel,-1,size=(50,40))
        hbox5.Add(self.t12,1,wx.ALIGN_LEFT|wx.ALL,5)
        
        label13 = wx.StaticText(panel, -1, gallery4)
        hbox5.Add(label13, 1, wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)
        
        self.t13 = wx.TextCtrl(panel,-1,size=(50,40))
        hbox5.Add(self.t13,1,wx.ALIGN_LEFT|wx.ALL,5)
        
        label14 = wx.StaticText(panel, -1, gallery5)
        hbox5.Add(label14, 1, wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)
        
        self.t14 = wx.TextCtrl(panel,-1,size=(50,40))
        hbox5.Add(self.t14,1,wx.ALIGN_LEFT|wx.ALL,5)
       
        label6 = wx.StaticText(panel, -1, "Materials used")
        hbox6.Add(label6, 1, wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)
    
        label7 = wx.StaticText(panel, -1, "Description")
        hbox7.Add(label7, 1, wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)
    
        self.t6 = wx.TextCtrl(panel,-1,size=(350,80),style = wx.TE_MULTILINE)
        hbox6.Add(self.t6,1,wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)
    
        self.t7 = wx.TextCtrl(panel,-1,size=(350,160),style = wx.TE_MULTILINE)
        hbox7.Add(self.t7,1,wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)
        
        self.savebtn = wx.Button(panel, label = "save painting data")
        hboxr2.Add(self.savebtn,1,wx.ALIGN_CENTER|wx.ALIGN_BOTTOM|wx.ALL, 5)
        self.savebtn.Bind(wx.EVT_BUTTON, self.onSavePainting)   
    
        vbox1.Add(hbox1)
        vbox1.Add(hbox1a)
        vbox1.Add(hbox2) 
        vbox1.Add(hbox3)
        vbox1.Add(hbox4)
        vbox1.Add(hbox5)
        vbox1.Add(hbox6)
        vbox1.Add(hbox7)
        
        vbox2.Add(hboxr1)
        vbox2.Add(hboxr2)

        hboxMain.Add(vbox1)
        hboxMain.Add(vbox2)
        
        vboxBig.Add(hbox0)
        vboxBig.Add(hboxMain)
    
        panel.SetSizer(vboxBig)
        panel.Center()
        panel.Show()
        panel.Fit()
        
        self.labelA.SetLabel(nameOfPaintingfile)
        self.labelB.SetLabel(nameOfCatagory)
        
        self.t1.SetValue(nameOfPainting)
        self.t2.SetValue(datePainted)
        self.t2a.SetValue(str(idnum))
        self.t2b.SetValue(str(secid))
        self.t3.SetValue(wherePainted)
        self.t4.SetValue(Dims)
        self.t5.SetValue(hDims)
        self.t6.SetValue(materialsUsed)
        self.t7.SetValue(description)
        self.t10.SetValue(str(gallery1Val))
        self.t11.SetValue(str(gallery2Val))
        self.t12.SetValue(str(gallery3Val))
        self.t13.SetValue(str(gallery4Val))
        self.t14.SetValue(str(gallery5Val))
        
    #here are the actions for above code for the menu
    
    #SHOULD BE WORKING
    def OpenFile(self,event):
        
        global catDir
        global mylibListOfPaintings
        global mylibOfSubdirectories
        global dirOfCatandPaintings
        global mylibOfSubPaintings
        
        global jsonData 
        global json1Data
        
        global gallery1
        global gallery2
        global gallery3
        global gallery4
        global gallery5
        
        global nameOfPaintingfile 
        global nameOfCatagory
        global nameOfPainting
        global datePainted
        global wherePainted
        global vertDim
        global horizDim
        global materialsUsed
        global description
        
        global listSubs
        global currentCat
        global listPtngs
        global dispPainting
        global totalSubs
        global totalPtngs
        
        self.SetStatusText("Opens the database")
        
        dialog = wx.DirDialog(None, "Choose a directory to work with: ", style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
        if dialog.ShowModal() == wx.ID_OK:
            cfg.workingDir = str(dialog.GetPath())
            os.chdir(str(dialog.GetPath()))
        dialog.Destroy()
        
        cfg.subDirList = os.listdir(cfg.workingDir)
        cfg.subDirList.remove("info")
        
        for each in cfg.subDirList:
            listOfPaintings = {}
            if True == os.path.isdir(cfg.workingDir + "/" + each):
                cfg.subDirPaths.append(cfg.workingDir + "/" + each)
                os.chdir(cfg.workingDir + "/" + each)
                thePaintings = os.listdir(os.getcwd())
                print(thePaintings)
                dirOfCatandPaintings[each] = thePaintings
                for eacheins in thePaintings:
                    os.chdir(cfg.workingDir + "/" + each + "/" + eacheins + "/info")
                    for theFile in os.listdir("."):
                        if theFile.endswith(".json"):
                            with open(theFile, "r") as content:
                                datastuff = json.load(content)
                                print(datastuff)
                                listOfPaintings[eacheins]= datastuff
                    os.chdir("..")
                    os.chdir("..")

                catDir[each] =listOfPaintings

        mylibListOfPaintings = {"list_of_paintings" : cfg.paintingList }
        mylibOfSubdirectories = {"list_of_subdirectories" : cfg.subDirList}
        mylibOfSubPaintings = {"list_of_cat_and_paintings": dirOfCatandPaintings}
        
        jsonData = json.dumps(mylibOfSubdirectories, sort_keys=True,  indent=4, separators=(",", ": "))
        json1Data = json.dumps(mylibOfSubPaintings, sort_keys=True,  indent=4, separators=(",", ": "))
        json2Data = json.dumps(catDir, sort_keys=True,  indent=4, separators=(",", ": "))
        json3Data = json.dumps(cfg.workingDir, sort_keys=True,  indent=4, separators=(",", ": "))

        print("\n")
        print(os.getcwd())
        
        os.chdir(cfg.workingDir + "/" + "info")
        filename = "libOfSubdirs.json"
        with open(filename, 'w') as f:
             f.write(jsonData)
        file2name = "libOfSubsandPaintngs.json"
        with open(file2name, 'w') as f:
             f.write(json1Data)  
        file3name = "alljsondatagrams.json"
        with open(file3name, 'w') as f:
             f.write(json2Data)
        file4name = "fliepathmainfolder.json"
        with open(file4name, 'w') as f:
             f.write(json3Data)
             
        #now load correct stuff to screen.
        
        listSubs = mylibOfSubdirectories["list_of_subdirectories"]
        totalSubs = len(listSubs)
        
        currentCat = listSubs[1]
        
        listPtngs = mylibOfSubPaintings["list_of_cat_and_paintings"][currentCat]
        totalPtngs = len(listPtngs)
              
        dispPainting = listPtngs[0]
        
        ptgName = catDir[currentCat][dispPainting][dispPainting]["pname"]
        ptgDesc = catDir[currentCat][dispPainting][dispPainting]["desc"]
        ptgDate = catDir[currentCat][dispPainting][dispPainting]["year"]
        ptgNum = catDir[currentCat][dispPainting][dispPainting]["number"]
        saatchi= catDir[currentCat][dispPainting][dispPainting]["saatchi"]
        s6 = catDir[currentCat][dispPainting][dispPainting]["soc6"]
        try : 
            mysite = catDir[currentCat][dispPainting][dispPainting]["mysite"]
        except:
            mysite = 0
            pass
        try : 
            secid = catDir[currentCat][dispPainting][dispPainting]["secid"]
        except:
            secid = 0
            pass
        displate = catDir[currentCat][dispPainting][dispPainting]["displate"]
        dev = catDir[currentCat][dispPainting][dispPainting]["deviant"]
        buzz= catDir[currentCat][dispPainting][dispPainting]["buzz"]
        dims= catDir[currentCat][dispPainting][dispPainting]["dims"]
        try:
            hdims = catDir[currentCat][dispPainting][dispPainting]["hdims"]
        except:
            hdims = "none"
            pass
        try:
            mat = catDir[currentCat][dispPainting][dispPainting]["materialsUsed"]
        except:
            mat = "none"
            pass
        
        self.labelA.SetLabel(dispPainting)
        self.labelB.SetLabel(currentCat)
        
        self.t1.SetValue(ptgName)
        self.t2.SetValue(str(ptgDate))
        self.t2a.SetValue(str(ptgNum))
        self.t2b.SetValue(str(secid))
        self.t3.SetValue(wherePainted)
        self.t4.SetValue(dims)
        self.t5.SetValue(hdims)
        
        self.t6.SetValue(materialsUsed)
        self.t7.SetValue(ptgDesc)
        self.t10.SetValue(saatchi)
        self.t11.SetValue(dev)
        self.t12.SetValue(s6)
        self.t13.SetValue(buzz)
        self.t14.SetValue(str(mysite))
            
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
            mylocation=os.getcwd()
        dialog.Destroy()
        dlg = wx.TextEntryDialog(None, "What is the new painting named",'Name of new painting', 'new painting')
        if dlg.ShowModal() == wx.ID_OK:
            response = dlg.GetValue()
            os.mkdir("./" + response)
            os.chdir("./" + response)
            for each in cfg.dirlist:
                os.mkdir("./" + each) 
            os.chdir("info")
            print("\n")
            print("\n")
            print(os.getcwd())
            print("\n")
            print("\n")
            print(cfg.workingDir)
            print("\n")
            shutil.copyfile(cfg.workingDir + "/info/placeholder.json","./"+response+".json" )
                
    #SHOULD BE WORKING
    def AddNewSubFolder(self, event):
        self.SetStatusText("Add a new catagory to database")
        dlg = wx.TextEntryDialog(None, "What is the new catagory named",'Name of new folder', 'new folder')
        if dlg.ShowModal() == wx.ID_OK:
            response = dlg.GetValue()
            os.chdir(cfg.workingDir)
            for each in os.getcwd():
                os.chdir(cfg.workingDir + "/" + each)
                for each1 in os.getcwd():
                    os.chdir(cfg.workingDir + "/" + each + "/" + each1)
                    os.mkdir(response)  

    def onSavePainting(self,event):
        #global cfg.workingDir
        global currentCat
        global dispPainting
        
        self.SetStatusText("saving painting data to json file")
        
        ptgname =self.t1.GetValue()
        ptgDate =self.t2.GetValue()
        numb = self.t2a.GetValue()
        secid =self.t2b.GetValue()
        wherePainted = self.t3.GetValue()
        vertDim = self.t4.GetValue()
        horizDim = self.t5.GetValue()
        materialsUsed = self.t6.GetValue()
        ptgDesc = self.t7.GetValue()
        gal1 = self.t10.GetValue()
        gal2 =self.t11.GetValue()
        gal3 =self.t12.GetValue()
        gal4 =self.t13.GetValue()
        gal5 =self.t14.GetValue()
               
        mydata = {dispPainting:{"pname": ptgname,"wherepainted":wherePainted,"secid":secid, "mysite":gal1,"buzz":gal2,"deviant":gal3,"saatchi":gal4,"soc6":gal5,"number": numb,"secid":secid, "year" : ptgDate, "dims": vertDim, "hdims": horizDim, "desc" : ptgDesc, "materials": materialsUsed}}
        jsonData = json.dumps(mydata, sort_keys=True,  indent=4, separators=(",", ": "))
        os.chdir(cfg.workingDir + "/" + currentCat + "/"+ dispPainting +  "/info") 
        filename = dispPainting + ".json"
        with open(filename, 'w') as f:
             f.write(jsonData)

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
        
    #works
    def ColateAllInfoSheets(self,event):
        self.SetStatusText("Collate all info sheets in one folder")
        for each in cfg.paintingPaths:
            os.chdir(each + "/info")
            for eachone in os.listdir():
                if eachone.endswith(".odt"):
                    shutil.copy(eachone, cfg.workingDir + "/info/odtFiles/")
                elif eachone.endswith("lr.pdf"):
                    shutil.copy(eachone, cfg.workingDir + "/info/lrpdfFiles/")
                else:
                    shutil.copy(eachone, cfg.workingDir + "/info/pdfFiles/")
    
    def RenameAllFotosPicDateNum(self, event):
        self.SetStatusText("Rename all fotos to name date index")
        renameFotos()
    
    def DisplayWork(self,event):
        self.SetStatusText("Display a work")
        pass
    
    def GetHelp(self, event):
        self.SetStatusText("Help")
        pass
    
    def SetPreferences(self, event):
        self.SetStatusText("Set up preferences")
        pass
    
    def PrevPainting(self,event):
        global listSubs
        global currentCat
        global listPtngs
        global dispPainting 
        global catIndex
        global ptngIndex
        global totalSubs
        global totalPtngs
        
        global mylibOfSubPaintings
        global catDir
        
        ptngIndex -= 1
        if ptngIndex < 0:
            ptngIndex = (totalPtngs-1)
        #load new painting
        
        dispPainting = listPtngs[ptngIndex]
        
        ptgName = catDir[currentCat][dispPainting][dispPainting]["pname"]
        ptgDesc = catDir[currentCat][dispPainting][dispPainting]["desc"]
        ptgDate = catDir[currentCat][dispPainting][dispPainting]["year"]
        ptgNum = catDir[currentCat][dispPainting][dispPainting]["number"]
        saatchi= catDir[currentCat][dispPainting][dispPainting]["saatchi"]
        s6 = catDir[currentCat][dispPainting][dispPainting]["soc6"]
        try : 
            mysite = catDir[currentCat][dispPainting][dispPainting]["mysite"]
        except:
            mysite = 0
            pass
        try : 
            secid = catDir[currentCat][dispPainting][dispPainting]["secid"]
        except:
            secid = 0
            pass
        displate = catDir[currentCat][dispPainting][dispPainting]["displate"]
        dev = catDir[currentCat][dispPainting][dispPainting]["deviant"]
        buzz= catDir[currentCat][dispPainting][dispPainting]["buzz"]
        dims= catDir[currentCat][dispPainting][dispPainting]["dims"]
        try:
            hdims = catDir[currentCat][dispPainting][dispPainting]["hdims"]
        except:
            hdims = "none"
            pass
        try:
            mat = catDir[currentCat][dispPainting][dispPainting]["materialsUsed"]
        except:
            mat = "none"
            pass
        
        self.labelA.SetLabel(dispPainting)
        self.labelB.SetLabel(currentCat)
        
        self.t1.SetValue(ptgName)
        self.t2.SetValue(str(ptgDate))
        self.t2a.SetValue(str(ptgNum))
        self.t2b.SetValue(str(secid))
        self.t3.SetValue(wherePainted)
        self.t4.SetValue(dims)
        self.t5.SetValue(hdims)
        
        self.t6.SetValue(materialsUsed)
        self.t7.SetValue(ptgDesc)
        self.t10.SetValue(saatchi)
        self.t11.SetValue(dev)
        self.t12.SetValue(s6)
        self.t13.SetValue(buzz)
        self.t14.SetValue(str(mysite))
        
        self.SetStatusText("back one painting")
        
    def NextPainting(self,event):
        global listSubs
        global currentCat
        global listPtngs
        global dispPainting 
        global catIndex
        global ptngIndex
        global totalSubs
        global totalPtngs
        
        global mylibOfSubPaintings
        global catDir
        
        ptngIndex += 1
        if ptngIndex > (totalPtngs-1):
            ptngIndex =0
        #load new painting
        
        dispPainting = listPtngs[ptngIndex]
        
        ptgName = catDir[currentCat][dispPainting][dispPainting]["pname"]
        ptgDesc = catDir[currentCat][dispPainting][dispPainting]["desc"]
        ptgDate = catDir[currentCat][dispPainting][dispPainting]["year"]
        ptgNum = catDir[currentCat][dispPainting][dispPainting]["number"]
        saatchi= catDir[currentCat][dispPainting][dispPainting]["saatchi"]
        s6 = catDir[currentCat][dispPainting][dispPainting]["soc6"]
        try : 
            mysite = catDir[currentCat][dispPainting][dispPainting]["mysite"]
        except:
            mysite = 0
            pass
        try : 
            secid = catDir[currentCat][dispPainting][dispPainting]["secid"]
        except:
            secid = 0
            pass
        displate = catDir[currentCat][dispPainting][dispPainting]["displate"]
        dev = catDir[currentCat][dispPainting][dispPainting]["deviant"]
        buzz= catDir[currentCat][dispPainting][dispPainting]["buzz"]
        dims= catDir[currentCat][dispPainting][dispPainting]["dims"]
        try:
            hdims = catDir[currentCat][dispPainting][dispPainting]["hdims"]
        except:
            hdims = "none"
            pass
        try:
            mat = catDir[currentCat][dispPainting][dispPainting]["materialsUsed"]
        except:
            mat = "none"
            pass
        
        self.labelA.SetLabel(dispPainting)
        self.labelB.SetLabel(currentCat)
        
        self.t1.SetValue(ptgName)
        self.t2.SetValue(str(ptgDate))
        self.t2a.SetValue(str(ptgNum))
        self.t2b.SetValue(str(secid))
        self.t3.SetValue(wherePainted)
        self.t4.SetValue(dims)
        self.t5.SetValue(hdims)
        
        self.t6.SetValue(materialsUsed)
        self.t7.SetValue(ptgDesc)
        self.t10.SetValue(saatchi)
        self.t11.SetValue(dev)
        self.t12.SetValue(s6)
        self.t13.SetValue(buzz)
        self.t14.SetValue(str(mysite))
        
        self.SetStatusText("forward one painting")
        
    def PrevCat(self,event):
        global listSubs
        global currentCat
        global listPtngs
        global dispPainting 
        global catIndex
        global ptngIndex
        global totalSubs
        global totalPtngs
        
        global mylibOfSubPaintings
        global catDir
        
        catIndex -= 1
        
        if catIndex < 0:
            catIndex = totalSubs-1
        currentCat = listSubs[catIndex]
        
        #reload data
       
        listPtngs = mylibOfSubPaintings["list_of_cat_and_paintings"][currentCat]
        totalPtngs = len(listPtngs)
        
        dispPainting = listPtngs[0]
        
        ptgName = catDir[currentCat][dispPainting][dispPainting]["pname"]
        ptgDesc = catDir[currentCat][dispPainting][dispPainting]["desc"]
        ptgDate = catDir[currentCat][dispPainting][dispPainting]["year"]
        ptgNum = catDir[currentCat][dispPainting][dispPainting]["number"]
        saatchi= catDir[currentCat][dispPainting][dispPainting]["saatchi"]
        s6 = catDir[currentCat][dispPainting][dispPainting]["soc6"]
        try : 
            mysite = catDir[currentCat][dispPainting][dispPainting]["mysite"]
        except:
            mysite = 0
            pass
        try : 
            secid = catDir[currentCat][dispPainting][dispPainting]["secid"]
        except:
            secid = 0
            pass
        displate = catDir[currentCat][dispPainting][dispPainting]["displate"]
        dev = catDir[currentCat][dispPainting][dispPainting]["deviant"]
        buzz= catDir[currentCat][dispPainting][dispPainting]["buzz"]
        dims= catDir[currentCat][dispPainting][dispPainting]["dims"]
        try:
            hdims = catDir[currentCat][dispPainting][dispPainting]["hdims"]
        except:
            hdims = "none"
            pass
        try:
            mat = catDir[currentCat][dispPainting][dispPainting]["materialsUsed"]
        except:
            mat = "none"
            pass
        
        self.labelA.SetLabel(dispPainting)
        self.labelB.SetLabel(currentCat)
        
        self.t1.SetValue(ptgName)
        self.t2.SetValue(str(ptgDate))
        self.t2a.SetValue(str(ptgNum))
        self.t2b.SetValue(str(secid))
        self.t3.SetValue(wherePainted)
        self.t4.SetValue(dims)
        self.t5.SetValue(hdims)
        
        self.t6.SetValue(materialsUsed)
        self.t7.SetValue(ptgDesc)
        self.t10.SetValue(saatchi)
        self.t11.SetValue(dev)
        self.t12.SetValue(s6)
        self.t13.SetValue(buzz)
        self.t14.SetValue(str(mysite))
        
    def NextCat(self, event):
        global listSubs
        global currentCat
        global listPtngs
        global dispPainting 
        global catIndex
        global ptngIndex
        global totalSubs
        global totalPtngs
        
        global mylibOfSubPaintings
        global catDir
        
        catIndex = catIndex + 1

        if catIndex > (totalSubs-1):
            catIndex = 0
            
        currentCat = listSubs[catIndex]

        #reload data
        
        listPtngs = mylibOfSubPaintings["list_of_cat_and_paintings"][currentCat]
        totalPtngs = len(listPtngs)
        
        dispPainting = listPtngs[0]
        
        ptgName = catDir[currentCat][dispPainting][dispPainting]["pname"]
        ptgDesc = catDir[currentCat][dispPainting][dispPainting]["desc"]
        ptgDate = catDir[currentCat][dispPainting][dispPainting]["year"]
        ptgNum = catDir[currentCat][dispPainting][dispPainting]["number"]
        saatchi= catDir[currentCat][dispPainting][dispPainting]["saatchi"]
        s6 = catDir[currentCat][dispPainting][dispPainting]["soc6"]
        try : 
            mysite = catDir[currentCat][dispPainting][dispPainting]["mysite"]
        except:
            mysite = 0
            pass
        try : 
            secid = catDir[currentCat][dispPainting][dispPainting]["secid"]
        except:
            secid = 0
            pass
        displate = catDir[currentCat][dispPainting][dispPainting]["displate"]
        dev = catDir[currentCat][dispPainting][dispPainting]["deviant"]
        buzz= catDir[currentCat][dispPainting][dispPainting]["buzz"]
        dims= catDir[currentCat][dispPainting][dispPainting]["dims"]
        try:
            hdims = catDir[currentCat][dispPainting][dispPainting]["hdims"]
        except:
            hdims = "none"
            pass
        try:
            mat = catDir[currentCat][dispPainting][dispPainting]["materialsUsed"]
        except:
            mat = "none"
            pass
        
        self.labelA.SetLabel(dispPainting)
        self.labelB.SetLabel(currentCat)
        
        self.t1.SetValue(ptgName)
        self.t2.SetValue(str(ptgDate))
        self.t2a.SetValue(str(ptgNum))
        self.t2b.SetValue(str(secid))
        self.t3.SetValue(wherePainted)
        self.t4.SetValue(dims)
        self.t5.SetValue(hdims)
        
        self.t6.SetValue(materialsUsed)
        self.t7.SetValue(ptgDesc)
        self.t10.SetValue(saatchi)
        self.t11.SetValue(dev)
        self.t12.SetValue(s6)
        self.t13.SetValue(buzz)
        self.t14.SetValue(str(mysite))
##################################################################################
    
class App(wx.App):
    
    def OnInit(self):
         self.frame = mainMenu(parent=None, id = -1)
         self.frame.Center()
         self.frame.Show()
         self.frame.Fit()
         self.SetTopWindow(self.frame)
         return True
##################################################################################
if __name__ == '__main__':
	
    app = App()
    app.MainLoop()

    print("Ending program.")       
##################################################################################
