import pyautogui as py
import time
from settings import Configs

class LogarSite:

    def run():
        try:
            time.sleep(2)
            py.click(x=130, y=20)
            print("click")
            time.sleep(1)
            py.write(Configs.url)
            py.press("enter")
            time.sleep(2)
            py.press("tab")
            py.write(Configs.login)
            py.press("tab")
            py.write(Configs.senha)
            py.press("tab")
            py.press("enter")
            time.sleep(2)

            return True
        except Exception as e:
            print(e)
            return False
        
    def esperar_elemento(imagem_elemento, tempo_limite=10):
        tempo_inicial = time.time()
        while time.time() - tempo_inicial < tempo_limite:
            # Tenta localizar o elemento na tela
            if py.locateOnScreen(imagem_elemento, confidence=0.9) is not None:
                return True
            time.sleep(0.5)  # Aguarda 1 segundo antes de tentar novamente
        return False