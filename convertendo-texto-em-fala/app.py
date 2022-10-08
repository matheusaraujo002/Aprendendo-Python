from gtts import gTTS

text_to_say = "Olá Matheus, bom dia!"

language = "pt-BR-Wavenet-C"

gtts_object = gTTS(text = text_to_say, 
                  lang = language,
                  slow = False)

gtts_object.save(r"C:\Users\mathe\Desktop\Conversao-de-texto-para-fala/gtts.wav")