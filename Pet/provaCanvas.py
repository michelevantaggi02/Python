from tkinter import Tk, Frame, Canvas
from PIL import ImageTk

t = Tk()
t.title("Transparency")

frame = Frame(t)
frame.pack()

canvas = Canvas(frame, bg="black", width=500, height=500)
canvas.pack()

photoimage = ImageTk.PhotoImage(file="discord1.png")
canvas.create_image(150, 150, image=photoimage)
#t.config(highlightbackground='black')
#t.overrideredirect(True)
t.wm_attributes('-transparentcolor','black')
t.mainloop()