import random
from tkinter import *
import pyperclip
"""""
AUTHOR = ABADHİSTORY
HUB-DSZ
"""""

#function that makes the sentences, output them and
#save them to the clipboard



def display2 ():
    global my_label
    textboxcontents = textbox.get("1.0", "end")
    my_list = []
    for letter in textboxcontents:
        randnum = random.randint(1, 2)
        if randnum % 2 == 0:
            my_list.append(letter.upper())
        else:
            my_list.append (letter.lower())
    str1 = ''.join(my_list)
    my_label = Label(root,text = str1,font = 'Helvetica 10 bold')
    my_label.place(x = 375 ,y = 70 )
    pyperclip.copy(str1)



#text deleting function
def destroy ():
    my_label.destroy()
    textbox.delete("1.0","end")


root = Tk()
root.geometry("700x250")

#clear button
clear_button = Button(root,text = "clear\n text ",command = destroy)
clear_button.place(x = 260, y = 70 , width = 40 ,height = 50)

#the main titles position
title = Label(root,text ="Mocking SpongeBob" ,font='Helvetica 12 bold')
title.place (x = 220,y = 0)

#text box's title
txttitle = Label (root,text ="Enter text ")
txttitle.place (x = 120,y = 25)

#output title
outputtitle = Label(root,text = "Program output")
outputtitle.place(x = 435,y = 25)


#the text box
textbox  = Text (root,font ='Helvetica 10 bold' )
textbox.place(x = 50, y = 50, height = 135, width = 200)

#note label
note_label = Label(root ,text = "note :the outputs are automatically\n saved to your clipboard")
note_label.place(x= 260 , y = 200)
#button

generate= (Button(root,text = "generate",command = display2)).place(x = 120 ,y = 200,height = 35 , width = 60)


root.mainloop()















