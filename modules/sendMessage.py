import requests
import time

TEST_MESSAGE = """Hola {name}, te saluda Unilix 🎉
📢 Estamos enviando mensajes de prueva, para verificar los numeros vinculado
📌 Esperamos no sea una molestia 😁."""

TEST = """
🎉Hola {name}, te saludamos de la Academia YACHAYWASI🎉
Apertura un ciclo especializado para la preparación para tu examen de preselección PRONBEC.
🕣 HORARIO 🕣
Lunes a viernes 
4:00 p.m - 7:15 p.m
🧾Sábados ✍
    Simulacros 

*Costo mensual S/80.00 soles*
*Inicio de clases 20 de mayo*
Informes e inscripciones 
📲949 205 807
📲946 301 605
Jr.dos de mayo 707 ( 2º piso)"""

class msg:
    def __init__(self, para, mensaje, port):
        self.para = para
        self.mensaje = mensaje
        self.port = port

    def sendMessage(self):
        url = 'http://localhost:'+ str(self.port)
        data = {
            "message": self.mensaje,
            "phone": self.para
        }
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.post(url, json=data, headers=headers)
        time.sleep(3)
        return response

def main():
    mensaje = msg('949152262', TEST, 3000)
    mensaje.sendMessage()

# main()