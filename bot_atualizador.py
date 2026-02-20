import pyautogui
import time

IMAGE_PATH = "assets/refresh_button.png"

INTERVAL = 40

print("Iniciando busca... Clique CTRL + c para interromper a execução.")

stop = False

while not stop:
    try:
        location = pyautogui.locateCenterOnScreen(
            IMAGE_PATH,
            confidence=0.7
        )

        if location:
            print(f"Imagem encontrada em {location}! Clicando...")
            pyautogui.click(location)
        else:
            print("Imagem não encontrada.")

    except Exception as e:
        print("Erro:", e)

    time.sleep(INTERVAL)
