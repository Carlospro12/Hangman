from compare_words import Compare_Word
from choose_word import Choose_Word
from clear import Clear
import estilos


def Run():
    Interfaz()

def Interfaz():
    Clear()

    print(estilos.Interfaz1)

    opcion = str(input())
    
    if opcion == '1':
        Opcion1()
    elif opcion == '2':
        Opcion2()
    elif opcion == '3':
        Clear()
        exit()
    else:
        Interfaz()
        

 #opcion1
def Opcion1():
    Clear()
    resultado = Compare_Word(Choose_Word())

    if resultado[0] == 'Win':
        Win(resultado)
       
    else:
        Loss(resultado)

#opcion2
def Opcion2():
    Clear()
    with open(r'./reglas.txt','r', encoding="utf-8") as data:
        for line in data:
            print(line)   
        print(estilos.opcion2)    
        opcion2 =input()

        if opcion2 == '1':
            Clear()
            Interfaz()
        else:
            Opcion2()    

#si gana:
def Win(resultado):
    Clear()
    estilos.Win(resultado)
    Opciones_Recurrentes(resultado)

#si pierde
def Loss(resultado):
    Clear()
    estilos.Game_Over(resultado)  
    Opciones_Recurrentes(resultado)     
            
#opciones recurrentes
def Opciones_Recurrentes(resultado):
    opcion = str(input())
    if opcion == '1':
        Opcion1()
    elif opcion == '2':
        Interfaz()
    elif opcion == '3':
        Clear()
        exit()
    else:

        if resultado[0] == 'Win':
            Win(resultado)
        else:
            Loss(resultado)    
 
if __name__ == '__main__':
    Run()
