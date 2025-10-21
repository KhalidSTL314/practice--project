import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
import os

def choose_file():
    file_path = filedialog.askopenfilename(
        title="Select a song file",
        filetypes=[("Audio Files", "*.wav *.mp3 *.m4a *.flac")]
    )
    if file_path:
        entry.delete(0, tk.END)
        entry.insert(0, file_path)

def run_transcription():
    file_path = entry.get()
    if not file_path:
        messagebox.showerror("Error", "Please select a song file first.")
        return

    # Call your transcribe.py script
    try:
        subprocess.run(["python3", "transcribe.py", file_path], check=True)
        messagebox.showinfo("Done", "Transcription complete! Check your output file.")
    except subprocess.CalledProcessError:
        messagebox.showerror("Error", "Something went wrong while running the transcription.")

# GUI setup
root = tk.Tk()
root.title("Song Transcriber")
root.geometry("400x200")

tk.Label(root, text="Choose a song to transcribe:", font=("Arial", 12)).pack(pady=10)

frame = tk.Frame(root)
frame.pack(pady=5)

entry = tk.Entry(frame, width=40)
entry.pack(side=tk.LEFT, padx=5)

tk.Button(frame, text="Browse", command=choose_file).pack(side=tk.LEFT)

tk.Button(root, text="Transcribe", command=run_transcription, bg="#4CAF50", fg="white", padx=10, pady=5).pack(pady=15)

root.mainloop()
