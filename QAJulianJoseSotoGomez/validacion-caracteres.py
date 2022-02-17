import re

def validar_palabra(palabra,cadena):
    for i in cadena:
        if re.search(i,palabra):
            print(palabra)
        else:
            print("NO")

palabra = "SegurosBolivar"
#cadena = "SSSeegreruarrriioorsaBiolllaeivvarr"
cadena = "SSSeegreruarrriirsaBiolllaeivvarr"
validar_palabra(palabra,cadena)
