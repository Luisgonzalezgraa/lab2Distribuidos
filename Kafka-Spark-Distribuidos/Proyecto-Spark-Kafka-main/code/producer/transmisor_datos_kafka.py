import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from clases.generador_json_datos_personas import GeneradorJSONDatosPersonas
from kafka import KafkaProducer
import time

# Configuración del Kafka
bootstrap_servers = 'localhost:9092'  # Cambia esto si tu servidor Kafka tiene una configuración diferente
topic_name = 'DataTopic'  # Cambia esto por el nombre de tu topic


while True:

    # Crear un productor Kafka
    producer = KafkaProducer(bootstrap_servers=bootstrap_servers)

    # Geneara datos (mensaje) que se enviará al topic
    gen_datos_persona = GeneradorJSONDatosPersonas()
    datos_persona = gen_datos_persona.generar_json_datos_personas()
    print(datos_persona)

    producer.send(topic_name, value=str(datos_persona).encode('utf-8'))
    # Cerrar el productor
    producer.close()
    time.sleep(2)  # Esperar 2 segundos antes de enviar el próximo mensaje
    
