import pyautogui
import pyperclip # Biclioteca para reconhecer caracteres. Ex: ?
import time

pyautogui.PAUSE = 0.5 # Delay de 0.3s para cada linha do pyautogui

# pyautogui.click -> Clicar
# pyautogui.press -> Apertar uma tecla
# pyautogui.hotkey -> Conjunto de teclas
# pyautogui.write -> escreve um texto

time.sleep(5)

pyautogui.press("win")
pyautogui.write("Navegador Opera GX")
pyautogui.press("enter")
pyperclip.copy("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")

time.sleep(2)

pyautogui.click(x=1362, y=877)