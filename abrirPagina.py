import pyautogui as py
from settings import Configs as cf

class AbrirPaginaChrome:

    def run():
        try:
            py.PAUSE = 0.4
            py.press("win")
            py.write("chrome")
            py.press("Enter")
            py.hotkey('win', 'up')  # Maximizar a janela no Windows
            return True
        except Exception as e:
            print(e)
            return False