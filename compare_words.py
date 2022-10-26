from validar import Validar
from clear import Clear
import estilos

def Run():
    Compare_Word()
    

def Compare_Word(Palabra_aleatoria):

    vidas = 0
    Palabra_correcta = list(('_')*len(Palabra_aleatoria))

    while vidas < 7:
        
        Clear()

        estilos.Animacion(Palabra_correcta,vidas)
        

        Palabra_ingresada = Validar(Palabra_aleatoria, Palabra_correcta,vidas)

        if len(Palabra_ingresada) == 1:

            for i, letra in enumerate(Palabra_aleatoria):

                if Palabra_ingresada == letra:
                    Palabra_correcta[i] = letra 

                    
            if not(Palabra_ingresada) in Palabra_aleatoria:
                vidas += 1   
            

            if(("".join(Palabra_correcta)) == ("".join(Palabra_aleatoria))):
                break     

                      

        else:
            if Palabra_aleatoria == list(Palabra_ingresada):
                Palabra_correcta = list(Palabra_ingresada)
                break

            else:
                vidas += 2

    if Palabra_aleatoria == Palabra_correcta:
        return ['Win',Palabra_aleatoria]

    return ['Loss', Palabra_aleatoria]



                 

if __name__ == '__main__':
    Run()                        

    
    
    




















   
            


if __name__ == '__main__':
    Run()     
    