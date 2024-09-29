import tkinter as tk
from tkinter import filedialog
from pydub import AudioSegment
import subprocess
import tempfile
import os

# Membuat jendela utama
root = tk.Tk()
root.title("Musik Player")

# Definisikan fungsi untuk memutar musik
def play_music():
    file_path = filedialog.askopenfilename()
    if file_path:
        audio = AudioSegment.from_file(file_path)
        
        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp_audio_file:
            temp_file_path = temp_audio_file.name
            audio.export(temp_file_path, format="wav")
        
        # Memutar audio dengan ffplay
        subprocess.call(['ffplay', '-nodisp', '-autoexit', temp_file_path])

         # Menghapus file sementara setelah pemutaran selesai
        os.remove(temp_file_path)
        
# Tombol memutar musik
play_button = tk.Button(root, text="Play", command=play_music)
play_button.pack()

# Menjalankan perulangan Tkinter
root.mainloop()