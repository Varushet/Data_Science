import getpass

def jugar():
    ABC = "ABCDEFGHIJKLMNÑOPQRSTUVXYZ"
    NUMERO = "0123456789"
    vidas = 6    
    
    while True:
        ahorcado = getpass.getpass("Palabra secreta: ")
        if any(c in NUMERO for c in ahorcado):
            print("La palabra no puede contener números. Inténtalo de nuevo.")
        else:
            break
    
    espacios = [" _"]*len(ahorcado)
    palabra = list(ahorcado.upper())
    errores = set()
    ejecucion = 0
    
    while vidas > 0:
        print(f"Tienes: {vidas} vidas")
        print(*espacios)
        print("Fallos: ", list(errores))
        
        match ejecucion:
            case 0:
                print("       ")
                print("=========")
            case 1:
                print("  +---+")
                print("  |   |")
                print("  0   |")
                print("      |")
                print("      |")
                print("      |")
                print("=========")
            case 2:
                print("  +---+")
                print("  |   |")
                print("  O   |")
                print("  |   |")
                print("      |")
                print("      |")
                print("=========")
            case 3:
                print("  +---+")
                print("  |   |")
                print("  0   |")
                print("  |   |")
                print(" /    |")
                print("      |")
                print("=========")
            case 4:
                print("  +---+")
                print("  |   |")
                print("  0   |")
                print("  |   |")
                print(" / \  |")
                print("      |")
                print("=========")
            case 5:
                print("  +---+")
                print("  |   |")
                print("  0   |")
                print(" /|   |")
                print(" / \  |")
                print("      |")
                print("=========")
            case 6:
                print("  +---+")
                print("  |   |")
                print("  0   |")
                print(" /|\  |")
                print(" / \  |")
                print("      |")
                print("=========")
        
        if "_" not in "".join(espacios):
            print("Has Ganado!!")
            break    
            
        try:
            print("_________________________________________________________________")
            letra = input("Prueba una letra: ").upper()
            
            if letra == "0":
                break
            
            if len(letra) == 0:
                raise ValueError("100")                
            elif len(letra) > 1:
                if ahorcado.upper() == letra:
                    print("Has Ganado!!")
                    break  
                else:
                    raise ValueError("101")  
            elif letra not in ABC:
                raise ValueError("102")
            elif letra in errores:
                raise ValueError("103")                
                
            bandera = False
            for n, a in enumerate(palabra):
                if a == letra:
                    espacios[n] = letra
                elif letra not in palabra:
                    bandera = True
            
            if bandera == True:
                vidas -= 1
                ejecucion += 1
                errores.add(letra)
                
        except ValueError as e:
            if str(e) == "100":
                print("Error: Campo vacío, introduce una letra")
            elif str(e) == "101":
                print("Error: Introduce solo una letra")
            elif str(e) == "102":
                print("Error: Caracter inválido")
            elif str(e) == "103":
                print("Error: Ya se ha introducido")
                
            

jugar()