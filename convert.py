import tkinter as tk
from tkinter import filedialog
from gtts import gTTS
from pydub import AudioSegment

class TextToAudioConverter:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Text to Audio Converter")
        self.label = tk.Label(self.root, text="Enter text:")
        self.label.pack()
        self.text_entry = tk.Text(self.root, height=10, width=40)
        self.text_entry.pack()
        self.convert_button = tk.Button(self.root, text="Convert", command=self.convert_text)
        self.convert_button.pack()
        self.audio_file_label = tk.Label(self.root, text="")
        self.audio_file_label.pack()

    def convert_text(self):
        text = self.text_entry.get("1.0", "end-1c")
        language = "en"  # default language
        speech = gTTS(text=text, lang=language, slow=False)
        speech.save("output.mp3")
        audio_file = AudioSegment.from_mp3("output.mp3")
        audio_file.export("output.wav", format="wav")
        self.audio_file_label.config(text=f"Audio file saved as output.wav")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    converter = TextToAudioConverter()
    converter.run()