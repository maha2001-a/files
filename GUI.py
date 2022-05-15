from ast import keyword
from tkinter import*
from tkinter import filedialog
from PIL import Image,ImageTk
from pyparsing import Word 

root=Tk()
root.title('Audio Encryption')
#root.iconbitmap('apple.ico') 
root.geometry("1000x1000")
root.configure(background='#D7BDE2')
my_label=Label(root, text='Privacy Preserving Searchable Encryption over audio files',fg='#3371FF')
def window_for_upload():
    upload=Tk()
    upload.title("Upload File")
    upload.geometry("1000x1000")
    upload.configure(background='#D7BDE2')
    my_label=Label(upload, text='File Uploading' ,fg='#3371FF')
    my_label.pack(side=TOP,padx=20,pady=50)
    def next():
        nx=Tk()
        nx.configure(background='#D7BDE2')
        nx.geometry("1000x1000")
        my_label=Label(nx,text='Enter Password to encrypt',fg='#3371FF')
        my_label.pack(side=TOP,padx=20,pady=100)
        e=Entry(nx,width=50,font=('Arial',10),fg='black')
        e.delete(0,END)
        e.pack()
        mybuttonp=Button(nx,text="Encrypt",fg='black',bg='#47F3AF')
        mybuttonp.pack(side=TOP,padx=20,pady=50)
    def browse():
        root.filename = filedialog.askopenfilename(initialdir='D:\chachu\pictures\2',title="Select File",filetypes=(("mp3 files"),("all files","*.*")))    
        next1=Button(upload,text="Next",command=next,fg='black',bg ='#F2B3EE')
        next1.pack(side=TOP,padx=10,pady=10)
    mybutton2=Button(upload,text="Browse",command=browse,fg ='black', bg ='#F2B3EE')
    mybutton2.pack() 
                       
def window_for_search():
    search=Tk()
    keyyword=StringVar
    search.title("Search Images")
    search.geometry("1000x1000")
    search.configure(background='#D7BDE2')
    my_label=Label(search, text='Image Searching' ,fg='#3371FF')
    my_label.pack(side=TOP,padx=20,pady=50)
    my_labels1=Label(search,text='Enter word to search in audio')
    my_labels1.pack(side=TOP,padx=20,pady=5)
    s1=Entry(search,textvariable=keyyword,font=('Arial',10),fg='black')
    s1.delete(0,END)
    s1.pack(side=TOP,padx=20,pady=5)
    my_labels3=Label(search,text='Enter password to decrypt')
    my_labels3.pack(side=TOP,padx=20,pady=5)
    s3=Entry(search,font=('Arial',10),fg='black')
    s3.delete(0,END)
    s3.pack(side=TOP,padx=20,pady=5)
    mybuttons=Button(search,text="search",fg ='black', bg ='#47F3AF')
    mybuttons.pack(side=TOP,padx=20,pady=15)
    
    
    
mybutton=Button(root,text= "Upload Audio",command=window_for_upload,fg ='black', bg ='#F2B3EE',padx=30,pady=30)
my_label3=Label(root,text='OR')
mybutton3=Button(root,text= "Search Audio",command=window_for_search,fg ='black', bg ='#F2B3EE',padx=30,pady=30)
img1=ImageTk.PhotoImage(Image.open("image.jpg"))
labelm=Label(root,image=img1)
labelm.pack(side=TOP, padx=20,pady=70)
my_label.pack()
mybutton.pack(side=TOP, padx=20, pady=10)
my_label3.pack(side=TOP,padx=20,pady=10)
mybutton3.pack(side=TOP, padx=20, pady=10)



root.mainloop()
