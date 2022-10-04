import pyautogui
import pyperclip
import pandas

pyautogui.PAUSE = 0.3

# pyautogui.click -> Clicar
# pyautogui.press -> Apertar uma tecla
# pyautogui.hotkey -> Conjunto de teclas
# pyautogui.write -> escreve um texto

pyautogui.press("win")
pyautogui.write("Navegador Opera GX")
pyautogui.press("enter")
pyperclip.copy("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")