import modules.csv_reader_data as csv
import modules.sendMessage as send
import modules.Table as tb
import time
import threading
import os 

TEST_PATH = './database/test.csv'

NUMBER_SV = 1

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

MSF_NEWCOMANDS = """📢Hola ya tienes dispoibles nuevos comando para enviar:
    - !info: Muestra información de la academia
    - !ubicacion: Muestra la ubicación de la academia"""

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
    for date in data:
        # mensaje = send.msg(date[2], MESSAGE.format(
        #     name = date[1], 
        #     pay_money = MONEY_MSG, 
        #     date_start = START_DATE,
        #     phones = PHONES,
        #     address = ADDRESS
        #     ), port)
        mensaje = send.msg(date[2], MSF_NEWCOMANDS, port)
        mensaje.sendMessage()
        print(f"Se envio mensaje a {date[2]} - {date[1]} por el puerto {port}")
        print("Delay de 15 segundos")
        sleep(14)

def main():
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