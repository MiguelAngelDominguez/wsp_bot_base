import requests
import time

TEST_MESSAGE = """Hola {name}, te saluda Unilix 🎉
📢 Estamos enviando mensajes de prueva, para verificar los numeros vinculado
📌 Esperamos no sea una molestia 😁."""

TEST = """Hola {name}, te saludamos de la Academia TONER 📚✨

Abrimos un ciclo SELECCION GENERAL
🕣 HORARIO 🕣
Lunes a viernes
5:00 p.m - 8:00 p.m

Costo mensual {pat_money} soles
Inicio de clases {date_start}

Informes e inscripciones
{phones}
{address}
"""

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