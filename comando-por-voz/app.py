# pip install SpeechRecognition
# pip install C:\Users\mathe\Desktop\projeto\PyAudio-0.2.11-cp310-cp310-win_amd64.whl

import speech_recognition as sr

import os

def ouvir_microfone():
    #Habilita o microfone do usuário
    mic = sr.Recognizer()

    with sr.Microphone() as source:

        # Chama um algoritimo de redução de ruídos
        mic.adjust_for_ambient_noise(source)

        print("Diga algo: ")

        # Armazena o que foi dito em uma variável.
        audio = mic.listen(source)
    
    try:

        # Envia a variável para o algoritmo reconhecer padrões.
        frase = mic.recognize_google(audio, language='pt-BR')

        if "navegador" in frase:
            os.system("start Chrome.exe")

        elif "Excel" in frase:
            os.system("start Excel.exe")

        print("Você disse: " + frase)

    # Se não reconhecer a fala, irá exibir uma mensagem.
    except sr.UnknownValueError:
        print("Não entendi, tente novamente!")

    return frase

ouvir_microfone()