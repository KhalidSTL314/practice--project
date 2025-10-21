import speech_recognition as sr

print("Script is running")

r = sr.Recognizer()

with sr.AudioFile('song.wav') as source:
    duration = source.DURATION
    print(f"Audio duration: {duration} seconds")
    chunk_length = 30  # seconds
    transcript = ""

    offset = 0
    while offset < duration:
        print(f"Processing chunk from {offset} to {min(offset + chunk_length, duration)} seconds")
        audio = r.record(source, duration=chunk_length)
        try:
            chunk_text = r.recognize_google(audio)
            transcript += chunk_text + " "
        except sr.UnknownValueError:
            transcript += "[Unrecognized] "
        except sr.RequestError as e:
            transcript += f"[Error: {e}] "
        offset += chunk_length

print("Full transcript:")
print(transcript)