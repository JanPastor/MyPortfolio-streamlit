import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap import Style
from ttkbootstrap.constants import *


# Set up main window
window = ttk.Window(themename= 'lancer_lumineer')
window.geometry('1900x1080')
window.minsize(400,300)
window.title('Lancer Lumineer ROV Control System')
icon_path = 'Tkinter_Lancer_Lumineer\ROV_images\image1.ico'
window.iconbitmap(icon_path)

# Layout (Grid Method)

# Widgets
meter1 = ttk.Meter(master= window,
                   metersize= 180,
                   padding = 5, 
                   amountused= 0,
                   metertype= 'semi',
                   subtext= 'Left Forward Thrust',
                   bootstyle= PRIMARY,
                   interactive= True,
                   stripethickness= 10,
                   amounttotal= 1900,
                   textright= 'us',
                   stepsize= 100
                   )
meter2 = ttk.Meter(master= window,
                   metersize= 180,
                   padding = 5, 
                   amountused= 0,
                   metertype= 'semi',
                   subtext= 'Right Forward Thrust',
                   bootstyle= PRIMARY,
                   interactive= True,
                   stripethickness= 10,
                   amounttotal= 1900,
                   textright= 'us',
                   stepsize= 100
                   )
meter1.pack(side= 'left', pady= 10, padx= 10, anchor= 'nw')
meter2.pack(side= 'left',pady= 10, padx= 10, anchor = 'nw')

# Main loop
window.mainloop()