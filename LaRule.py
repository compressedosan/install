import random
import sys

#este bloque es para asignar los numeros de la ruleta, for es para añadir un rango a la lista de numeros de la ruleta
numeros_rulote = []
for x in range(37):
    numeros_rulote.append(x)


print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⠟⢉⣠⢶⣟⠋⢹⣆⣀⣿⣬⣾⣿⣠⣿⣰⣢⡏⠙⢻⡶⣄⡙⢻⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡷⠺⢀⣴⢿⣷⣘⣿⠶⣛⣭⣵⡆⣶⣶⢶⣶⣰⣯⣭⣓⠶⣿⡠⣸⣿⢦⡈⠿⣺⣿⣿⣿⣿⣿⣿⣿⣿⣿")
print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⢁⣴⠛⢷⣴⡽⣫⣶⣯⣻⣿⢻⣿⢹⣿⣼⣇⣿⣟⣿⣟⣿⣶⣝⠻⣠⣾⡟⣦⡛⢻⣿⣿⣿⣿⣿⣿⣿⣿")
print("⣿⣿⣿⣿⣿⣿⣿⣿⡏⢠⡾⢷⣀⡼⣫⣾⣿⣮⣿⡿⢛⣩⣭⣴⣶⣶⣦⣭⣌⡛⢿⣿⣵⣿⣷⣝⢷⣢⡼⢷⡄⠻⣿⣿⣿⣿⣿⣿⣿")
print("⣿⣿⣿⣿⣿⣿⣿⢗⢠⣿⣤⣲⡟⣬⣿⢿⣿⠟⣡⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣌⠻⣿⣿⣿⣧⢹⣄⣠⣿⡄⠸⣿⣿⣿⣿⣿⣿")
print("⣿⣿⣿⣿⣿⣿⡟⡀⣾⣍⣉⡟⣼⣿⡻⣿⢋⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⠛⢻⣷⡙⡿⣟⣿⣧⢻⡉⣂⣷⡀⢻⣿⣿⣿⣿⣿")
print("⣿⣿⣿⣿⣿⣿⡃⢰⡏⠉⣽⢣⣽⣻⣿⡇⣾⣿⣿⣿⣿⣿⣿⡿⠿⠿⢿⣿⣿⣿⣷⡀⢻⣷⠸⣿⣛⣯⡝⣿⠟⢻⡇⠸⣿⣿⣿⣿⣿")
print("⣿⣿⣿⣿⣿⣿⣁⢸⠷⠷⡿⢸⣿⣿⣟⢰⣿⣿⣿⣿⣿⣿⡏⡀⡀⡀⡀⠹⣿⣿⣿⣇⣈⣿⡆⣿⣿⣿⡇⣿⠛⠛⡇⣇⣿⣿⣿⣿⣿")
print("⣿⣿⣿⣿⣿⣿⢩⢸⣶⣶⣧⢸⣛⣻⣿⢸⣿⣿⣿⣿⣿⣿⣇⡀⡀⡀⡀⣨⣿⣿⣿⡟⢉⣿⡇⣿⣟⣛⡃⣿⢤⢤⡇⡏⣿⣿⣿⣿⣿")
print("⣿⣿⣿⣿⣿⣿⡆⢸⣯⣭⣿⣼⣻⣿⣿⡅⢿⣿⣿⣿⣿⣿⣿⣷⣦⣤⣾⣿⣿⣿⡟⡀⣼⡿⢠⣿⣿⣟⣇⣷⣀⢸⡇⢠⣿⣿⣿⣿⣿")
print("⣿⣿⣿⣿⣿⣿⣧⡀⢿⠉⢘⣇⢻⣿⣽⣿⡌⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⡿⢡⣿⣯⣟⡿⣸⠋⠉⡿⡀⣼⣿⣿⣿⣿⣿")
print("⣿⣿⣿⣿⣿⣿⣿⡖⠘⣿⠋⠹⣯⢻⣿⣷⡿⣦⡙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢋⣴⢿⣿⣿⡟⣱⠋⠛⣿⠃⢰⣿⣿⣿⣿⣿⣿")
print("⣿⣿⣿⣿⣿⣿⣿⣿⣔⡘⣷⡞⡉⢷⡹⢿⣿⣿⣿⣶⣬⡙⠛⠿⠿⠿⠿⣛⢋⣥⣶⣿⡻⣷⣿⢏⡾⡙⢶⣼⠃⣢⣿⣿⣿⣿⣿⣿⣿")
print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡈⢻⣤⡾⠛⣾⣝⠿⣿⣽⣿⣽⣿⢹⣿⢻⣏⣿⣯⣿⣯⣿⡿⣫⡴⠋⠳⣤⡟⢁⣶⣿⣿⣿⣿⣿⣿⣿⣿")
print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡷⣶⠝⠳⣿⡏⠈⣷⠾⣝⣛⠿⠏⠿⡿⠾⠿⠹⢿⣛⡩⠵⣿⡉⢿⣦⠞⠉⣶⢼⣿⣿⣿⣿⣿⣿⣿⣿⣿\n")

#roleplay
print("¡LAAAA SUPEEER RUELEE DE LA SUERTEEEE!\n")
input("Presiona enter para empezar...\n")
print("Las tres apuestas posibles son:\n[1]   Verde x14 beneficios\n[2]   Rojo x2 beneficios\n[3]   Negro x2 beneficios\n")
print("*en letra pequeña* El casino no se hace responsable de desaucios y causar fuertes problemas de ludopatía o addicción al juego.\n")
input("Presiona enter si has entendido las reglas\n")


deposit = abs(float(input("Introduce el deposito par empezar a jugar\n")))
print(f"Gracias por depositar {deposit} rublos ¥\n")


#esto es para asegurarse de que la apuesta sea una valida
bet = abs(int(input("Introduce la apuesta [1] [2] [3] \n")))
while not (bet == 1 or bet == 2 or bet == 3):
    print("Por favor introduce una apuesta válida [1] [2] [3] \n")
    bet = abs(int(input("Introduce la apuesta [1] [2] [3] \n")))

#Este bloque es para anunciar al jugador a que color ha apostado
if bet == 1:
    print("Has apostado al verde!\n")
else:  
    if bet == 2:
        print("Has apostado al Rojo!\n")
    else:
        print("Has apostado al Negro!\n")

#Este bloque es para fijar una apuesta y asegurar de que sea menos de la cantidad del deposito
mbet = abs(float(input("Introduce cuantos rublos quieres apostar\n")))
while mbet > deposit: 
    print("No puedes apostar más dineros de los que tienes [X]\n")
    mbet = abs(float(input("Introduce cuantos rublos quieres apostar\n")))

deposit = deposit - mbet

#aqui tiene que elegir automaitcamente por rng la rule de la suerte un numero
ganador = random.choice(numeros_rulote)

#seleccion de ganador y prices
#apuesta a VERDE
if bet == 1:    
    if ganador == 0:
        print("El número de la super rule es el putisimos", ganador, "guatefoc omaigod chad\n")
        deposit = deposit + (mbet*15)
        print("Has putisimo ganado el x14, ahora eres rico y tienes ", deposit, " putisimos Rublos ¥\n")
    else: 
        if ganador % 2 == 0:
            print("El número de la super rule es ", ganador,"ROJO !\n") 
            print("Has perdido!\n")
            print("Ahora tienes", deposit, "rublos ¥ !, Échale 5 eurillos más anda.\n" )
        else:
            if ganador % 2 != 0:
                print("El número de la super rule es ", ganador,"NEGRO !\n") 
                print("Has perdido!")
                print("Ahora tienes", deposit, "rublos ¥ !, Échale 5 eurillos más anda.\n" )

#Apuesta a ROJO
if bet == 2:
    if ganador == 0:
         print("El número de la super rule es el putisimos", ganador, "guatefoc omaigod chad\n")
         print("Has putisimo troleado, salió el 0 y te has estampado\n")
         print("Ahora tienes", deposit, "rublos ¥ !, Échale 5 eurillos más anda.\n")
    else:
        if ganador % 2 == 0:
            print("El número de la super rule es ", ganador,"ROJO !\n") 
            deposit = deposit + (mbet*2) 
            print("Has ganado!\n")    
            print("Ahora tienes", deposit, "rublos ¥ !\n" )
        else:
            print("El número de la super rule es ", ganador,"NEGRO !\n")
            print("Has perdido!\n")    
            print("Ahora tienes", deposit, "rublos ¥ !, Échale 5 eurillos más anda.\n")

#Apuesta a NEGRO
if bet == 3:
    if ganador == 0:
         print("El número de la super rule es el putisimos", ganador, "guatefoc omaigod chad\n")
         print("Has putisimo troleado, salió el 0 y te has estampado\n")
         print("Ahora tienes", deposit, "rublos ¥ !, Échale 5 eurillos más anda.\n" )
    else:
        if ganador % 2 != 0:
            print("El número de la super rule es ", ganador,"NEGRO !\n") 
            deposit = deposit + (mbet*2) 
            print("Has ganado!")    
            print("Ahora tienes", deposit, "rublos ¥ !\n")
        else:
            print("El número de la super rule es ", ganador,"ROJO !\n")
            print("Has perdido!\n")    
            print("Ahora tienes", deposit, "rublos ¥ !, Échale 5 eurillos más anda.\n" )    
       

