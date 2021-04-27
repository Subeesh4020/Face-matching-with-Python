import tkinter as tk
from tkinter import filedialog
from tkinter import Image, Image, ttk
import numpy as np
import face_recognition as fr
from PIL import Image, ImageDraw, ImageTk
import filetype as ft

global Width, Height

def FileUpload1(event = None):
   filename = filedialog.askopenfilename()
   Img1 = Image.open(filename)
   Imggrp = ImageTk.PhotoImage(Img1) # 660 x 554
   ImgWidth = Imggrp.width()
   ImgHeight = Imggrp.height()
   if(ImgWidth > 660):
      Img1 = Img1.resize((660, ImgHeight))
      ImgWidth = 660

   if(ImgHeight > 554):
      Img1 = Img1.resize((ImgWidth, 554))

   Imggrp = ImageTk.PhotoImage(Img1) # Allowed image size 660 x 554
   left_label.config(image = Imggrp)
   left_label.image = Imggrp
   flnameleft_label.config(text = filename)
   
   
   
def FileUpload2(event = None):  
   filename = filedialog.askopenfilename()
   Img1 = Image.open(filename)
   Imggrp = ImageTk.PhotoImage(Img1) # 660 x 554
   ImgWidth = Imggrp.width()
   ImgHeight = Imggrp.height()
   if(ImgWidth > 660):
      Img1 = Img1.resize((660, ImgHeight))
      ImgWidth = 660

   if(ImgHeight > 554):
      Img1 = Img1.resize((ImgWidth, 554))

   Imggrp = ImageTk.PhotoImage(Img1) # 660 x 554   
   right_label.config(image = Imggrp)
   right_label.image = Imggrp
   flnameright_label.config(text = filename)


def Start_Scan(event = None):
   count = 0
   Img_Search = fr.load_image_file(flnameleft_label.cget("text"))
   faces_left = fr.face_locations(Img_Search)
   Img_Search_Encd = fr.face_encodings(Img_Search, faces_left)

   Img_To_Match = fr.load_image_file(flnameright_label.cget("text"))
   faces_right = fr.face_locations(Img_To_Match)
   Img_To_Match_Encd = fr.face_encodings(Img_To_Match, faces_right)
   left_face_num = len(faces_left)
   right_face_num = len(faces_right)
   for inx1 in range(left_face_num):
      for inx2 in range(right_face_num):
         result = fr.compare_faces([Img_Search_Encd[inx1]], Img_To_Match_Encd[inx2])
         if result[0] == True:
            count = count + 1
      
   if (count == 0):
     result_label.config(text = "Mismatching")
   else:
     result_label.config(text = f"Matching - {count} times")    



rootW = tk.Tk()
Width = rootW.winfo_screenwidth()
Height = rootW.winfo_screenheight()
rootW.geometry("%dx%d" %(Width, Height))

Wicon = tk.PhotoImage(file = './images/icon2.png')
Bicon = tk.PhotoImage(file = './images/open.png')
Scan_Icon = tk.PhotoImage(file = './images/scan_document.png')

rootW.iconphoto(False, Wicon)
rootW.title('Face detector')
Upload_button1 = tk.Button(rootW, text = "Open", command = FileUpload1)
Upload_button2 = tk.Button(rootW, text = "Open", command = FileUpload2)
scan_button = tk.Button(rootW, text = "Scan", command = Start_Scan)
Upload_button1.config(image = Bicon)
Upload_button2.config(image = Bicon)
scan_button.config(image = Scan_Icon)
Upload_button1.pack()
Upload_button2.pack()
scan_button.pack()
Upload_button1.place(x = 10, y = 10)
Upload_button2.place(x = ((Width / 2) + 1), y = 10)
scan_button.place(x = 15, y = (Height - 118))

frm1 = ttk.Frame(master = rootW, width = (Width / 2), height = (Height - 200), relief = tk.RAISED, borderwidth = 1)
frm2 = ttk.Frame(master = rootW, width = ((Width / 2) - 10), height = (Height - 200), relief = tk.RAISED, borderwidth = 1)
frm1.pack(fill = tk.BOTH, side = tk.LEFT, expand = True)
frm2.pack(fill = tk.BOTH, side = tk.LEFT, expand = True)
frm1.place(x = 10, y = 70)
frm2.place(x = (Width / 2), y = 70)

left_label = tk.Label(image = None)
right_label = tk.Label(image = None)
result_label = tk.Label(image = None)
flnameleft_label = tk.Label(image = None)
flnameright_label = tk.Label(image = None)

#flnamefnd_label.config(bg = "yellow")  ####

left_label.pack()
right_label.pack()
result_label.pack()
flnameleft_label.pack()
flnameright_label.pack()

left_label.place(x = 15, y = 75)
right_label.place(x = ((Width / 2) + 4), y = 75) 
result_label.place(x = 100, y = (Height - 118))
flnameleft_label.place(x = 90, y = 40)
flnameright_label.place(x = (((Width / 2) + 4) + 80), y = 40)


rootW.mainloop()