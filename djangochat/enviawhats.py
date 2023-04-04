import pandas as pd
import webbrowser as web
import pyautogui as pg
import time
import pywhatkit 
import os
# # import time
# # import webbrowser as web
# # from datetime import datetime
# # from re import fullmatch
# # from typing import List
# # from urllib.parse import quote
# # import paperclip
# # import pyautogui as pg
# # import pyperclip
# # import keyboard

# pywhatkit.start_server()
# pywhatkit.sendwhatmsg("+5492932447203", "Mi mensajeProgramado",17,32)
pywhatkit.sendwhatmsg_instantly("+5492932447203", "Mi mensaje instantaneo", True)

# # Send a WhatsApp Message to a Group instantly
pywhatkit.sendwhatmsg_to_group_instantly("GkpPPepSkiM6ZabSXixxX4", "Hey All! group desde python")

# Crear mensaje personalizado
mensaje = "Hola, " + "! Gracias por comprar " + " con nosotros 🙌"
    
    # Abrir una nueva pestaña para entrar a WhatsApp Web
    # Opción 1: Si te abre WhastApp Web directamente en Google Chrome
web.open("https://web.whatsapp.com/send?phone=" + "+5492932447203" + "&text=" + mensaje)
    
    # Opción 2: Si te abre WhastApp Web en Microsoft Edge, especificar que lo abra en Chrome
# chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
# web.get(chrome_path).open("https://web.whatsapp.com/send?phone=" + "+5492932447203" + "&text=" + mensaje)

time.sleep(8)           # Esperar 8 segundos a que cargue
pg.click(1230,964)      # Hacer click en la caja de texto
time.sleep(2)           # Esperar 2 segundos 
pg.press('enter')       # Enviar mensaje 
time.sleep(3)           # Esperar 3 segundos a que se envíe el mensaje
pg.hotkey('ctrl', 'w')  # Cerrar la pestaña
time.sleep(2)