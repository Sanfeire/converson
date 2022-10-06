#principio

from math import *
import sys
from colorama import Fore
import time
import os

# F secundarias

def banner():
    print(Fore.RED + """

                                   &(            &
                    @@@@@@/    @@@    @@.     @@   *@@
                              &@       @@     @@   *@@   @@@@*
                     *@@@@@   @@       @@        #    /@@
                              @@       @@             /@@
                   @@@@@@@@   @@   @@  @@                @@@@@
                              @@   @@  @@
                      @@@@    @@   @@  @@
                              @@   @@  @@
                              @@   @@  @@
                      @@@@@   @@   @@  @@
                              @@   @@  @@
                   @@@@@@@@   @@   @@  @@@
                            @@     @@    @@@
                           @@   @@   #@@  ,@@
                           @@   @@    @@   @@
                            @@   @@@@@@   @@
                             @@@       (@@/
                                 @@@@@@

    """)





def pantallaInicial(): # pantalla inicial
    print (Fore.BLUE + "CONVERSOR CELSIUS <--> FAHERENHEIT")
    banner()
    uno_u_otro()


def uno_u_otro(): # confirma si el usuario quiere salir o continuar

        #banner()
        decision = input("Quieres introducir Celsius o Fahrenheit? (c/f):")

        if decision == "c":
                os.system("cls")
                print(Fore.GREEN + "OK, Celsius a Fahrenheit")
                time.sleep(2)
                main_c()

        else:
            os.system("cls")
            print(Fore.RED + "OK, Fahrenheit a Celsius")
            time.sleep(2)
            main_f()



#fin F secundarias



# F primarias



def main_c(): #función1 principal del programa, para pasar celsius a fah /// (0°C × 9/5) + 32 = 32°F [function]
        os.system("cls") 
        time.sleep(1)

        y = float(input("Introduce la temperatura en grados Celsius (ºC):"))
        
        primera_op_c = y * 9

        segunda_op_c = primera_op_c / 5

        total_c = segunda_op_c + 32

        print("La temperatura en ºF es:", total_c)
         
        time.sleep(7)
        os.system("cls")
        banner()
        time.sleep(2)
        os.system("cls")
        uno_u_otro()


def main_f(): #función2 principal del programa, para pasar fah celsius/// (32°F − 32) × 5/9 = 0°C [function]
        os.system("cls") 
        time.sleep(1)

        z = float(input("Introduce la temperatura en grados Fahrenheit (ºF):"))
        
        primera_op_f = z - 32

        segunda_op_f = primera_op_f * 5

        total_f = segunda_op_f / 9

        print("La temperatura en ºC es:", total_f)
         
        time.sleep(7)
        os.system("cls")
        banner()
        time.sleep(2)
        os.system("cls")
        uno_u_otro()

#final F primaria






#principal



os.system("cls")
pantallaInicial()
time.sleep(1)
#main_c()





#fin principal