import pyautogui
import time

# Caminho da imagem que você quer encontrar
IMAGE_PATH = "assets/refresh_button.png"

# Intervalo em segundos (1 minuto)
INTERVAL = 60

print("Iniciando busca... Pressione CTRL+C para parar.")

while True:
    try:
        location = pyautogui.locateCenterOnScreen(
            IMAGE_PATH,
            confidence=0.8  # diminua se não estiver encontrando
        )

        if location:
            print(f"Imagem encontrada em {location}! Clicando...")
            pyautogui.click(location)
        else:
            print("Imagem não encontrada.")

    except Exception as e:
        print("Erro:", e)

    time.sleep(INTERVAL)