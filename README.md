art management program

NOTE: this is still in development. As an assist to all possible developers, I have included all files that I have created in the debian package.NOTE: this is still in development. As an assist to all possible developers, I have included all files that I have created in the debian package.  

a python GUI program to manage a artists or photographers work / protfolio of work and data that goes with it. 

this program helps artists and fotographers manage a file system that contains pictures of finished works, and data about these works. it uses python 3.5 and wxPython 4.0 to create a gui interface that makes management of the system easy and straightforward.

every artist needs a file system to manage photographs of their work, data about their works (size, materials, descriptions, dates prices galleries etc) and to create catalogs ( here in pdf format) for distrbution to fans, galleries and interested parties.  this program automates the whole process,savng the artist many hours of tedious work that isnt really art related.

as of 18 January 2020 this program has basic functionality. you can

   create databases 
   
   create new paintings (ie a json file which displays on the screen the data about the painting)
   
   store data about the paintings in json files
   
   scroll thru your collection of data
   
   sort fotos into folders based on type ( basic level of sorting)
   
   organize paintings into sub catagories
  
   set the system up to display a foto of your painting with the data
   
   create pdfs from the .md sheet
   
   
still to do:
   
   create a method that automatically does file system set up for the user
    
   change output directory of pdf to painting.info
   
possibly in the future:
   
   system that automatically produces catalogs of work as set up by the artist for shows, fairs advertising etc.
   
   right now, 18 jan 2020 I am using the program and debuging it, I hope to release it as a python PyPl program by feb 1 2020, so that others can use it as well.
   
UPDATE:
 1 may 2020: most of the serious debugging is done. if you alter the json files by hand in painting/info files you are going to have problems if anything is wrong. right now there is no check for correctness of json files. all the other functions are working. also when you create a new painting the program will take you to that painting so you can immediately enter data. 

   if anyone would like to help, im planning on releasing this to the pypl repository in a few weeks when i get some more functionality in , as a shareware/ freeware software tool for artists. im looking for people to help with writing the program, documentation, and suggesting new features etc. you can contact me here if you are interested.
   
   please note that i run this using the anaconda python install on my computer and used anaconda to install wxPython. I have problems installing using pip and pip3. any thoughts on this would be welcome. 
   
   once again i have just tried to install wxpython on my system and it failed, i can only get it to work inside the anaconda virtual envronment any leads or thoughts on how to fix this would be greatly appreciated. i was trying to build a debian package for this but the wx python dependency remains a major problem. 

8 june 2020 wxPython install problems SOLVED!
this is a complex subject, and ill write more later, but go to these 2 webpages for solutions on most linux systems. it should not be a problem on windows or mac.

https://wxpython.org/blog/2017-08-17-builds-for-linux-with-pip/index.html
https://wxpython.org/pages/downloads/

a list of pip wheels that work can be found at

https://extras.wxpython.org/wxPython4/extras/linux/gtk3/

read the above info (first 2 sites) then poke around the last one, if you are running ubuntu, fedora, debian, or centos.

Known Problems:
	if you have bad json files for any reason the program will not start up correctly. also if the subfiles in each painting file arent correct you will also have problems. eventually Ill fix this but it is not a priority, as this is a very part time project for me. if you fork and develop/modify/fix etc i would bevery happy, and will add you to the development team and README as a contact.

dependancies:
	wxpython 4.0 or greater (python 3 compatible)
	markdown
	PIL
	pdfkit
	
	wkhmtltopdf.deb (you can use apt to install)

 can contact me at jfs@tandkcybernetics.christopherrehm.de for more info.
   
   
   
