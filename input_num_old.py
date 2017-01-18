from Tkinter import *

def entryCompNumber():
    mainRoot,res=Tk(),[None] # window
    # local function for close the window
    def callback():
        res[0]=entry.get()
        mainRoot.destroy()
    L=Label(mainRoot, text='Number of computations',fg='blue').pack() # text
    entry=Entry(mainRoot)
    entry.pack() # entry area
    entry.bind('<Return>',lambda e: callback()) # use callback, if user press Enter
    ok=Button(mainRoot, text='OK',command=callback).pack() # OK button
    mainRoot.mainloop() # pack the window
    return res[0]

Ncomp=int(entryCompNumber())
