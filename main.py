import time
from ensamblaje import Carro, CintaCorrediza, Robot, Operador

cinta = CintaCorrediza()
robot = Robot(1)

print("Digite el nombre del operador del sistema: ")
nombre_op = str(input())
operador = Operador(nombre_op)

while True:
    print("\n--- PANEL DE CONTROL ---")
    print("Digite 1 para ingresar carros a la cinta corrediza")
    print("Digite 2 para que el operador controle el robot y ponga los vidrios")
    print("Digite 3 para ver el resumen del proceso")
    print("Digite 4 para salir del programa")
    
    opcion = int(input())

    match opcion:
        case 1:
            print("Digite la cantidad de carros a ingresar: ")
            cantidad = int(input())
            for i in range(cantidad):
                nuevo_carro = Carro(i + 1)
                cinta.agregar_carro(nuevo_carro)
                print(nuevo_carro.ver_info())
        case 2:
            if len(cinta.carros) == 0:
                print("No hay carros en la cinta corrediza.")
            else:
                for carro in cinta.carros:
                    operador.controlar_proceso(cinta, robot, carro)
                    time.sleep(2) 
        case 3:
            print(operador.generar_resumen(cinta))
        case 4:
            print("Finalizó con éxito \n")
            break
