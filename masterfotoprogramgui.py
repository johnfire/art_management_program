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
#import pprint
import wx 
#import sys
import shutil
import json
import artmanagementcfg as cfg
import BlockWindow

   
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
        
        # Add a panel so it looks correct on all platforms
        #self.panel = wx.Panel(self, wx.ID_ANY)
        #self.panel.SetBackgroundColour("blue")
        panel = wx.Panel(self, wx.ID_ANY)
        panel.SetBackgroundColour("blue")
        hboxMain =wx.BoxSizer(wx.HORIZONTAL)
        vbox1 = wx.BoxSizer(wx.VERTICAL)
        vbox2 = wx.BoxSizer(wx.VERTICAL)
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        hbox4 = wx.BoxSizer(wx.HORIZONTAL)
        hbox5 = wx.BoxSizer(wx.HORIZONTAL)
        hbox6 = wx.BoxSizer(wx.HORIZONTAL)
        hbox7 = wx.BoxSizer(wx.HORIZONTAL)
        
#        sizer = wx.GridSizer(rows=4, cols=4, hgap=5, vgap=5)
#        
#        for i in range(1,len(cfg.subDirList)): 
#            btn = "Btn_"+str(i) 
#            sizer.Add(wx.Button(self.panel,label = btn), 0, wx.EXPAND) 
#            self.btn.Bind(wx.EVT_BUTTON, self.OnClicked) 
#        self.panel.SetSizer(sizer)  
        
        
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
        
        #self.panel = wx.Panel(self)
        #self.panel.SetBackgroundColour("blue")
        #sizer = wx.GridSizer(rows=4, cols=6, hgap=5, vgap=5)
        #button = wx.Button(self.panel, -1, label="End Program")
        #button = wx.Button(self.panel, -1, label="does nothing")
        #sizer.Add(button, 0, 0)
        
        self.SetMenuBar(menuBar)
        self.CreateStatusBar()
        self.SetStatusText("Welcome to art business management")
        
        #self.Bind(wx.EVT_BUTTON, self.OnCloseMe, button)
        
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
        
        #self.SetSizer(sizer)
        #self.Fit()
        
        label1 = wx.StaticText(panel, -1, "Name of work")
        hbox1.Add(label1, 1, wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)
        
        label2 = wx.StaticText(panel, -1, "Date painted")
        hbox2.Add(label2, 1, wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)
        
        label3 = wx.StaticText(panel, -1, "Where painted")
        hbox3.Add(label3, 1, wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)
        
        label4 = wx.StaticText(panel, -1, "Vertical dimension")
        hbox4.Add(label4, 1, wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)
        
        label5 = wx.StaticText(panel, -1, "Horizontal dimension")
        hbox5.Add(label5, 1, wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)
        
        label6 = wx.StaticText(panel, -1, "Materials used")
        hbox6.Add(label6, 1, wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)
        
        
        label7 = wx.StaticText(panel, -1, "Description")
        hbox7.Add(label7, 1, wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)
        
         
        
        self.t1 = wx.TextCtrl(panel,-1,size=(400,50))
        hbox1.Add(self.t1,1,wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)
        
        self.t2 = wx.TextCtrl(panel,-1,size=(400,50))
        hbox2.Add(self.t2,1,wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)
        
        self.t3 = wx.TextCtrl(panel,-1,size=(400,50))
        hbox3.Add(self.t3,1,wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)
        
        self.t4 = wx.TextCtrl(panel,-1,size=(400,50))
        hbox4.Add(self.t4,1,wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)
        
        self.t5 = wx.TextCtrl(panel,-1,size=(400,50))
        hbox5.Add(self.t5,1,wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)
        
        self.t6 = wx.TextCtrl(panel,-1,size=(400,50))
        hbox6.Add(self.t6,1,wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)
        
        self.t7 = wx.TextCtrl(panel,-1,size=(400,50))
        hbox7.Add(self.t7,1,wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)
        
        
        vbox1.Add(hbox1)
        vbox1.Add(hbox2) 
        vbox1.Add(hbox3)
        vbox1.Add(hbox4)
        vbox1.Add(hbox5)
        vbox1.Add(hbox6)
        vbox1.Add(hbox7)
        hboxMain.Add(vbox1)
        hboxMain.Add(vbox2)
        
        panel.SetSizer(hboxMain)
        panel.Center()
        panel.Show()
        panel.Fit()
    
    #here are the actions for above code from menu
    
    #SHOULD BE WORKING
    def OpenFile(self,event):
       
        listOfPaintings = []
        self.SetStatusText("Opens the database")
        dialog = wx.DirDialog(None, "Choose a directory to work with: ", style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
        if dialog.ShowModal() == wx.ID_OK:
            #print(dialog.GetPath())
            cfg.workingDir = str(dialog.GetPath())
            os.chdir(str(dialog.GetPath()))
        dialog.Destroy()
        cfg.subDirList = os.listdir(cfg.workingDir)
        cfg.subDirList.remove("info")
        for each in cfg.subDirList:
            listOfPaintings =[]
            if True == os.path.isdir(cfg.workingDir + "/" + each):
                cfg.subDirPaths.append(cfg.workingDir + "/" + each)
                os.chdir(cfg.workingDir + "/" + each)
                listOfPaintings = os.listdir(os.getcwd())
                for eachone in listOfPaintings:
                    cfg.paintingList.append(eachone)
                    cfg.paintingPaths.append(cfg.workingDir + "/" + each + "/" + eachone)
                    cfg.paintingDic[eachone] = cfg.workingDir + "/" + each + "/" + eachone
        mylibListOfPaintings = {"list_of_paintings" : cfg.paintingList }
        mylibOfSubdirectories = {"list_of_subdirectories" : cfg.subDirList}
        
        cfg.myData = {"paintings": mylibListOfPaintings, "subdir" : mylibOfSubdirectories}
        jsonData = json.dumps(cfg.myData, indent=4, separators=(". ", " = "))
        print(jsonData)
        print("\n")
        print(os.getcwd())
        filename = "myfisrtjsonfile"
        with open(filename, 'w+') as f:
            json.dump(cfg.myData, f)
            
        sizer = wx.GridSizer(rows=4, cols=4, hgap=5, vgap=5)  
        print(cfg.subDirList)
        sizernumber = 0
        for i in cfg.subDirList: 
            btn = "Btn_"+ str(i) 
            sizer.Add(wx.Button(self.panel,label = btn), sizernumber, wx.EXPAND) 
            sizernumber +=1
            #self.btn.Bind(wx.EVT_BUTTON, self.OnClicked) 
        self.panel.SetSizer(sizer)  
        
        
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
            for each in cfg.dirlist:
                os.mkdir("./" + each)   
                
    #SHOULD BE WORKING
    def AddNewSubFolder(self, event):
        self.SetStatusText("Add a Subfolder to all Paintings")
        dlg = wx.TextEntryDialog(None, "What is the new folder named",'Name of new folder', 'new folder')
        if dlg.ShowModal() == wx.ID_OK:
            response = dlg.GetValue()
            os.chdir(cfg.workingDir)
            for each in os.getcwd():
                os.chdir(cfg.workingDir + "/" + each)
                for each1 in os.getcwd():
                    os.chdir(cfg.workingDir + "/" + each + "/" + each1)
                    os.mkdir(response)  

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
         self.frame.Center()
         self.frame.Show()
         self.frame.Fit()
         self.SetTopWindow(self.frame)
         #self.frame.OpenFile()
         return True
##################################################################################
##################################################################################

#if __name__ == __main__
#    main()
	
answer = 2
app = App()
app.MainLoop()
print("Ending program.")
        
##################################################################################
