import speech_recognition as sr 

# PyAudio installation error -> download in unofficial python binaries.

def main():
    recog = sr.Recognizer()
    
    with sr.Microphone() as source:
        recog.adjust_for_ambient_noise(source)
        print("Plz say some thing...")

        audio = recog.listen(source)

        try :
            print("You said : \n" + recog.recognize_google(audio)) 

        except Exception as e:
            print("Error : " + str(e))

if __name__ == "__main__":
    main()
    