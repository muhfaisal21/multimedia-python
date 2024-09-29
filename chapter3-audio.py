import tkinter as tk
from tkinter import filedialog
from pydub import AudioSegment
import subprocess
import tempfile
import os

# Membuat jendela utama
root = tk.Tk()
root.title("Aplikasi Multimedia")

# Definisikan fungsi untuk memutar musik
def play_music():
    # Menggunakan file dialog untuk memilih file audio
    file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3;*.wav;*.ogg;*.flac")])
    if file_path:
        try:
            # Memuat file audio
            audio = AudioSegment.from_file(file_path)

            # Membuat file sementara untuk menyimpan audio yang akan diputar
            with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as temp_audio_file:
                temp_file_path = temp_audio_file.name
                # Mengekspor audio ke file sementara
                audio.export(temp_file_path, format="mp3")

            # Memutar audio dengan ffplay
            subprocess.call(['ffplay', '-nodisp', '-autoexit', temp_file_path])

        except Exception as e:
            print(f"Error saat memutar audio: {e}")

        finally:
            # Menghapus file sementara setelah pemutaran selesai
            if os.path.exists(temp_file_path):
                os.remove(temp_file_path)

# Tombol memutar musik
play_button = tk.Button(root, text="Play", command=play_music)
play_button.pack(pady=20)

# Menjalankan perulangan acara Tkinter
root.mainloop()
