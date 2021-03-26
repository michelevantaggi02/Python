import tkinter as tk
from PIL import Image as im, ImageTk as imtk


window = tk.Tk()
def chiudi(event):
    global window
    window.destroy()

img = im.open("Pet/discord1.png")
res = img.resize((100,100))
immagine = imtk.PhotoImage(res)

label = tk.Label(window,bd=0,bg='yellow', image = immagine)
label.pack()
label.bind("<Button-3>", chiudi)

window.config(highlightbackground='black')
window.overrideredirect(True)
window.wm_attributes('-transparentcolor','yellow')
window.wm_attributes("-topmost", 1)
window.geometry("+0+580")
window.mainloop()