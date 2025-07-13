# WiFi Button Ping Counter

Este script en MicroPython está diseñado para placas como el ESP32 o ESP8266. Su función es establecer una conexión Wi-Fi cuando el usuario presiona un botón físico y luego realizar una solicitud HTTP (`ping`) a Google para verificar conectividad. 

Además, como parte de una interacción simple, el script cuenta cuántas veces se presiona el botón en un intervalo de 20 segundos. Esta funcionalidad puede utilizarse con fines educativos, pruebas de conectividad o como una introducción a la interacción física con dispositivos embebidos.

## 🔧 Funcionalidades principales

- ✅ Espera a que el usuario presione un botón para iniciar el proceso.
- 📶 Se conecta a una red Wi-Fi definida por el usuario (SSID y contraseña).
- 🌐 Verifica la conectividad a Internet realizando un `GET` a `https://www.google.com`.
- ⏱️ Cuenta las pulsaciones del botón durante un intervalo de 20 segundos.
- 📟 Muestra mensajes informativos por consola durante todas las etapas del proceso.

## 📎 Requisitos

- Placa ESP32 o ESP8266.
- MicroPython cargado en el dispositivo.
- Un botón físico conectado al pin GPIO 0 (u otro, modificando el script).
- Acceso a una red Wi-Fi de 2.4 GHz.

## 🔒 Seguridad

⚠️ Este script incluye la contraseña Wi-Fi en texto plano. Para usos reales o compartidos públicamente, se recomienda mover las credenciales a un archivo separado no versionado (`config.py`, por ejemplo) o usar variables de entorno.

## ✏️ Uso

1. Cargar el script en la placa usando `ampy`, `rshell`, `Thonny`, etc.
2. Reiniciar el dispositivo.
3. Presionar el botón para iniciar la conexión y el test.
4. Seguir las instrucciones mostradas por consola.
