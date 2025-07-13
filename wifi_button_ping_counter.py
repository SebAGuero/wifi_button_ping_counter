import machine
import time
import network
import urequests

# Configuración del pin para el botón
button = machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_UP)
#cambio para github
#desde web 0001_01
#MARCOS
#MARCOS 2

#otro cambio
#cambio importante
#new branch
# Variables de Wi-Fi
ssid = 'Fibertel WiFi480 2.4GHz'  # Tu SSID
password = '00429605255'  # Tu contraseña

# Función para conectar al Wi-Fi con un timeout
def connect_wifi(timeout=30):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.disconnect()  # Desconectar cualquier conexión previa
    if not wlan.isconnected():
        print('Conectando a la red Wi-Fi...')
        wlan.connect(ssid, password)
        start_time = time.time()  # Captura el tiempo de inicio
        while not wlan.isconnected():
            print("Esperando a que se establezca la conexión Wi-Fi...")
            if time.time() - start_time > timeout:
                print("Error: No se pudo conectar al Wi-Fi en el tiempo límite.")
                return False
            time.sleep(1)
    print('Conexión establecida con la red Wi-Fi. IP:', wlan.ifconfig()[0])
    return True

# Función para hacer un ping a Google
def ping_google():
    try:
        print("Haciendo ping a Google...")
        response = urequests.get('https://www.google.com', timeout=10)  # Timeout en 10 segundos
        if response.status_code == 200:
            print('¡Conexión exitosa a Google!')
            print('¡Presione el boton la maxima cantidad de veces posible en 20s!')
        else:
            print(f'Error en la conexión a Google. Código de estado: {response.status_code}')
        response.close()  # Cerrar la respuesta
    except Exception as e:
        print('Error al hacer ping a Google:', e)

# Función para contar pulsos del botón durante 20 segundos
def count_button_presses(interval=20):
    press_count = 0
    start_time = time.time()
    while time.time() - start_time < interval:  # Contar durante 20 segundos
        if button.value() == 0:  # El botón está presionado
            press_count += 1
            print(f"Botón presionado {press_count} veces.")
            time.sleep(0.5)  # Esperar un poco para evitar el rebote del botón
        time.sleep(0.1)  # Pausa para evitar un uso excesivo del CPU
    print(f"Total de pulsos en {interval} segundos: {press_count}")
    return press_count

# Mensaje inicial
print("Por favor, presiona el botón para conectar al Wi-Fi y hacer un ping a Google.")

# Espera a que se presione el botón
while True:
    if button.value() == 0:  # El botón está presionado
        print("Botón presionado, conectando a WiFi...")
        if connect_wifi(timeout=30):  # Tiempo límite de 30 segundos para la conexión
            ping_google()
            # Contamos los pulsos del botón durante 20 segundos
            count_button_presses(interval=20)
        break  # Termina el ciclo una vez que se hizo el ping y se conectó a WiFi
    else:
        print("Esperando que presiones el botón...")  # Feedback para el usuario
    time.sleep(0.05)  # Retardo pequeño para evitar el rebote del botón