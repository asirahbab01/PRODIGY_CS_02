from tkinter import *
from tkinter import filedialog

root=Tk(className='Image encryption tool')
root.geometry("200x150")
root.configure(bg='light blue')

def encrypt_image():
    f1=filedialog.askopenfile(mode='r',filetypes=[('jpg file','*.jpg'),('png file','*.png')])
    if f1 is not None:
        #print(f1)  
        f1_name=f1.name  #Removing Textwrapper.io & extracting the writing inside the angle bracket--Location of the image.
        #print(f1_name)
        key=e1.get(1.0,END)
        print("The image location is: ",f1_name)
        print('Note : Encryption key and Decryption key must be same.')
        print("The value of key is: ",key)
        fi=open(f1_name,'rb')    #Read the data in binary format
        image=fi.read()
        fi.close()
        image=bytearray(image)   #converting pixel intensities into byte values.
        for index,values in enumerate(image):
            image[index]=values^int(key)         ##Encryption
        fi1=open(f1_name,'wb')
        fi1.write(image)                        ##Decryption
        fi1.close()
        

b1=Button(root,text="encrypt/decrypt",command=encrypt_image)
b1.place(x=45,y=60)

e1=Text(root,height=1,width=15)    #Here key value is minimum 1. No value below 1 is considered as a valid key.
e1.place(x=20,y=30)

root.mainloop()
print("Operation done!!")