from tkinter import Frame, Label, W, E, BOTTOM, CENTER, StringVar
import ttkbootstrap as ttk
from ttkbootstrap.constants import SUCCESS, OUTLINE

def planet():
    Planet()

class Planet(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        label = ttk.Label(self, text="Choose a Celestial Body", font=('Segoe UI', '14') )
        label.place(y=50, relx=.5, rely=0,anchor=CENTER)

        celestialBody = StringVar()
        celestialBody.set('Mars')

        BODIES = [('Mars', 'mars'), ('Earth', 'earth'), ('The Moon', 'moon'), ('Ceres', 'ceres'), ('Europa', 'europa') ]

        for index, (text, body) in enumerate(BODIES):
            rb = ttk.Radiobutton(self, text=text, variable=celestialBody, value=body, bootstyle="success")
            rb.place(y=(90 + index * 30), relx=.25, rely=0, anchor=W)

        # Continue
        button = ttk.Button(
            self, 
            text="Continue", 
            command=lambda: parent.show_frame('Command'),
            bootstyle=(SUCCESS, OUTLINE)
        )
        # 30 for headH
        button.pack(side=BOTTOM, padx=12, pady=42, anchor=E)