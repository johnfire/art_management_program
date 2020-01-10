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

catDir={}
mylibListOfPaintings = {}
mylibOfSubdirectories = {}
jsonData = {}
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
        vbox1 = wx.BoxSizer(wx.VERTICAL)
        vbox2 = wx.BoxSizer(wx.VERTICAL)
        hbox0 = wx.BoxSizer(wx.HORIZONTAL)
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        hbox1a = wx.BoxSizer(wx.HORIZONTAL)
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        hbox4 = wx.BoxSizer(wx.HORIZONTAL)
        hbox5 = wx.BoxSizer(wx.HORIZONTAL)
        hbox6 = wx.BoxSizer(wx.HORIZONTAL)
        hbox7 = wx.BoxSizer(wx.HORIZONTAL)
        vboxBig = wx.BoxSizer(wx.VERTICAL)
 
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
        #menuItemBlank = menu2.Append(-1, "Blank, future use")
        
        #menuItemDisplayWork = menu3.Append(-1, "Display a Work")
        #menuItemDisplayAll = menu3.Append(-1, "Display All Works")
        
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
        
        #self.Bind(wx.EVT_MENU, self.DisplayWork, menuItemDisplayWork)
        #self.Bind(wx.EVT_MENU, self.DisplayAll, menuItemDisplayAll)
        
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
        
        label1a =wx.StaticText(panel, -1, "Catagory")
        hbox1a.Add(label1a, 1, wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)
        
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
         
        self.t1 = wx.TextCtrl(panel,-1,size=(350,40))
        hbox1.Add(self.t1,1,wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)
        
        self.t1a = wx.TextCtrl(panel,-1,size=(350,40))
        hbox1a.Add(self.t1a,1,wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)
        
        self.t2 = wx.TextCtrl(panel,-1,size=(350,40))
        hbox2.Add(self.t2,1,wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)
        
        self.t3 = wx.TextCtrl(panel,-1,size=(350,40))
        hbox3.Add(self.t3,1,wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)
        
        self.t4 = wx.TextCtrl(panel,-1,size=(350,40))
        hbox4.Add(self.t4,1,wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)
        
        self.t5 = wx.TextCtrl(panel,-1,size=(350,40))
        hbox5.Add(self.t5,1,wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)
        
        self.t6 = wx.TextCtrl(panel,-1,size=(350,80),style = wx.TE_MULTILINE)
        hbox6.Add(self.t6,1,wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)
        
        self.t7 = wx.TextCtrl(panel,-1,size=(350,160),style = wx.TE_MULTILINE)
        hbox7.Add(self.t7,1,wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)
        
        vbox1.Add(hbox1)
        vbox1.Add(hbox1a)
        vbox1.Add(hbox2) 
        vbox1.Add(hbox3)
        vbox1.Add(hbox4)
        vbox1.Add(hbox5)
        vbox1.Add(hbox6)
        vbox1.Add(hbox7)

        hboxMain.Add(vbox1)
        hboxMain.Add(vbox2)
        vboxBig.Add(hbox0)
        vboxBig.Add(hboxMain)
        
        panel.SetSizer(vboxBig)
        panel.Center()
        panel.Show()
        panel.Fit()
    
    #here are the actions for above code for the menu
    
    #SHOULD BE WORKING
    def OpenFile(self,event):
        global catDir
        global mylibListOfPaintings
        global mylibOfSubdirectories 
        global jsonData 
        
        dirOfCatandPaintings = {}
        
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
                                listOfPaintings[eacheins]= datastuff
                    os.chdir("..")
                    os.chdir("..")

                catDir[each] =listOfPaintings

        mylibListOfPaintings = {"list_of_paintings" : cfg.paintingList }
        mylibOfSubdirectories = {"list_of_subdirectories" : cfg.subDirList}
        mylibOfSubPaintings = {"list_of_cat_and_paintings": dirOfCatandPaintings}
        
        cfg.myData = [cfg.workingDir, mylibOfSubdirectories,mylibOfSubPaintings]
        cfg.myDataBase =[ mylibOfSubdirectories, mylibOfSubPaintings, catDir]
        jsonData = json.dumps(cfg.myData, sort_keys=True,  indent=4, separators=(". ", " = "))
        json1Data = json.dumps(cfg.myDataBase, sort_keys=True,  indent=4, separators=(". ", " = "))

        print("\n")
        print(os.getcwd())
        
        os.chdir(cfg.workingDir + "/" + "info")
        filename = "myDatajsonfile"
        with open(filename, 'w') as f:
             f.write(jsonData)
        file2name = "myDataBasejsonfile"
        with open(file2name, 'w') as f:
             f.write(json1Data)
             
             
        #now load correct stuff to screen.
        self.labelA.SetLabel("blah blah")
        self.labelB.SetLabel("and more bah")
        self.t1.SetValue("some text here")
        self.t1a.SetValue("something here")
        self.t2.SetValue("something here")
        self.t3.SetValue("something here")
        self.t4.SetValue("something here")
        self.t5.SetValue("something here")
        self.t6.SetValue("something here")
        self.t7.SetValue("something here")
        
        
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
        self.SetStatusText("Display all works")
        
    def GetHelp(self, event):
        self.SetStatusText("Help")
        pass
    
    def SetPreferences(self, event):
        self.SetStatusText("Set up preferences")
        pass
    
    def PrevPainting(self,event):
        global jsonData
        print(jsonData)
        print("\n")
        print(os.getcwd())
        self.SetStatusText("back one painting")
        pass
        
    def NextPainting(self,event):
        self.SetStatusText("forward one painting")
        pass
        
    def PrevCat(self,event):
        pass
        
    def NextCat(self, event):
        pass
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
