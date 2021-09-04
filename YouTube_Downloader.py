# -----------------------Modules used----------------------- #
from tkinter import *
from pytube import *
from tkinter.filedialog import *
from threading import *
from tkinter import messagebox
from tkinter import ttk
# -------------------------------------------------------------
download_path = None
# The pytube functions 

# ------------------------This function is to ask user to select the location where he/she want to download the video---------------------------
def get_path():
    global download_path
    download_path = askdirectory()

def pop_up_message():
    messagebox.showwarning("", "Select location")

def else_message():
    message.config(text="Enter a valid URL", fg="red")
    message.place(x=355,y=360)
    download_button.config(state=NORMAL)

def progress_bar():
    stats = ttk.Progressbar(root, orient=HORIZONTAL, length=400, mode="determinate")
    stats.place(x=227,y=360)

# --------------This is the main functionality which reads the URL, manipulates on the URL and finally downloades the video to the system-----------
def download_process():
    try:
        download_button.config(state=DISABLED)
        if(len(url.get())>0):
            url_name = YouTube(url.get())
            url_object = url_name.streams.get_by_itag("18")
            url_object.download(download_path)
            url.delete(0, END)
            message.config(text="Video downloaded successfully !!!", fg="darkgreen")
            message.place(x=285,y=360)
            download_button.config(state=NORMAL)
                
        else:
           else_message() 
    except:
        message.config(text="Couldnt download this video, Enter a valid URL", fg="red")
        message.place(x=220,y=360)
        download_button.config(state=NORMAL)

#-------------------------It runs the main function in a seperate thread so the gui is not interrupted-------------------------------------
def thread_function():
    thread_one = Thread(target=download_process)
    thread_one.start()
# ---------------------------------------------------------------------------------------------------------------------------------------------------

def one():
    if download_path==None and len(url.get())==0:
        else_message()
    elif download_path==None:
        pop_up_message()
    else:
        thread_function()
# --------------------------------The GUI Interface------------------------------------------
root = Tk()
root.iconbitmap("yt_icon_.ico")
root.title("YouTube Downloader")
root.minsize(850,500)
root.maxsize(850,500)

yt_pic = PhotoImage(file = "youtube.png")
yt_pic2 = Label(image = yt_pic)
yt_pic2.place(x=235,y=20)

Downloader = Label(root, text="Downloader", fg="red", font=("Montserrat",32))
Downloader.place(x=375,y=55)

url = Entry(width=50, font=("Montserrat",12) ,borderwidth=1)
url.place(x=200,y=240)

Enter_url = Label(root, text="Enter the URL : ", font=("Montserrat",11))
Enter_url.place(x=90,y=240)

download_button = Button(root,width=12 ,height=1 , text="Download", font=("Montserrat",14) ,relief="groove", bg="#3A2E2E", fg="white", borderwidth=1, command=one)
download_button.place(x=360,y=290)

location = Button(root, text="Select location", font=("Montserrat",10) ,relief="groove", fg="black", borderwidth=2, command=get_path)
location.place(x=660,y=237)

message = Label(text="Video downloaded successfully !!!", font=("Montserrat",14), fg="#33DE08")
download_button.config(state=NORMAL)  

root.mainloop()
# ----------------------------------------------------------------------------------------------
