import pandas as pd
import pyautogui as py
import time
from settings import Configs as cf

class InserirDadosWeb:

    def run():
        py.PAUSE = 0.05
        tabela = pd.read_csv(cf.caminho_dados)
        py.press("tab")
        for linha in tabela.index:
            #Codigo 
            py.write(tabela.loc[linha, 'codigo'])

            #Marca
            py.press("tab")
            py.write(tabela.loc[linha, 'marca'])

            #tipo
            py.press("tab")
            py.write(tabela.loc[linha, 'tipo'])

            #categoria
            py.press("tab")
            py.write(str(tabela.loc[linha, 'categoria']))

            #Preco unitario
            py.press("tab")
            py.write(str(tabela.loc[linha, 'preco_unitario']))

            #Custo
            py.press("tab")
            py.write(str(tabela.loc[linha, 'custo']))

            #obs
            py.press("tab")
            dados = tabela.loc[linha, 'obs']
            if not pd.isna(dados):
                py.write(str(tabela.loc[linha, 'obs']))
            
            #Enviar
            py.press("tab")
            py.press("enter")
            py.press('pageup')
            time.sleep(1.5)
            py.click(x=521, y=292)
        py.hotkey('alt', 'f4')
