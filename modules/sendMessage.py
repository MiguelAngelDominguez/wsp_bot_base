import requests

from datetime import datetime

TEST_MESSAGE = """Hola, te saluda Unilix 🎉
📢 Estamos enviando mensajes de prueva, para verificar los numeros vinculado
📌 Esperamos no sea una molestia 😁."""

TEST = """💥 PARTICIPA‼ GRATIS 🙂
CONCURSO DE BECAS ✏📚

📣 Ciclo TODO EL DÍA ⏰☝
Clases 💯 %PRESENCIALES

💥 INSCRÍBETE AQUÍ: 👇
▶ https://bit.ly/44zZ6QD ◀

🗒 Jueves 23 mayo
⏰ 4:30 p.m.

📌 Lugar
🏢 Jr. 28 de Julio N° 1098 - 4to piso | Frente al Banco de la Nación, a una cuadra de la Plaza de Armas. 

🔥 No olvides llevar lápiz ✏, borrador y tú DNI.

👉 ÚNETE A LA PRE MÁS GRANDE DE LA REGIÓN 👊 

🎓 Tu mejor garantía:
NUESTROS CACHIMBOS‼"""

class msg:
    def __init__(self, para, mensaje, port):
        self.para = para
        self.mensaje = mensaje
        self.port = port
    
    def check_server(self):
        url = f'http://localhost:{self.port}'
        try:
            response = requests.get(url)
            return response.status_code == 200
        except requests.exceptions.RequestException:
            return False

    def sendMessage(self):
        if not self.check_server():
            with open('log_msgEnviados.txt', 'a') as log:
                current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                log.writelines(f"El servidor se cayó al enviar mensaje a {self.para} a las {current_time} por el puerto {self.port}\n")
            return None
        
        url = 'http://localhost:'+ str(self.port)
        data = {
            "message": self.mensaje,
            "phone": self.para
        }
        headers = {
            'Content-Type': 'application/json'
        }
        try:
            response = requests.post(url, json=data, headers=headers)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            with open('log_msgEnviados.txt', 'a') as log:
                current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                log.writelines(f"Error al enviar mensaje a {self.para} a las {current_time} por el puerto {self.port}: {str(e)}\n")
            return None

def main():
    mensaje = msg('949152262', TEST, 4000)
    mensaje.sendMessage()

# main()