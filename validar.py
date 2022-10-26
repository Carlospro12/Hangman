from clear import Clear
from estilos import Animacion

def Run():
    pass


def Validar(Palabra_aleatoria, Palabra_correcta,vidas):
    call = 'yes'
    while call == 'yes':
        Clear()
        Animacion(Palabra_correcta,vidas)
        call = __Validar(Palabra_aleatoria, Palabra_correcta)
    return call




def __Validar(Palabra_aleatoria, Palabra_correcta):
        

    Palabra_ingresada = (input(str("""   ingrese letra o adivinr la palabra:   """)))


    if any(map(str.isdigit, Palabra_ingresada)) == True:
        return 'yes'

    elif len(Palabra_ingresada) == 0:
        return 'yes'

    elif   1 < len(Palabra_ingresada) < len(Palabra_aleatoria):
        return 'yes'

    elif Palabra_ingresada in Palabra_correcta:
        return 'yes'        
    elif len(Palabra_ingresada) > len(Palabra_aleatoria):
        return 'yes'    

    else:
        return Palabra_ingresada

        
if __name__ == '__main__':
    Run()      

    




