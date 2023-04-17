from tkinter import *
import tkinter.messagebox
from pygame import mixer
from tkinter import filedialog
import os

root = Tk()  #Tk function actually create window and storing this window in root varriable

mixer.init()   #initializing the mixer

# root.geometry('200x200')
root.title("Music Player")

#icon
root.iconbitmap(r'Image/musicicon.ico')

#texting
filelabel = Label(root, text = 'Lets rock on!!!')
filelabel.pack(pady=10)

middleframe = Frame(root)
middleframe.pack(padx=30, pady =30)

#play button
def show_detail():
    filelabel['text'] = 'Playing' + '  -  ' + os.path.basename(file_name)
    a = mixer.Sound(file_name)

def play_music():
    global paused

    if paused:
        mixer.music.unpause()
        statusbar['text'] = 'Music Resumed'
        paused = FALSE

    else:
        try:
            mixer.music.load(file_name)
            mixer.music.play()
            # print("Hey! it works well.")
            statusbar['text'] = 'Playing Music' + '  -  ' + os.path.basename(file_name)
            show_detail()
        except:
            tkinter.messagebox.showinfo('Music Player', "FILE NOT FOUND.")

play_photo = PhotoImage(file='Image/play3.png ')
play_button = Button(middleframe, image = play_photo, command = play_music)
play_button.grid(row = 0,column =0)

#Pause Button
paused = FALSE

def pause_music():
    global paused
    paused = TRUE
    mixer.music.pause()
    statusbar['text'] = 'Music paused'

pause_photo= PhotoImage(file = 'Image/pause-button.png')
pause_button = Button(middleframe, image = pause_photo, command = pause_music)
pause_button.grid(row = 0,column =1)

#stop button
def stop_music():
    mixer.music.stop()
    statusbar['text'] = 'Music stopped'

stop_photo = PhotoImage(file = 'Image/stop-button2.png')
stop_button = Button(middleframe, image = stop_photo, command = stop_music)
stop_button.grid(row = 0,column = 2)

#bottom frame for volume ,mute rewind etc.
buttomframe = Frame(root)
buttomframe.pack(padx=10, pady =10)

#Rewind button
def rewind_music():
    play_music()
    statusbar['text'] = 'Music Rewinded'

rewind_photo = PhotoImage(file = 'Image/rewind.png')
rewind_button = Button(buttomframe, image = rewind_photo, command= rewind_music)
rewind_button.grid(row = 0,column =0)

#mute and volume button
muted  = FALSE
def mute_music():
    global muted
    if muted:   #Unmuted the music'
        volume_button.configure(image=volume_photo)
        volupdown.set(55)
        mixer.music.set_volume(0.5)

        muted = FALSE

    else:     #muted the music
        volume_button.configure(image=mute_photo)
        volupdown.set(0)  # set the volume to 0
        mixer.music.set_volume(0)

        muted = TRUE

mute_photo = PhotoImage(file = 'Image/mute.png')
volume_photo = PhotoImage(file = 'Image/volume.png')
volume_button = Button(buttomframe, image = volume_photo, command= mute_music)
# mute_button = Button(buttomframe, image = mute_photo, command= mute_music)
volume_button.grid(row = 0,column =1)

#volume up and down
def set_volume(val):
    volum = int(val) / 100
    mixer.music.set_volume(volum)    #set volume of mixer only from 0 to 1. example = 0.1 , 0.55,0.54, 1 etc

volupdown = Scale(buttomframe, from_ = 0, to = 100 , orient=HORIZONTAL, command = set_volume)
volupdown.set(55) #default value of music player
mixer.music.set_volume(0.5)
volupdown.grid(row = 0, column = 2, pady=15)

#create the menubar
menubar = Menu(root)
root.config(menu = menubar)

#create the sub menu
def browse_file():
    global file_name
    file_name = filedialog.askopenfilename() #this askopenfilename actually open your device files
    # print(file_name)

submenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu =submenu)
# menubar.add_cascade(label="Edit", menu =submenu)
submenu.add_command(label="Open",command = browse_file)
submenu.add_command(label="Exit", command = root.destroy)

def about_us():
    tkinter.messagebox.showinfo('Music Player','This is the infomation that we want.')

submenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu =submenu)
submenu.add_command(label="About us",command = about_us)

#Status bar
statusbar = Label(root, text = "Welcome to Music Player", relief= SUNKEN, anchor= W)
statusbar.pack(side = BOTTOM, fill = X)

root.mainloop()    #putting the window in infinite loop by writing root.mainloop()
