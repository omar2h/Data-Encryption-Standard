from tkinter import *
from key import generateKey
from text import encrypt, decrypt

root = Tk()

def showCipher():
    key = entry1.get()
    text = entry2.get()
    n = int(entry4.get())
    text = encrypt(text, key)
    for i in range(n-1):
        text = encrypt(text, key)
    label1 = Label(root, text=text)
    canvas1.create_window(200, 250, window=label1)

def showPlain():
    key = entry1.get()
    text = entry3.get()
    n = int(entry5.get())
    text = decrypt(text, key)
    for i in range(n-1):
        text = decrypt(text, key)
    label2 = Label(root, text=text)
    canvas1.create_window(200, 440, window=label2)

root.title("DES Encryption & Decryption")
canvas1 = Canvas(root, width=400, height=500)
canvas1.pack()

key_label = Label(root, text="Key")
canvas1.create_window(200, 20, window=key_label)

entry1 = Entry(root)
canvas1.create_window(200, 40, window=entry1)
entry1.focus_set()

enc_label = Label(root, text="Encryption", font='calibri 14 bold')
canvas1.create_window(200, 80,window=enc_label)

plain_label = Label(root, text="Plaintext")
canvas1.create_window(200, 110, window=plain_label)

entry2 = Entry(root)
canvas1.create_window(200, 130, window=entry2)

n2_label = Label(root, text="Number of runs")
canvas1.create_window(200,160, window=n2_label)

entry4 = Entry(root)
canvas1.create_window(200, 180, width=50, window=entry4)
entry4.insert(1,"1")

button1 = Button(text='Encrypt', command=showCipher)
canvas1.create_window(200, 220, window=button1)

dec_label = Label(root, text="Decryption", font='calibri 14 bold')
canvas1.create_window(200, 280,window=dec_label)

cipher_label = Label(root, text="Ciphertext")
canvas1.create_window(200, 310, window=cipher_label)

entry3 = Entry(root)
canvas1.create_window(200, 330, window=entry3)

n_label = Label(root, text="Number of runs")
canvas1.create_window(200,350, window=n_label)

entry5 = Entry(root)
canvas1.create_window(200, 380, width=50, window=entry5)
entry5.insert(1,"1")

button2 = Button(text='Decrypt', command=showPlain)
canvas1.create_window(200, 410, window=button2)

root.mainloop()
