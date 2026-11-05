import time

class Carro:
    def __init__(self, id_carro):
        self.id_carro = id_carro
        self.tiene_vidrio = False
        self.estado = "en espera"

    def get_tiene_vidrio(self):
        return self.tiene_vidrio

    def set_tiene_vidrio(self, tiene_vidrio):
        self.tiene_vidrio = tiene_vidrio

    def ver_info(self):
        return f"Carro {self.id_carro} | Vidrio instalado: {self.tiene_vidrio} | Estado: {self.estado}"


class CintaCorrediza:
    def __init__(self):
        self.carros = []
        self.movimiento = "detenida"

    def agregar_carro(self, carro):
        self.carros.append(carro)

    def mover_cinta(self, carro):
        self.movimiento = "en movimiento"
        carro.estado = "en posición de ensamblaje"
        return f"Cinta {self.movimiento}: El Carro {carro.id_carro} avanzó a la posición."

    def detener_cinta(self):
        self.movimiento = "detenida"
        return f"Cinta {self.movimiento} para iniciar instalación."


class Robot:
    def __init__(self, id_robot):
        self.id_robot = id_robot
        self.accion = "inactivo"

    def poner_vidrio(self, carro):
        if carro.get_tiene_vidrio() == False:
            self.accion = "instalando vidrio panorámico"
            carro.set_tiene_vidrio(True)
            carro.estado = "completado"
        else:
            self.accion = "sin acción (ya tiene vidrio)"

    def ver_info(self):
        return f"Robot {self.id_robot}: {self.accion}"


class Operador:
    def __init__(self, nombre):
        self.nombre = nombre

    def controlar_proceso(self, cinta, robot, carro):
        print(f"\nOperador {self.nombre} iniciando secuencia desde el panel...")
        print(cinta.mover_cinta(carro))
        print(cinta.detener_cinta())
        
        time.sleep(2)
        
        robot.poner_vidrio(carro)
        print(robot.ver_info())
        print(carro.ver_info())

    def generar_resumen(self, cinta):
        completados = sum(1 for c in cinta.carros if c.estado == "completado")
        pendientes = sum(1 for c in cinta.carros if c.estado != "completado")
        return f"Resumen de línea: {completados} carros con vidrio panorámico, {pendientes} pendientes."
