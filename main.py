import speech_recognition as sr

credentials_path = 'sa_speech_demo.json'

speech = sr.Recognizer()
while True:
    print("Python is listening ...")
    inp = ""
    with sr.Microphone() as source:
        speech.adjust_for_ambient_noise(source)
        try:
            audio = speech.listen(source)
            # Run this code to test if audio is being stored properly
            # if audio:
            #     print("Audio captured successfully")
            #
            #     # with open("captured_audio.wav","wb") as audio_file:
            #     #     audio_file.write(audio.get_wav_data())
            inp = speech.recognize_google_cloud(audio, credentials_json=credentials_path)
        except sr.UnknownValueError:
            pass
        except sr.RequestError:
            pass
        except sr.WaitTimeoutError:
            pass
    print(f'You just said {inp}.')
    if inp == "stop listening ":
        print("Goodbye")
        break
