
#*************
# Sena, Mosquera CBA
# Brayan Esteban Penagos Gutierrez
# Version 2.0
# 02/05/2024
# Ficha: 2877795
#Funcionalidad: Clases y Objetos con Herencia
#*************


from colorama import Fore, Style, init
import modules.classes as classes
import modules.funtions as functions
import os
init()

def main():
    persona = classes.Persona()
    personas = functions
    os.system('cls')
    print(Fore.LIGHTRED_EX + '\n''************PERSONA************''\n'+ Style.RESET_ALL)
    persona.datos_generales()
    persona.informacion_persona()
    personas.mostrar_informacion_persona()
    
    docente = classes.Docentes()
    docente = functions
    
    print(Fore.LIGHTYELLOW_EX + '\n''************DOCENTES************''\n' + Style.RESET_ALL)
    docente.mostrar_datos_docentes()

    tiempo = classes.Tiempo_Completo()
    tiempo = functions

    print(Fore.LIGHTBLUE_EX + '\n''************TIEMPO COMPLETO************''\n'+ Style.RESET_ALL)
    tiempo.mostrar_datos_tiempo()
    
    ocasional = classes.Ocasionales()
    ocasional = functions

    print(Fore.LIGHTBLUE_EX + '\n''************OCASIONALES************''\n'+ Style.RESET_ALL)
    ocasional.mostrar_datos_ocasional()

    catedra = classes.Hora_Catedra()
    catedra = functions

    print(Fore.LIGHTBLUE_EX + '\n''************CÁTEDRA************''\n'+ Style.RESET_ALL)
    catedra.mostrar_datos_catedra()


    admin = classes.Administrativos()
    admin = functions

    print(Fore.CYAN + '\n''************ADMINISTRATIVOS************''\n'+ Style.RESET_ALL)
    admin.mostrar_datos_admin()


    planta = classes.Planta()
    planta = functions

    print(Fore.LIGHTGREEN_EX + '\n''************PLANTA************''\n'+ Style.RESET_ALL)
    planta.mostrar_datos_planta()
    
    ops = classes.OPS()
    ops = functions
    
    print(Fore.LIGHTMAGENTA_EX + '\n''************OPS************''\n'+ Style.RESET_ALL)
    ops.mostrar_datos_OPS()
    
    auxiliar = classes.Auxiliar()
    auxiliar = functions
    
    print(Fore.YELLOW + '\n''************AUXILIARES************''\n'+ Style.RESET_ALL)
    auxiliar.mostrar_datos_auxiliar()
    
    tecnico = classes.Tecnico()
    tecnico = functions
    
    print(Fore.LIGHTGREEN_EX + '\n''************TECNICO************''\n'+ Style.RESET_ALL)
    tecnico.mostrar_datos_tecnico()
    
    profesional = classes.Profesional()
    profesional = functions
    
    print(Fore.LIGHTMAGENTA_EX + '\n''************PROFESIONAL************''\n'+ Style.RESET_ALL)
    profesional.mostrar_datos_profesional()
if __name__ == '__main__':
    main()