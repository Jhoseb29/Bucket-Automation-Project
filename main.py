from src.layers.presentation.display import display_sort_stack, display_txt_files
import pyautogui
from time import sleep

pyautogui.press('win')
sleep(1.5)
pyautogui.write("Archivos", interval=0.1)
pyautogui.press('enter')
sleep(1.5)
pyautogui.press('enter')
sleep(2)
pyautogui.write("Documentos", interval=0.1)
sleep(1)
pyautogui.press('enter')
sleep(1)
pyautogui.write("Archivos_txt", interval=0.1)
sleep(1)
pyautogui.press('enter')


#* Show the .txt files
display_txt_files()

print()

#* Show the stack created
display_sort_stack()
