#!/home/christopher/anaconda3/bin/python3

# -*- coding: utf-8 -*-
"""
begun on Sun Aug 25 11:24:43 2019
ver alpha 16 jan 2020
this is the main foto management proram.
@author: christopher rehm
note this program uses the wxPython4.0 and wxWidgets for GUI development,
both must be installed
plase use wxPython 4.0 or higher 
"""
import os
import wx
import shutil
import json
import artmanagementcfg as cfg
from markdown import markdown
import pdfkit
from PIL import Image

##################################################################################
def makeList():
    # this function makes a list of all paintings in the file of works
    count = 1
    os.chdir(cfg.myworkingFolder)
    print(os.getcwd())
    os.chdir("./info")  # enter info dir, where we keep all info files
    if os.path.isfile("./finishedPaintings.txt"):
        os.rename("./finishedPaintings.txt","./finishedPaintingsOld.txt")
    fh = open("./finishedPaintings.txt", "w+")
    mylist = {}
    mylist = searchLevel(cfg.myworkingFolder)
    for each in mylist:
        print(each)
        fh.write(each)
        fh.write("\n")
        for eachone in mylist[each]:
            fh.write("    " + str(count) + " " + eachone)
            fh.write("\n")
            count += 1
    fh.close()
    os.chdir("..")


##################################################################################
def createAllSubfolders():
    os.chdir(cfg.workingDir)
    mylist = os.listdir()
    for each in mylist:
        chkdir = cfg.workingDir + "/" + str(each)
        if os.path.isdir(each) is True:
            os.chdir(chkdir)
            mylist1 = os.listdir()
            for each1 in mylist1:
                chkdir1 = chkdir + "/" + str(each1)
                if os.path.isdir(each1) is True:
                    os.chdir(chkdir1)
                    for every in cfg.dirlist:
                        newdir = chkdir + "/" + str(each1) + "/" + str(every)
                        if os.path.isdir(newdir) is False:
                            os.mkdir(newdir)
                    os.chdir("..")
            os.chdir("..")


##################################################################################
def moveAllPhotos():
    for each in cfg.paintingPaths:
        os.chdir(each)
        listOfFilesToMove = os.listdir(".")
        for each in listOfFilesToMove:
            if each.endswith(".CR2"):
                shutil.move("./" + each, "./cr2type/" + each)
            elif each.endswith(".JPG"):
                shutil.move("./" + each, "./jpgtype/" + each)
            elif each.endswith(".jpg"):
                shutil.move("./" + each, "./oldCamerPics/" + each)
            else:
                pass


##################################################################################
def renameFotos():
    pass


##################################################################################
def searchLevel(myLevel):
    tableofitems = {}
    thisdirlist = os.listdir(myLevel)
    thisdirlist.remove('info')
    #countoffiles = 1
    for each in thisdirlist:
        if os.path.isdir(myLevel + "/" + each) is True:
            mynewlevel = myLevel + "/" + each
            tableofitems[each] = os.listdir(mynewlevel)
    return tableofitems


##################################################################################

##################################################################################
# GUI APP
class mainMenu(wx.Frame):
    def __init__(self, parent, id):

        wx.Frame.__init__(self, parent, id, "Menus", size=(1200, 800))

        panel = wx.Panel(self, wx.ID_ANY)
        panel.SetBackgroundColour("blue")

        vboxBig = wx.BoxSizer(wx.VERTICAL)

        hbox0 = wx.BoxSizer(wx.HORIZONTAL)
        hboxMain = wx.BoxSizer(wx.HORIZONTAL)

        vbox1 = wx.BoxSizer(wx.VERTICAL)

        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        hbox1a = wx.BoxSizer(wx.HORIZONTAL)
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        hbox4 = wx.BoxSizer(wx.HORIZONTAL)
        hbox5 = wx.BoxSizer(wx.HORIZONTAL)
        hbox6 = wx.BoxSizer(wx.HORIZONTAL)
        hbox7 = wx.BoxSizer(wx.HORIZONTAL)

        vbox2 = wx.BoxSizer(wx.VERTICAL)

        hboxr1 = wx.BoxSizer(wx.HORIZONTAL)
        hboxr1aa = wx.BoxSizer(wx.HORIZONTAL)
        hboxr1aaa = wx.BoxSizer(wx.HORIZONTAL)
        hboxr1a = wx.BoxSizer(wx.HORIZONTAL)
        hboxr2 = wx.BoxSizer(wx.HORIZONTAL)

        menuBar = wx.MenuBar()
        menu1 = wx.Menu()
        menu2 = wx.Menu()
        menu3 = wx.Menu()
        menu4 = wx.Menu()
        menuItemLoad = menu1.Append(-1, "&Load dir")
        menuItemClose = menu1.Append(-1, "&Close dir")
        menuItemExit = menu1.Append(-1, "&Exit...")

        menuItemNewPainting = menu2.Append(-1, "&New Painting")
        menuItemNewSubfolder = menu2.Append(-1, "Create New Subfolder")

        menuItemMakeListAll = menu3.Append(-1, "List all works")
        menuItemCreateAllSubfolders = menu3.Append(-1, "Make All Subfolders")
        menuItemMoveFotosToFolders = menu3.Append(-1, "Move Fotos to Subfolders")
        menuItemColate = menu3.Append(-1, "Collate all Info Sheets")
        menuItemRenameAll = menu3.Append(-1, "Rename All Fotos")

        menuItemHelp = menu4.Append(-1, "Help")
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

        workName = "Name of Work"
        catName = "Current Catagory"

        self.b1 = wx.Button(panel, label="Previous Work")
        hbox0.Add(self.b1, 1, wx.EXPAND | wx.ALIGN_CENTER | wx.ALL, 5)
        self.labelA = wx.StaticText(panel, -1, workName, style=wx.TE_CENTER)
        hbox0.Add(self.labelA, 1, wx.EXPAND | wx.ALIGN_CENTER | wx.ALL, 5)
        self.b2 = wx.Button(panel, label="Next Work")
        hbox0.Add(self.b2, 1, wx.EXPAND | wx.ALIGN_CENTER | wx.ALL, 5)

        self.b3 = wx.Button(panel, label="Previous Catagory")
        hbox0.Add(self.b3, 1, wx.EXPAND | wx.ALIGN_CENTER | wx.ALL, 5)
        self.labelB = wx.StaticText(panel, -1, catName, style=wx.TE_CENTER)
        hbox0.Add(self.labelB, 1, wx.EXPAND | wx.ALIGN_CENTER | wx.ALL, 5)
        self.b4 = wx.Button(panel, label="Next Catagory")
        hbox0.Add(self.b4, 1, wx.EXPAND | wx.ALIGN_CENTER | wx.ALL, 5)

        self.b1.Bind(wx.EVT_BUTTON, self.PrevPainting)
        self.b2.Bind(wx.EVT_BUTTON, self.NextPainting)
        self.b3.Bind(wx.EVT_BUTTON, self.PrevCat)
        self.b4.Bind(wx.EVT_BUTTON, self.NextCat)

        label1 = wx.StaticText(panel, -1, "Name of work")
        hbox1.Add(label1, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)
        self.t1 = wx.TextCtrl(panel, -1, size=(350, 40))
        hbox1.Add(self.t1, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)
        label2 = wx.StaticText(panel, -1, "Date painted")
        hbox2.Add(label2, 1, wx.ALIGN_LEFT | wx.ALL, 5)
        self.t2 = wx.TextCtrl(panel, -1, size=(100, 40))
        hbox2.Add(self.t2, 1, wx.ALIGN_LEFT | wx.ALL, 5)
        label2a = wx.StaticText(panel, -1, "ID number")
        hbox2.Add(label2a, 1, wx.ALIGN_LEFT | wx.ALL, 5)
        self.t2a = wx.TextCtrl(panel, -1, size=(50, 40))
        hbox2.Add(self.t2a, 1, wx.ALIGN_LEFT | wx.ALL, 5)
        label2b = wx.StaticText(panel, -1, "Count/Year")
        hbox2.Add(label2b, 1, wx.ALIGN_LEFT | wx.ALL, 5)
        self.t2b = wx.TextCtrl(panel, -1, size=(50, 40))
        hbox2.Add(self.t2b, 1, wx.ALIGN_LEFT | wx.ALL, 5)

        label3 = wx.StaticText(panel, -1, "Where painted")
        hbox3.Add(label3, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)

        self.t3 = wx.TextCtrl(panel, -1, size=(350, 40))
        hbox3.Add(self.t3, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)

        label4 = wx.StaticText(panel, -1, "Vertical dim")
        hbox4.Add(label4, 1, wx.ALIGN_LEFT | wx.ALL, 5)

        self.t4 = wx.TextCtrl(panel, -1, size=(50, 40))
        hbox4.Add(self.t4, 1, wx.ALIGN_LEFT | wx.ALL, 5)

        label5 = wx.StaticText(panel, -1, "Horizontal dim")
        hbox4.Add(label5, 1, wx.ALIGN_LEFT | wx.ALL, 5)

        self.t5 = wx.TextCtrl(panel, -1, size=(50, 40))
        hbox4.Add(self.t5, 1, wx.ALIGN_LEFT | wx.ALL, 5)

        label10 = wx.StaticText(panel, -1, cfg.gallery1)
        hbox5.Add(label10, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)

        self.t10 = wx.TextCtrl(panel, -1, size=(50, 40))
        hbox5.Add(self.t10, 1, wx.ALIGN_LEFT | wx.ALL, 5)

        label11 = wx.StaticText(panel, -1, cfg.gallery2)
        hbox5.Add(label11, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)

        self.t11 = wx.TextCtrl(panel, -1, size=(50, 40))
        hbox5.Add(self.t11, 1, wx.ALIGN_LEFT | wx.ALL, 5)

        label12 = wx.StaticText(panel, -1, cfg.gallery3)
        hbox5.Add(label12, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)

        self.t12 = wx.TextCtrl(panel, -1, size=(50, 40))
        hbox5.Add(self.t12, 1, wx.ALIGN_LEFT | wx.ALL, 5)

        label13 = wx.StaticText(panel, -1, cfg.gallery4)
        hbox5.Add(label13, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)

        self.t13 = wx.TextCtrl(panel, -1, size=(50, 40))
        hbox5.Add(self.t13, 1, wx.ALIGN_LEFT | wx.ALL, 5)

        label14 = wx.StaticText(panel, -1, cfg.gallery5)
        hbox5.Add(label14, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)

        self.t14 = wx.TextCtrl(panel, -1, size=(50, 40))
        hbox5.Add(self.t14, 1, wx.ALIGN_LEFT | wx.ALL, 5)

        label6 = wx.StaticText(panel, -1, "Materials used")
        hbox6.Add(label6, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)

        label7 = wx.StaticText(panel, -1, "Description")
        hbox7.Add(label7, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)

        self.t6 = wx.TextCtrl(panel, -1, size=(350, 80), style=wx.TE_MULTILINE)
        hbox6.Add(self.t6, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)

        self.t7 = wx.TextCtrl(panel, -1, size=(350, 160), style=wx.TE_MULTILINE)
        hbox7.Add(self.t7, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)

        # ------------------------#

        self.savebtn = wx.Button(panel, label="Save painting data")
        hboxr2.Add(
            self.savebtn,
            1,
            wx.FIXED_MINSIZE | wx.ALIGN_CENTER | wx.ALIGN_BOTTOM | wx.ALL,
            2,
        )
        self.savebtn.Bind(wx.EVT_BUTTON, self.onSavePainting)

        self.printbtn = wx.Button(panel, label="Print .md and pdf")
        hboxr2.Add(
            self.printbtn,
            1,
            wx.FIXED_MINSIZE | wx.ALIGN_CENTER | wx.ALIGN_BOTTOM | wx.ALL,
            2,
        )
        self.printbtn.Bind(wx.EVT_BUTTON, self.MakeMd)

        self.b5 = wx.Button(panel, label="EXIT PROGRAM")
        hboxr2.Add(
            self.b5, 1, wx.FIXED_MINSIZE | wx.ALIGN_CENTER | wx.ALIGN_BOTTOM | wx.ALL, 2
        )
        self.b5.Bind(wx.EVT_BUTTON, self.OnQuit)

        image_size = (480, 480)

        self.max_size = 480

        img = wx.Image(*image_size)

        self.image_ctrl = wx.StaticBitmap(panel, bitmap=wx.Bitmap(img))
        hboxr1.Add(self.image_ctrl, 1, wx.ALIGN_TOP, 0)

        self.browse_btn = wx.Button(panel, label="LR Browse")
        self.browseHR_btn = wx.Button(panel, label="HR Browse")
        hboxr1a.Add(
            self.browse_btn,
            0,
            wx.FIXED_MINSIZE | wx.ALIGN_BOTTOM | wx.ALIGN_CENTER | wx.ALL,
            1,
        )
        hboxr1a.Add(
            self.browseHR_btn,
            0,
            wx.FIXED_MINSIZE | wx.ALIGN_BOTTOM | wx.ALIGN_CENTER | wx.ALL,
            1,
        )

        self.browse_btn.Bind(wx.EVT_BUTTON, self.on_browse)
        self.browseHR_btn.Bind(wx.EVT_BUTTON, self.on_HRbrowse)

        self.photo_txt = wx.StaticText(panel, -1, "This is the LR file")
        hboxr1aa.Add(
            self.photo_txt,
            0,
            wx.FIXED_MINSIZE | wx.ALIGN_BOTTOM | wx.ALIGN_LEFT | wx.ALL,
            1,
        )
        self.photo_HRtxt = wx.StaticText(panel, -1, "This is the HR file")
        hboxr1aaa.Add(
            self.photo_HRtxt,
            0,
            wx.FIXED_MINSIZE | wx.ALIGN_BOTTOM | wx.ALIGN_LEFT | wx.ALL,
            1,
        )

        vbox1.Add(hbox1, 1, wx.EXPAND | wx.ALIGN_CENTER | wx.ALL, 2)
        vbox1.Add(hbox1a, 1, wx.EXPAND | wx.ALIGN_CENTER | wx.ALL, 2)
        vbox1.Add(hbox2, 1, wx.EXPAND | wx.ALIGN_CENTER | wx.ALL, 2)
        vbox1.Add(hbox3, 1, wx.EXPAND | wx.ALIGN_CENTER | wx.ALL, 2)
        vbox1.Add(hbox4, 1, wx.EXPAND | wx.ALIGN_CENTER | wx.ALL, 2)
        vbox1.Add(hbox5, 1, wx.EXPAND | wx.ALIGN_CENTER | wx.ALL, 2)
        vbox1.Add(hbox6, 1, wx.EXPAND | wx.ALIGN_CENTER | wx.ALL, 2)
        vbox1.Add(hbox7, 1, wx.EXPAND | wx.ALIGN_CENTER | wx.ALL, 2)

        vbox2.Add(hboxr1, 1, wx.EXPAND | wx.ALIGN_BOTTOM | wx.ALIGN_CENTER | wx.ALL, 4)
        vbox2.Add(
            hboxr1aa, 0, wx.FIXED_MINSIZE | wx.ALIGN_BOTTOM | wx.ALIGN_LEFT | wx.ALL, 1
        )
        vbox2.Add(
            hboxr1aaa, 0, wx.FIXED_MINSIZE | wx.ALIGN_BOTTOM | wx.ALIGN_LEFT | wx.ALL, 1
        )
        vbox2.Add(
            hboxr1a, 0, wx.FIXED_MINSIZE | wx.ALIGN_BOTTOM | wx.ALIGN_CENTER | wx.ALL, 1
        )
        vbox2.Add(
            hboxr2, 0, wx.FIXED_MINSIZE | wx.ALIGN_BOTTOM | wx.ALIGN_CENTER | wx.ALL, 1
        )

        hboxMain.Add(vbox1, 1, wx.EXPAND | wx.ALIGN_CENTER | wx.ALL, 2)
        hboxMain.Add(vbox2, 1, wx.EXPAND | wx.ALIGN_CENTER | wx.ALL, 2)

        vboxBig.Add(hbox0, 1, wx.EXPAND | wx.ALIGN_CENTER | wx.ALL, 2)
        vboxBig.Add(hboxMain, 1, wx.EXPAND | wx.ALIGN_CENTER | wx.ALL, 2)

        panel.SetSizer(vboxBig)
        panel.Center()
        panel.Show()
        panel.Fit()

        self.labelA.SetLabel(cfg.nameOfPaintingfile)
        self.labelB.SetLabel(cfg.nameOfCatagory)

        self.t1.SetValue(cfg.nameOfPainting)
        self.t2.SetValue(cfg.datePainted)
        self.t2a.SetValue((cfg.idnum))
        self.t2b.SetValue((cfg.secid))
        self.t3.SetValue(cfg.wherePainted)
        self.t4.SetValue(cfg.Dims)
        self.t5.SetValue(cfg.hDims)
        self.t6.SetValue(cfg.materialsUsed)
        self.t7.SetValue(cfg.description)
        self.t10.SetValue((cfg.gallery1Val))
        self.t11.SetValue((cfg.gallery2Val))
        self.t12.SetValue((cfg.gallery3Val))
        self.t13.SetValue((cfg.gallery4Val))
        self.t14.SetValue((cfg.gallery5Val))

        # load working dir from json file?????
        print(cfg.workingDir)
        self.OpenFile(event="none", opt=cfg.workingDir)

    # ++++++++++++++++++++++++++++++++++++++++++++++++
    def dispData(self):

        #print("in dispData function")
        ptgName = cfg.catDir[cfg.currentCat][cfg.dispPainting][cfg.dispPainting]["pname"]
        #print(str(cfg.catDir[cfg.currentCat][cfg.dispPainting]))
        #print("painting name is:")
        #print(ptgName)
        ptgDesc = cfg.catDir[cfg.currentCat][cfg.dispPainting][cfg.dispPainting]["desc"]
        ptgDate = cfg.catDir[cfg.currentCat][cfg.dispPainting][cfg.dispPainting]["year"]
        ptgNum = cfg.catDir[cfg.currentCat][cfg.dispPainting][cfg.dispPainting]["number"]
        saatchi = cfg.catDir[cfg.currentCat][cfg.dispPainting][cfg.dispPainting]["saatchi"]
        s6 = cfg.catDir[cfg.currentCat][cfg.dispPainting][cfg.dispPainting]["soc6"]
        mysite = cfg.catDir[cfg.currentCat][cfg.dispPainting][cfg.dispPainting]["mysite"]
        secid = cfg.catDir[cfg.currentCat][cfg.dispPainting][cfg.dispPainting]["secid"]
        picLR = cfg.catDir[cfg.currentCat][cfg.dispPainting][cfg.dispPainting]["locLRfoto"]
        picHR = cfg.catDir[cfg.currentCat][cfg.dispPainting][cfg.dispPainting]["locHRfoto"]
        dev = cfg.catDir[cfg.currentCat][cfg.dispPainting][cfg.dispPainting]["deviant"]
        buzz = cfg.catDir[cfg.currentCat][cfg.dispPainting][cfg.dispPainting]["buzz"]
        dims = cfg.catDir[cfg.currentCat][cfg.dispPainting][cfg.dispPainting]["dims"]
        hDims = cfg.catDir[cfg.currentCat][cfg.dispPainting][cfg.dispPainting]["hDims"]
        materialsUsed = cfg.catDir[cfg.currentCat][cfg.dispPainting][cfg.dispPainting]["materials"]
        wherePainted = cfg.catDir[cfg.currentCat][cfg.dispPainting][cfg.dispPainting]["wherePainted"]

        self.labelA.SetLabel(cfg.dispPainting)
        self.labelB.SetLabel(cfg.currentCat)

        self.t1.SetValue(ptgName)
        self.t2.SetValue(ptgDate)
        self.t2a.SetValue((ptgNum))
        self.t2b.SetValue(secid)
        self.t3.SetValue(wherePainted)
        self.t4.SetValue(dims)
        self.t5.SetValue(hDims)
        self.t6.SetValue(materialsUsed)
        self.t7.SetValue(ptgDesc)
        self.t10.SetValue((saatchi))
        self.t11.SetValue((dev))
        self.t12.SetValue((s6))
        self.t13.SetValue((buzz))
        self.t14.SetValue((mysite))
        self.photo_txt.SetLabel(picLR)
        self.photo_HRtxt.SetLabel(picHR)
        if picLR != "No Pic":
            self.load_image()

    # ++++++++++++++++++++++++++++++++++++++++++++++++
    # WORKING
    def OpenFile(self, event, opt=""):
        print("opening the working file")
        print(cfg.workingDir)
        self.SetStatusText("Opens the Database")
        if opt == "":
            dialog = wx.DirDialog(
                None,
                "Choose a directory to work with: ",
                style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON,
            )
            if dialog.ShowModal() == wx.ID_OK:
                cfg.workingDir = str(dialog.GetPath())
                cfg.myworkingFolder = str(dialog.GetPath())
                os.chdir(str(dialog.GetPath()))
            dialog.Destroy()
        else:
            os.chdir(cfg.workingDir)
        cfg.subDirList = os.listdir(cfg.workingDir)
        cfg.subDirList.remove("info")
        for each in cfg.subDirList:
            listOfPaintings = {}
            if True == os.path.isdir(cfg.workingDir + "/" + each):
                cfg.subDirPaths.append(cfg.workingDir + "/" + each)
                os.chdir(cfg.workingDir + "/" + each)
                thePaintings = os.listdir(os.getcwd())
                cfg.dirOfCatandPaintings[each] = thePaintings
                for eacheins in thePaintings:
                    os.chdir(cfg.workingDir + "/" + each + "/" + eacheins + "/info")
                    for theFile in os.listdir("."):
                        if theFile.endswith(".json"):
                            with open(theFile, "r") as content:
                                datastuff = json.load(content)
                                listOfPaintings[eacheins] = datastuff
                    os.chdir("..")
                    os.chdir("..")

                cfg.catDir[each] = listOfPaintings

        cfg.mylibListOfPaintings = {"list_of_paintings": cfg.paintingList}
        print("the total number of paintings is ", len(cfg.mylibListOfPaintings))
        cfg.mylibOfSubdirectories = {"list_of_subdirectories": cfg.subDirList}
        cfg.mylibOfSubPaintings = {
            "list_of_cat_and_paintings": cfg.dirOfCatandPaintings
        }

        jsonData = json.dumps(
            cfg.mylibOfSubdirectories, sort_keys=True, indent=4, separators=(",", ": ")
        )
        json1Data = json.dumps(
            cfg.mylibOfSubPaintings, sort_keys=True, indent=4, separators=(",", ": ")
        )
        json2Data = json.dumps(
            cfg.catDir, sort_keys=True, indent=4, separators=(",", ": ")
        )
        json3Data = json.dumps(
            cfg.workingDir, sort_keys=True, indent=4, separators=(",", ": ")
        )

        print("\n")
        print(os.getcwd())

        os.chdir(cfg.workingDir + "/" + "info")
        filename = "libOfSubdirs.json"
        with open(filename, "w") as f:
            f.write(jsonData)
        file2name = "libOfSubsandPaintngs.json"
        with open(file2name, "w") as f:
            f.write(json1Data)
        file3name = "alljsondatagrams.json"
        with open(file3name, "w") as f:
            f.write(json2Data)
        file4name = "fliepathmainfolder.json"
        with open(file4name, "w") as f:
            f.write(json3Data)

        # now load correct stuff to screen.

        cfg.listSubs = cfg.mylibOfSubdirectories["list_of_subdirectories"]
        cfg.totalSubs = len(cfg.listSubs)
        cfg.currentCat = cfg.listSubs[1]
        #print(cfg.currentCat)
        cfg.listPtngs = cfg.mylibOfSubPaintings["list_of_cat_and_paintings"][cfg.currentCat]
        print(cfg.mylibOfSubPaintings["list_of_cat_and_paintings"][cfg.currentCat])
        cfg.totalPtngs = len(cfg.listPtngs)
        print(cfg.totalPtngs)
        #print(cfg.listPtngs[0])
        cfg.dispPainting = cfg.listPtngs[0]

        self.dispData()

    # ++++++++++++++++++++++++++++++++++++++++++++++++
    # WORKING
    def CloseFile(self, event):
        self.SetStatusText("Closes the database")
        wx.MessageBox(
            "This closes the file ", "fileloader", wx.OK | wx.ICON_INFORMATION, self
        )

    # ++++++++++++++++++++++++++++++++++++++++++++++++
    # WORKING
    def OnAbout(self, event):
        self.SetStatusText("About this Program")
        wx.MessageBox(
            "This program manages data and files for an artist.\n See the user manual for more info.\n if you use regularly a 10 € contribution to my paypal account would be helpful, to keep this project and others like it going. christopherrehm@web.de",
            "About Art Biz Manager",
            wx.OK | wx.ICON_INFORMATION,
            self,
        )

    # ++++++++++++++++++++++++++++++++++++++++++++++++
    # WORKING
    def OnCloseMe(self, event):
        self.Close()

    # ++++++++++++++++++++++++++++++++++++++++++++++++
    # WORKING
    def OnQuit(self, event):
        self.Close()

    # ++++++++++++++++++++++++++++++++++++++++++++++++
    # working
    def on_browse(self, event):
        """
        Browse for an image file
        @param event: The event object
        """
        wildcard = "JPEG files (*.jpg)|*.jpg"
        with wx.FileDialog(
            None, "Choose a file", wildcard=wildcard, style=wx.ID_OPEN
        ) as dialog:
            if dialog.ShowModal() == wx.ID_OK:
                self.photo_txt.SetLabel(dialog.GetPath())
                self.load_image()

    # ++++++++++++++++++++++++++++++++++++++++++++++++

    def on_HRbrowse(self, event):
        """
        Browse for an image file
        @param event: The event object
        """
        wildcard = "JPEG files (*.jpg)|*.jpg"
        with wx.FileDialog(
            None, "Choose a file", wildcard=wildcard, style=wx.ID_OPEN
        ) as dialog:
            if dialog.ShowModal() == wx.ID_OK:
                self.photo_HRtxt.SetLabel(dialog.GetPath())

    # ++++++++++++++++++++++++++++++++++++++++++++++++
    # working
    def load_image(self):
        """
        Load the image and display it to the user
        """
        
        filepath = self.photo_txt.GetLabel()
        if os.path.exists(filepath):
            img = wx.Image(filepath, wx.BITMAP_TYPE_ANY)
    
            # scale the image, preserving the aspect ratio
            W = img.GetWidth()
            H = img.GetHeight()
            if W > H:
                NewW = self.max_size
                NewH = self.max_size * H / W
            else:
                NewH = self.max_size
                NewW = self.max_size * W / H
            img = img.Scale(NewW, NewH)
    
            self.image_ctrl.SetBitmap(wx.Bitmap(img))
            self.Refresh()
        else:
            print("no image yet")

    # ++++++++++++++++++++++++++++++++++++++++++++++++
    # WORKING
    def NewPainting(self, event):

        self.SetStatusText("Create a New Painting")
        dialog = wx.DirDialog(
            None,
            "Choose a directory for your painting: ",
            style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON,
        )
        if dialog.ShowModal() == wx.ID_OK:
            print(dialog.GetPath())
            os.chdir(str(dialog.GetPath()))
            cfg.currentCat = os.getcwd()
            tmpcat = cfg.currentCat
        dialog.Destroy()
        dlg = wx.TextEntryDialog(
            None,
            "What is the new painting named",
            "Name of new painting",
            "new_painting",
        )
        if dlg.ShowModal() == wx.ID_OK:
            response = dlg.GetValue()
            os.mkdir("./" + response)
            os.chdir("./" + response)
            for each in cfg.dirlist:
                os.mkdir("./" + each)
            os.chdir("info")
            cfg.dispPainting = response
            tempPainting = cfg.dispPainting

            ptgname = "My New Painting"
            ptgDate = ""
            numb = ""
            secid = ""
            wherePainted = "Klosterlechfeld Bavaria"
            vertDim = ""
            horizDim = ""
            materialsUsed = ""
            ptgDesc = ""
            gal1 = "no"
            gal2 = "no"
            gal3 = "no"
            gal4 = "no"
            gal5 = "no"
            picLR = "no pic"
            picHR = "no Pic"

            mydata = {
                cfg.dispPainting: {
                    "pname": ptgname,
                    "wherePainted": wherePainted,
                    "secid": secid,
                    "mysite": gal1,
                    "buzz": gal2,
                    "deviant": gal3,
                    "saatchi": gal4,
                    "soc6": gal5,
                    "number": numb,
                    "secid": secid,
                    "year": ptgDate,
                    "dims": vertDim,
                    "hDims": horizDim,
                    "desc": ptgDesc,
                    "materials": materialsUsed,
                    "locLRfoto": picLR,
                    "locHRfoto": picHR,
                }
            }
            jsonData = json.dumps(
                mydata, sort_keys=True, indent=4, separators=(",", ": ")
            )
            print(os.getcwd())
            filename = cfg.dispPainting + ".json"
            with open(filename, "w") as f:
                f.write(jsonData)
            # self.OpenFile(event = "none",opt = cfg.myworkingFolder)
            cfg.currentCat = tmpcat
            cfg.dispPainting = tempPainting
            self.dispData()

    # ++++++++++++++++++++++++++++++++++++++++++++++++    #WORKING
    def AddNewSubFolder(self, event):
        self.SetStatusText("Add a new catagory to database")
        dlg = wx.TextEntryDialog(
            None, "What is the new catagory named", "Name of new folder", "new_folder"
        )
        if dlg.ShowModal() == wx.ID_OK:
            response = dlg.GetValue()
            os.chdir(cfg.myworkingFolder)
            os.mkdir(response)
        dlg.Destroy()
        self.OpenFile(event="none", opt=cfg.myworkingFolder)

    # ++++++++++++++++++++++++++++++++++++++++++++++++
    # should be working watch for bugs
    def onSavePainting(self, event):

        self.SetStatusText("Saving painting data to json file")
        ptgname = self.t1.GetValue()
        ptgDate = self.t2.GetValue()
        numb = self.t2a.GetValue()
        secid = self.t2b.GetValue()
        wherePainted = self.t3.GetValue()
        vertDim = self.t4.GetValue()
        horizDim = self.t5.GetValue()
        materialsUsed = self.t6.GetValue()
        ptgDesc = self.t7.GetValue()
        gal1 = self.t10.GetValue()
        gal2 = self.t11.GetValue()
        gal3 = self.t12.GetValue()
        gal4 = self.t13.GetValue()
        gal5 = self.t14.GetValue()
        picLR = self.photo_txt.GetLabel()
        picHR = self.photo_HRtxt.GetLabel()

        mydata = {
            cfg.dispPainting: {
                "pname": ptgname,
                "wherePainted": wherePainted,
                "secid": secid,
                "mysite": gal1,
                "buzz": gal2,
                "deviant": gal3,
                "saatchi": gal4,
                "soc6": gal5,
                "number": numb,
                "secid": secid,
                "year": ptgDate,
                "dims": vertDim,
                "hDims": horizDim,
                "desc": ptgDesc,
                "materials": materialsUsed,
                "locLRfoto": picLR,
                "locHRfoto": picHR,
            }
        }
        jsonData = json.dumps(mydata, sort_keys=True, indent=4, separators=(",", ": "))
        os.chdir(
            cfg.workingDir + "/" + cfg.currentCat + "/" + cfg.dispPainting + "/info"
        )
        filename = cfg.dispPainting + ".json"
        with open(filename, "w") as f:
            f.write(jsonData)

    # ++++++++++++++++++++++++++++++++++++++++++++++++
    # SHOULD BE WORKING
    def MakeListAllWorks(self, event):
        self.SetStatusText("Make a list of all works")
        makeList()

    # ++++++++++++++++++++++++++++++++++++++++++++++++
    def CreateAllSubfolders(self, event):
        self.SetStatusText("Create all subfolders, not normally used")
        createAllSubfolders()

    # ++++++++++++++++++++++++++++++++++++++++++++++++
    # Should be working not tested yet
    def MoveFotosToFolders(self, event):
        self.SetStatusText(
            "Move all fotos in a picture folder to correct picture folders"
        )
        moveAllPhotos()

    # ++++++++++++++++++++++++++++++++++++++++++++++++
    # WORKING
    def ColateAllInfoSheets(self, event):
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

    # ++++++++++++++++++++++++++++++++++++++++++++++++
    def RenameAllFotosPicDateNum(self, event):
        self.SetStatusText("Rename all fotos to name date index")
        renameFotos()

    # ++++++++++++++++++++++++++++++++++++++++++++++++
    def DisplayWork(self, event):
        self.SetStatusText("Display a work")

    # ++++++++++++++++++++++++++++++++++++++++++++++++
    def GetHelp(self, event):
        self.SetStatusText("Help")

    # ++++++++++++++++++++++++++++++++++++++++++++++++
    def SetPreferences(self, event):
        self.SetStatusText("Set up preferences")

    # ++++++++++++++++++++++++++++++++++++++++++++++++
    def MakeMd(self, event):
        filename = cfg.dispPainting + ".md"
        output_filename = cfg.dispPainting + "lr.pdf"
        ptgname = self.t1.GetValue()
        ptgDate = self.t2.GetValue()
        wherePainted = self.t3.GetValue()
        vertDim = self.t4.GetValue()
        horizDim = self.t5.GetValue()
        materialsUsed = self.t6.GetValue()
        ptgDesc = self.t7.GetValue()
        thepic = self.photo_txt.GetLabel()

        max_size = 900
        im = Image.open(thepic)
        W, H = im.size
        if W > H:
            NewW = max_size
            NewH = max_size * H / W
        else:
            NewH = max_size
            NewW = max_size * W / H
        im = im.resize((int(NewW), int(NewH)), Image.LANCZOS)
        im.save("temppic.jpg", "JPEG")
        thetemp = cfg.workingDir + "/info/temppic.jpg"

        data = (
            ' <body style="background-color: white !important;"><img src ='
            + thetemp
            + " >\n\n"
            + ptgname
            + "\n\n"
            + ptgDate
            + "\n\n"
            + wherePainted
            + "\n\n"
            + vertDim
            + "  *  "
            + horizDim
            + "\n\n"
            + materialsUsed
            + "\n\n"
            + ptgDesc
        )

        print(os.getcwd())
        with open(filename, "w") as f:
            f.write(data)
        f.close()

        with open(filename, "r") as f:
            # could be a problem here, not sure.
            testfile = markdown(f.read(), output_format="html4")
        pdfkit.from_string(testfile, output_filename)
        f.close()

    # ++++++++++++++++++++++++++++++++++++++++++++++++
    # WORKING
    def PrevPainting(self, event):
        cfg.ptngIndex -= 1
        if cfg.ptngIndex < 0:
            cfg.ptngIndex = cfg.totalPtngs - 1
        # load new painting
        cfg.dispPainting = cfg.listPtngs[cfg.ptngIndex]
        self.dispData()
        self.SetStatusText("Back one painting")

    # ++++++++++++++++++++++++++++++++++++++++++++++
    # WORKING
    def NextPainting(self, event):
        cfg.ptngIndex += 1
        if cfg.ptngIndex > (cfg.totalPtngs - 1):
            cfg.ptngIndex = 0
        # load new painting
        cfg.dispPainting = cfg.listPtngs[cfg.ptngIndex]
        self.dispData()
        self.SetStatusText("Forward one painting")

    # +++++++++++++++++++++++++++++++++++++++++++++++++++
    # WORKING
    def PrevCat(self, event):
        cfg.catIndex -= 1
        if cfg.catIndex < 0:
            cfg.catIndex = cfg.totalSubs - 1
        cfg.currentCat = cfg.listSubs[cfg.catIndex]
        cfg.listPtngs = cfg.mylibOfSubPaintings["list_of_cat_and_paintings"][
            cfg.currentCat
        ]
        cfg.totalPtngs = len(cfg.listPtngs)
        cfg.dispPainting = cfg.listPtngs[0]
        self.dispData()

    ####++++++++++++++++++++++++++++++++++++++++++++++++
    # WORKING
    def NextCat(self, event):
        cfg.catIndex = cfg.catIndex + 1
        if cfg.catIndex > (cfg.totalSubs - 1):
            cfg.catIndex = 0
        cfg.currentCat = cfg.listSubs[cfg.catIndex]
        cfg.listPtngs = cfg.mylibOfSubPaintings["list_of_cat_and_paintings"][
            cfg.currentCat
        ]
        cfg.totalPtngs = len(cfg.listPtngs)
        cfg.dispPainting = cfg.listPtngs[0]
        self.dispData()


##################################################################################
class App(wx.App):
    def OnInit(self):
        self.frame = mainMenu(parent=None, id=-1)
        self.frame.Center()
        self.frame.Show()
        self.frame.Fit()
        self.SetTopWindow(self.frame)
        return True


##################################################################################
if __name__ == "__main__":
    app = App()
    app.MainLoop()
##################################################################################
