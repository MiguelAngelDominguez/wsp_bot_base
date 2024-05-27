import modules.csv_reader_data as csv
import modules.sendMessage as send
import modules.Table as tb
import time
import threading
import os 
from datetime import datetime

TEST_PATH = './database/filtered_SMS.csv'

NUMBER_SV = 7

MONEY_MSG = 800
START_DATE = "12 de julio"
PHONES = "📞 999 000 111 - 999 000 111"
ADDRESS = "🏠 Jr. 28 de Julio 1098 4to piso"

MESSAGE = """Hola {name}, te saludamos de la Academia TONER 📚✨

Abrimos un ciclo SELECCION GENERAL
🕣 HORARIO 🕣
Lunes a viernes
7:00 a.m - 8:00 p.m

Costo mensual {pay_money} soles
Inicio de clases {date_start}

Informes e inscripciones
{phones}
{address}
"""

TEST_MESSAGE = """Hola {name}, te saludamos de parte de Unilix y del Dev MiguelADV 🎉
📢 Te queremos Informar que estamos haciendo Pruebas dentro y fuera de nuestro contexto.
En los próximos minutos recibirás algunos menajes de pruebas para una academia externa a nosotros.
Después de recibir este mensaje, te recomendamos silenciar este chat temporalmente.
Gracias por tu tiempo y comprensión.
"""

MSG_TORNER = """💥 PARTICIPA‼ GRATIS 🙂
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

def sleep(time_s= 1):
    i = 0
    while(time_s >= i):
        time.sleep(1)
        i += 1

def divide_array(array, num_chips):
    # Calcula el tamaño de cada subarray
    chunk_size = len(array) // num_chips
    remainder = len(array) % num_chips

    subarrays = []
    start = 0

    for i in range(num_chips):
        end = start + chunk_size + (1 if i < remainder else 0)
        subarrays.append(array[start:end])
        start = end

    return subarrays

def forInArrayNumber(data, port):
    total_numbers = len(data)
    
    for date in enumerate(data):
        mensaje = send.msg(date[0], MSG_TORNER, port)
        response = mensaje.sendMessage()
        if response is None:
            # El servidor está caído, parar el hilo.
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            with open('log_msgEnviados.txt', 'a') as log:
                log.writelines(f"El servidor se cayó al enviar mensaje a {date[0]} a las {current_time} por el puerto {port}\n")
                log.writelines(f"El hilo se detuvo en el número {date[0]} de {data[-1][0]}\n")
            break
        else:
            current_time = datetime.now()
            formatted_time = current_time.strftime('%Y-%m-%d %H:%M:%S')
            with open('log_msgEnviados.txt', 'a') as log:
                log.writelines(f"Se envió mensaje a {date[0]} a las {formatted_time} por el puerto {port}\n")
            print(f"Se envió mensaje a {date[0]} por el puerto {port}")
            print("Delay de 15 segundos")
            sleep(15)
    else:
        with open('log_msgEnviados.txt', 'a') as log:
            log.writelines(f"El hilo completó todos los envíos para el puerto {port}. Total números: {total_numbers}\n")


def main():
    data_unilix_test = csv.csvReader(TEST_PATH)
    print(len(data_unilix_test.getData()))
    data = data_unilix_test.getDatainRange(0, 5879)
    subarrays = divide_array(data, NUMBER_SV)
    i = 1
    for array in subarrays:
        tb.printTabla(array)
        print(f"Subarray {i}")
        i+=1
        os.system("pause") 
    hilos = []
    i = 0
    for subarray in subarrays:
        hilo = threading.Thread(target=forInArrayNumber, args=(subarray, 4000 + i))
        hilos.append(hilo)
        hilo.start()
        i += 1
    
    for hilo in hilos:
        hilo.join()

    
def test_unilix():
    data_unilix_test = csv.csvReader(TEST_PATH)
    print(len(data_unilix_test.getData()))
    data = data_unilix_test.getDatainRange()
    subarrays = divide_array(data, NUMBER_SV)
    i = 1
    for array in subarrays:
        tb.printTabla(array)
        print(f"Subarray {i}")
        i+=1
        os.system("pause") 
    hilos = []
    i = 0
    for subarray in subarrays:
        hilo = threading.Thread(target=forInArrayNumber, args=(subarray, 4000 + i))
        hilos.append(hilo)
        hilo.start()
        i += 1
    
    for hilo in hilos:
        hilo.join()

if __name__ == "__main__":
    main()