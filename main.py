from abrirPagina import AbrirPaginaChrome as apc
from logarSite import LogarSite as ls
from preencherDados import InserirDadosWeb as ids

class Main:

    #Abrir Chrome
    apc.run()

    #Logar no Site
    ls.run()

    #Preencher os dados na web
    ids.run()