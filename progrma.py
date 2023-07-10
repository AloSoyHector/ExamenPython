menu = """ Bienvenido a Creativos.cl 
1. Comprar Entradas
2. Mostrar Ubicaciones Disponibles
3. Ver listado de asistentes
4. Mostrar ganancias totales
5. Salir
Ingrese una opcion: 
"""
menuentradas = """ Seleccione la ubicacion de su asiento
1. Platinum, $120.000. (Asientos del 1 al 20). 
2. Gold, $80.000. (Asientos del 21 al 50).
3. Silver, $50.000. (Asientos del 51 al 100.).
"""
listaasientos = ['X' if i < 0 else ' ' for i in range(101)]  
def ComprarEntradas():
    while True:
        try:
           print("Comprar entradas")
           cantidad = int(input("Ingrese la cantidad de entradas a comprar (1-3): "))
           if cantidad < 1 or cantidad > 3:
            print("La cantidad debe estar entre 1 y 3.") 

           compra_entradas = []
           for i in range(cantidad):
            print(" Seleccione las Entradas ({} de {})".format(i + 1, cantidad))
            print("Asientos disponibles:")
           listaasientos()
           asientos = int(input("Ingrese el número de asiento deseado: "))
           if asientos < 1 or asientos > 100 or listaasientos[asientos] == 'X':
            print("Error: El asiento no está disponible.")

           listaasientos[asientos] = 'X'
           compra_entradas.append(asientos)
        except:
            print("Ha ocurrido una excepcion")

def MostrarUbicaciones():
    while True:
        try:
            print()
                
        except:
            print("Ocurrio una excepcion")








nombre_apellido = input("Ingrese su nombre y apellido")
while True:
    try:
        opc = int(input(menu))
        if opc == 1:
            ComprarEntradas()
        if opc == 2:
            MostrarUbicaciones()
        if opc == 3:
            Verlistado
        if opc == 4:
           MostrarGanancias
        if opc == 5:
           print(f"Ha salido exitosamente {nombre_apellido} con fecha 10/07/23")

    except:
        print("Ha ocurrido una excepcion")
