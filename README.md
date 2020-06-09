Art Portfolio Management Program

NOTE: This is still in development. As an assist to all possible developers, I have included all files that I have created in the debian/ubuntu/linux mint 18.1 environment.

As of now you have to manually create the basic file structure on your system before you start using it. I plan on having that fixed by 13 June 2020, so that you are guided thru a menu system to set up the first time.

This is a python GUI program to manage a artists or photographers work / protfolio of work and data that goes with it. 

This program helps artists and fotographers manage a file system that contains pictures of finished works, and data about these works. it uses python 3.5 (min) and wxPython 4.0 to create a gui interface that makes management of the system easy and straightforward.

Every artist needs a file system to manage photographs of their work, data about their works (size, materials, descriptions, dates prices galleries etc), and to create catalogs ( here in pdf format) for distrbution to fans, galleries and interested parties.  This program automates the whole process,savng the artist many hours of tedious work that isnt really art related.

As of 18 January 2020 this program has basic functionality. You can

   Create databases 
   
   Create new paintings (ie a json file which displays on the screen the data about the painting)
   
   Store data about the paintings in json files
   
   Scroll thru your collection of data
   
   Sort fotos into folders based on type ( basic level of sorting)
   
   Organize paintings into sub catagories
  
   Set the system up to display a foto of your painting with the data
   
   Create pdfs from the .md sheet
   
   
Still to do:
   
   Create a method that automatically does file system set up for the user
    
   Change output directory of pdf to painting.info
   
Possibly in the future:
   
   System that automatically produces catalogs of work as set up by the artist for shows, fairs advertising etc.
   
   Right now, 18 Jan 2020 I am using the program and debuging it, I hope to release it as a python PyPi program by 1 Feb 2020, so that others can use it as well.
   
UPDATE:
 1 May 2020: Most of the serious debugging is done. If you alter the json files by hand in painting/info files you are going to have problems if anything is wrong. Right now there is no check for correctness of json files. All the other functions are working. Also when you create a new painting the program will take you to that painting so you can immediately enter data. 

   If anyone would like to help, im planning on releasing this to the PyPi repository in a few weeks when I get some more functionality in , as a shareware/ freeware software tool for artists. Im looking for people to help with writing the program, documentation, and suggesting new features etc. You can contact me here if you are interested.
   
   Please note that I run this using the Anaconda python install on my computer and used Anaconda to install wxPython. 

UPDATE:
8 June 2020 wxPython install problems SOLVED!
Ok so this problem is solved. this will work easily if you install anaconda and the dependencies listed below. if you do not want to install anaconda then you will have to install all of the dependencies  either using pip3 or apt. My recommendation is to use pip3 to install the dependencies and get the program up and running. if you use apt or apt-get there may well be problems installing wxPython as wxPython requires non standard high level libraries to function. On linux systems this is a problem due to the variance in different linux systems and what is installed. Please see more info below.

INSTALL on Windows:
This is not tested and will not work without rewriting some of the code that deals with file handling in the program. if you are a python windows programmer and would like to help on this please contact me.
this is a complex subject, and ill write more later, but go to these 2 webpages for solutions on most linux systems. it should not be a problem on windows or mac.

INSTALL on macOS:
This is untested, as macOS is a linux based project it may or may not work. Again a programmer in this area would be gladly welcome to assist on porting this project.

INSTALL on Linux Unbuntu or Linux Mint:
Run the following commands to install the dependencies the program requires:

pip3 install markdown

pip3 install pillow

pip3 install pdfkit

pip3 install wkhtmltopdf

pip3 install -U -f https://extras.wxpython.org/wxPython4/extras/linux/gtk3/ubuntu-18.04 wxPython

Note that there are wheels already set up for ubuntu, fedora, debian and centos, at the site below.

https://extras.wxpython.org/wxPython4/extras/linux/gtk3/

Change your pip install as needed to reflect what you are trying to do.

If you have some other version of linux you will have to build wxpython from sources. Follow the links below to learn more about this:

https://wxpython.org/blog/2017-08-17-builds-for-linux-with-pip/index.html

https://wxpython.org/pages/downloads/


Note: I have a slightly different version of the program running outside of conda.
Im therefore setting up two folders, a conda version and a non conda version. 


Known Problems:
	If you have bad json files for any reason the program will not start up correctly. Also if the subfiles in each painting file arent correct you will also have problems. Eventually Ill fix this but it is not a priority, as this is a very part time project for me. If you fork and develop/modify/fix etc I would bevery happy, and will add you to the development team and README as a contact.

Dependencies:
	wxpython 4.0 or greater (python 3 compatible)
	
	markdown
	
	pillow (or in some systems PIL)
	
	pdfkit
	
	wkhtmltopdf
	
	or
	
	wkhmtltopdf.deb (you can use apt to install)

you can contact me at jfs@tandkcybernetics.christopherrehm.de for more info.
I am always willing to help as much as I can if you contact me. 
   
   
   
