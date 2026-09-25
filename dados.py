import random

from rich.console import Console
from rich.panel import Panel

DADO_D4 = 4
DADO_D6 = 6
DAD0_D8 = 8
DADO_D10 =10
DADO_D12 = 12
DADO_D20 = 20

console = Console()

opcion_menu =""

while opcion_menu != "3":
    console.print(Panel(
        "[bold cyan]1[/bold cyan]. Lanzar dados\n"
        "[bold cyan]2[/bold cyan]. Salir",
    ))

    opcion_menu = input("Elige una opción (1-3): ")
    
try:
    opcion_menu_numero = int(opcion_menu)
except ValueError:
    console.print("[red]Opcion no valida introduzca uno de los numeros de las opciones[/red]")
    opcion_menu = ""
    
    

if opcion_menu_numero == 1:
    console.print(Panel(
            "[bold]1[/bold]. D4\n"
            "[bold]2[/bold]. D6\n"
            "[bold]3[/bold]. D8\n"
            "[bold]4[/bold]. D10\n"
            "[bold]5[/bold]. D12\n"
            "[bold]6[/bold]. D20",
            print="Elige el tipo de dado",
        ))
    
    tipo_dado_valido = False
    
    while not tipo_dado_valido:
        tipo_dado_opcion = input("Que tipo de dado quieres lanzar:  ")
        
        try:
            tipo_dado = int(tipo_dado_opcion)
        except ValueError:
            console.print("[red]DEbes introducir un numero[/red]")
            continue
        
        if tipo_dado == 1:
            caras_dados = DADO_D4
            nombre_dado = "D4"
            tipo_dado_valido = True
        elif tipo_dado == 2:
            caras_dados = DADO_D6
            nombre_dado = "D6"
            tipo_dado_valido = True
        elif tipo_dado == 3:
            caras_dados = DAD0_D8
            nombre_dado = "D8"
            tipo_dado_valido = True
        elif tipo_dado == 4:
            caras_dados = DADO_D10
            nombre_dado = "D10"
            tipo_dado_valido = True
        elif tipo_dado == 5:
            caras_dados = DADO_D12
            nombre_dado = "D12"
            tipo_dado_valido = True
        elif tipo_dado == 6:
            caras_dados = DADO_D20
            nombre_dado = "D20"
            tipo_dado_valido = True
        else:
            console.print("[red]Elige una opcion validda[/red] ")