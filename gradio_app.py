import gradio as gr
import speech_recognition as sr

def transcribe_audio(audio):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio) as source:
        audio_data = recognizer.record(source)
        return recognizer.recognize_google(audio_data)

app = gr.Interface(
    fn=transcribe_audio,
    inputs=gr.Audio(type="filepath"),
    outputs="text",
    title="Song Transcriber",
    description="Upload a song or audio file to transcribe lyrics or speech."
)

app.launch()
