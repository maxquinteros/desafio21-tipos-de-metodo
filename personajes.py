import random

class Personaje:
    def __init__(self, nombre: str):
        self._nombre = nombre
        self._nivel = 1
        self._experiencia = 0

    def ajustar_nivel(self, experiencia_obtenida: int):
        experiencia_total = self._experiencia + experiencia_obtenida

        nivel_total = self._nivel + experiencia_total // 100

        if nivel_total < 1:
            nivel_total = 1

        return nivel_total

    def ajustar_experiencia(self, experiencia_obtenida: int):
        experiencia_total = self._experiencia + experiencia_obtenida

        if experiencia_total < 0 and self._nivel == 1:
            experiencia_total = 0

        experiencia_total = experiencia_total % 100

        return experiencia_total

    def obtener_probabilidades_ganar(personaje1: object, personaje2: object) -> float:
        if personaje1 < personaje2:
            return 1 / 3
        elif personaje1 == personaje2:
            return 1 / 2
        elif personaje1 > personaje2:
            return 1 / 1.5

    def comparar_niveles(personaje1: object, personaje2: object) -> str:
        if personaje1 < personaje2:
            return f"Con tu nivel actual, tienes {round(personaje1.obtener_probabilidades_ganar(personaje2)*100)}% de probabilidades de ganarle al Orco."
        elif personaje1 == personaje2:
            return f"Con tu nivel actual, tienes {round(personaje1.obtener_probabilidades_ganar(personaje2)*100)}% de probabilidades de ganarle al Orco."
        elif personaje1 > personaje2:
            return f"Con tu nivel actual, tienes {round(personaje1.obtener_probabilidades_ganar(personaje2)*100)}% de probabilidades de ganarle al Orco."

    def __lt__(personaje1: object, personaje2: object) -> bool:
        return personaje1._nivel < personaje2._nivel

    def __eq__(personaje1: object, personaje2: object) -> bool:
        return personaje1._nivel == personaje2._nivel

    def __gt__(personaje1: object, personaje2: object) -> bool:
        return personaje1._nivel > personaje2._nivel
    
    def Atacar(self, personaje2: object):
        dado = random.random()
        umbral_perder = self.obtener_probabilidades_ganar(personaje2)
        if dado < umbral_perder:
            print(f"¡Le has ganado al {personaje2._nombre}, felicidades!")
            print("¡Recibirás 50 puntos de experiencia!")
            self.estado = 50
            personaje2.estado = -30
        else:
            print(f"¡Oh no! ¡El {personaje2._nombre} te ha ganado!")
            print("¡Has perdido 30 puntos de experiencia!")
            self.estado = -30
            personaje2.estado = 50

    def Huir(self, personaje2: object) -> str:
        return f"¡Has huido! El {personaje2._nombre} ha quedado atrás."

    @property
    def estado(self):
        return f"NOMBRE: {self._nombre}   NIVEL: {self._nivel}     EXP: {self._experiencia}"

    @estado.setter
    def estado(self, experiencia_obtenida: int):
        self._nivel = self.ajustar_nivel(experiencia_obtenida)
        self._experiencia = self.ajustar_experiencia(experiencia_obtenida)
