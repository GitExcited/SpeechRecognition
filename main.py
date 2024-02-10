import speech_recognition as sr

credentials_path = 'sa_speech_demo.json'

speech = sr.Recognizer()
print("Python is listening ...")
with sr.Microphone() as source:
    speech.adjust_for_ambient_noise(source)
    audio = speech.listen(source)
    if audio:
        print("Audio captured successfully")
        # Run this code to test if audio is being stored properly
        # with open("captured_audio.wav","wb") as audio_file:
        #     audio_file.write(audio.get_wav_data())
    inp = speech.recognize_google_cloud(audio, credentials_json = credentials_path)
print(f'You just said {inp}.')
