import modules.csv_reader_data as csv
import modules.sendMessage as send
import modules.Table as tb
import time
import threading
import os 

PATH_CSV = './database/date_yachay.csv'

TEST_PATH = './database/test.csv'

NUMBER_SV = 3   

MESSAGE = """🎉Hola {name}, te saludamos de la Academia YACHAYWASI🎉
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

TEST_MESSAGE = """
Hola {name}, te saluda Unilix 🎉
📢 Estamos enviando mensajes de prueva, para verificar los numeros vinculado
📌 Esperamos no sea una molestia 😁.
"""
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
        mensaje = send.msg(date[2], MESSAGE.format(name = date[1]), port)
        mensaje.sendMessage()
        print(f"Se envio mensaje a {date[2]} - {date[1]} por el puerto {port}")
        print("Delay de 15 segundos")
        time.sleep(14)

def main():
    data_unilix_test = csv.csvReader(PATH_CSV)
    print(len(data_unilix_test.getData()))
    data = data_unilix_test.getDatainRange(500, len(data_unilix_test.getData()))
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

    
def test():
    data_unilix_test = csv.csvReader(TEST_PATH)
    data = data_unilix_test.getData()
    subarrays = divide_array(data, NUMBER_SV)
    for array in subarrays:
        print(array)   
    hilos = []
    i = 0
    for subarray in subarrays:
        hilo = threading.Thread(target=forInArrayNumber, args=(subarray, 3000 + i))
        hilos.append(hilo)
        hilo.start()
        i += 1
    
    for hilo in hilos:
        hilo.join()

if __name__ == "__main__":
    main()