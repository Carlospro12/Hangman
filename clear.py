import os

def Run():
    Clear()

def Clear():

    if os.name == "posix":
        os.system("clear")

    elif  os.name == "nt":
        os.system("cls")   

    else:
        print("El juego no es compatible con este sistema operativo")   


if __name__ == '__main__':
    Run()      

