import paho.mqtt.client as mqtt
import psutil
import time
import ssl
import datetime
import os

# Generera ett unikt id för varje session och hämta nuvarande arbetssökväg
now = datetime.datetime.now()

# MQTT-inställningar
MQTT_BROKER = "localhost"  # Använd localhost som värd
MQTT_PORT = 8883
MQTT_TOPIC = "sensor/virtual"

# Certifikatens sökvägar (anpassade för sekretess)
CA_CERT = "directory_to/ca.crt"
CLIENT_CERT = "directory_to/client.crt"
CLIENT_KEY = "directory_to/client.key"

# Kontrollera att certifikatfilerna existerar
for cert_path in [CA_CERT, CLIENT_CERT, CLIENT_KEY]:
    if not os.path.isfile(cert_path):
        raise ValueError(f"Certifikatfil ej hittad: {cert_path}")

# Skapa en MQTT-klient
client = mqtt.Client(client_id="VirtualSensorClient")

# Använd mTLS (mutual TLS)
ssl_context = ssl.create_default_context()
ssl_context.keylog_filename = os.path.join(os.getcwd(), "log", f"sslkeylog_{now.strftime('%Y-%m-%d_%H-%M-%S')}.log")
ssl_context.load_cert_chain(CLIENT_CERT, keyfile=CLIENT_KEY)
ssl_context.load_verify_locations(CA_CERT)

client.tls_set_context(ssl_context)
client.tls_insecure_set(True)  # Inaktivera värdnamnskontroll för utveckling

# Callback-funktioner för MQTT-händelser
client.on_connect = lambda client, userdata, flags, rc: print(f"Ansluten till MQTT Broker. Kod: {rc}")
client.on_disconnect = lambda client, userdata, rc: print(f"Frånkopplad från MQTT Broker. Kod: {rc}")
client.on_publish = lambda client, userdata, mid: print(f"Meddelande publicerat med ID: {mid}")

# Anslut till MQTT-brokern
client.connect(MQTT_BROKER, MQTT_PORT, 60)
client.loop_start()  # Starta loop för händelser

try:
    while True:
        # Kolla batterinivån på datorn
        battery = psutil.sensors_battery()
        if battery:
            battery_level = battery.percent
            # Skicka batterinivån till MQTT topic
            result = client.publish(MQTT_TOPIC, f"Batterinivå: {battery_level}%")
            result.wait_for_publish(1)
            print(f"Skickade batterinivå: {battery_level}%")
        else:
            print("Ingen batteridata tillgänglig.")

        time.sleep(10)

except KeyboardInterrupt:
    print("Stänger ner...")
    client.loop_stop()
    client.disconnect()
