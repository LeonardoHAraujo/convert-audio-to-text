import speech_recognition as sr


r = sr.Recognizer()

with sr.AudioFile('ng17.wav') as source:
    audio_text = r.listen(source)

    try:
        text = r.recognize_google(audio_text, language = "pt-BR")
        print('Converting audio transcripts into text ...')
        
        with open('file.txt', 'w') as f:
            f.write(text)
    except:
        print('Sorry.. run again...')
