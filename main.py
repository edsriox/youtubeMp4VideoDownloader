from tkinter import font
from tkinter.constants import ANCHOR
from pytube import YouTube
import tkinter as t 
import time 

zaman = time.localtime() #Login Time
lasttime = "%d/%d/%d %d:%d" % (zaman[0] , zaman[1] , zaman[2] , zaman[3] , zaman[4] )

langselect = t.Tk()
langselect.geometry("300x300")
langselect.title("Youtube Video Downloader")
centerframe = t.Frame(langselect , height=300 , width=300 , bg = "snow")
centerframe.pack()
titlelab = t.Label(centerframe , text = "Choose Language" , fg = "gray20" , font = "ariel 18 bold" , bg= "snow")
titlelab.place(x = 5 , y = 6)
selection = t.Listbox(centerframe,  bg = "gray20" , fg = "snow" ,  height=2 , width=13 , font="ariel 20 bold")
selection.insert(1 , "English")
selection.insert(2 , "Turkish(XX)") 
selection.place(x = 50 , y = 80)
selected1 = selection.get(first=1)
def windowmain():
    
    
    if selected1 == selection.get(first=1): #There is a mistake , 'selected1' defined for app can run.(The Problem will solve soon.)
        langselect.destroy()
        windowtr = t.Tk()
        windowtr.geometry("500x500")
        windowtr.title("Youtube Video Downloader  [ Language : English ]")
        frameC = t.Frame(windowtr , height=500 , width=500 , bg = "gray64")
        frameC.pack()
        infolab = t.Label(frameC , text = "Paste Link" , bg = "gray64" , fg = "black" , font="ariel 16 bold")
        infolab.place(x=175 , y= 130)
        link = t.StringVar()
        E1 = t.Entry(frameC , fg = "black" , font= "ariel 15 bold" , width=35 , textvariable=link)
        E1.place(x = 70 , y = 170 )
        devinfo = t.Label(frameC , text = " \t developed by Ege Demiraslan \n \t Copyright 2021 November , Thnks For Using! " , fg = "gray20" , bg = "gray64" , font = "ariel 12 bold")
        devinfo.place(x = 9 , y = 430)     
        entertime = t.Label(frameC , text= lasttime , fg = "gray20" , bg = "gray64" , font = "ariel 13 bold")
        entertime.place(x = 110 , y = 5)   
        enterinfo = t.Label(frameC , text= "Login Time :" , fg = "gray20" , bg = "gray64" , font = "ariel 13 bold")
        enterinfo.place(x =6 , y = 5)
        def downloader():
            url =YouTube(str(link.get()))
            video = url.streams.first()
            video.download()
           
            completedLab = t.Label(frameC , bg = "spring green" , fg = "gray20" , font = "ariel 13 bold"  , text = "Uygulamanın Kurulu Olduğu Klasöre Başarıyla İndirilmiştir!")
            completedLab.place(x= 10 , y = 290)
          
        downloadbtn = t.Button(frameC , text = "Download" , font = "ariel 16 bold" , bg = "black" , fg = "snow" , width = 10 , command=downloader)
        downloadbtn.place(x = 180 , y = 230)
        windowtr.mainloop()
    else:
        if selection == selection.get(first=2): #Here isn't running now!
            langselect.destroy()
            windowen = t.Tk()
            windowen.geometry("500x500")
            windowen.title("Youtube Video Downloader  [ Dil : Türkçe ]")
            frameC = t.Frame(windowen , height=500 , width=500 , bg = "gray64")
            frameC.pack()
            infolab = t.Label(frameC , text = "Linki Yapıştırın" , bg = "gray64" , fg = "black" , font="ariel 16 bold")
            infolab.place(x=175 , y= 130)
            link = t.StringVar()
            E1 = t.Entry(frameC , fg = "black" , font= "ariel 15 bold" , width=35 , textvariable=link)
            E1.place(x = 70 , y = 170 )
            def downloader2():
                url =YouTube(str(link.get()))
                video = url.streams.first()
                video.download()
           
            completedLab = t.Label(frameC , bg = "spring green" , fg = "gray20" , font = "ariel 13 bold"  , text = "Uygulamanın Kurulu Olduğu Klasöre Başarıyla İndirilmiştir!")
            completedLab.place(x= 10 , y = 290)
            downloadbtn = t.Button(frameC , text = "İndir" , font = "ariel 16 bold" , bg = "black" , fg = "snow" , width = 10 , command=downloader2)
            downloadbtn.place(x = 180 , y = 230)
        
            windowen.mainloop()
        
nextbtn = t.Button(centerframe , text=">" , font="ariel 22 bold" , fg = "gray20" , bg = "gray64" ,  command=windowmain , width=5)
nextbtn.place(x = 94 , y = 170  )
langselect.mainloop()