import tkinter as tk
 
# Membuat jendela utama
root = tk.Tk()
root.title("Aplikasi Multimedia")

from PIL import Image, ImageTk

# Memuat image menggunakan Pillow
image = Image.open('gambar.jpg')
image = image.resize((400, 300), Image.LANCZOS)
photo = ImageTk.PhotoImage(image)

# Membuat label untuk menampilkan gambar
label = tk.Label(root, image=photo)
label.pack()

# Menjalankan perulangan acara Tkinter
root.mainloop()