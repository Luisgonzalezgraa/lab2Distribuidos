# Proyecto Kafka - Spark con Python

El proyecto consiste en realizar análisis en tiempo real de la información de navegación de los usuarios de un E-commerce de Falabella. Para lo cual se emula mediante Python, el envío de la información del usuario y el producto comprado junto con el número de folio a un cluster de kafka, compuesto por 3 máquinas. Para simular el envío de los datos, se realizó un script en Python 'transmisor_datos_kafka.py' el cual genera datos aleatorios.

Posteriormente se recibe la información, haciendo uso del toíco (DataTopic) y se procesa con Spark y la API de SQL, en la cual se analiza la información recibida y se envía una notificación al usuario de la compra realizada con el número de folio generado para dicha compra, el folio solo se agregará si el tiempo de compra no es 0, si la persona compro y se demoró x tiempo se enviara un mensaje, esto para mitigar los casos donde las compras exceden un maximo de tiempo y puedan generar un error a la hora de adquerir un producto. Si el tiempo de compra es mayor a 30 segundos se enviará un mensaje donde se adjuntara el número de folio y si existió algun problema en la plataforma para que se pueda contactar con Falabella, en caso contrario se envia un mensaje diferente donde se agradece la preferencia.

## Pasos para ejecutar el Proyecto
## ANTES
Acceder a la carpeta cd .\Kafka-Spark-Distribuidos
Luego acceder a cd .\Proyecto-Spark-Kafka-main

### 1) Levantar los Contenedores

Se abre una terminal en la carpeta del proyecto y se ejecuta el siguiente comando:

```bash
docker-compose.yml
```
o 

```bash
docker-compose up -l
```
Para concer los nombres de los contenedores levantados, ejecutamos:

```bash
docker ps
```

### 2)Crear un tópico

```bash
docker exec -it kafka1-p bash
```

```bash
kafka-topics --bootstrap-server localhost:9092 --create --topic DataTopic --replication-factor 3 --partitions 3
```

### 3) Instalando las librerías en Kafka1-p

Dado que vamos a usar la maquina 'kfaka1-p' para generar la data y enviarla mediante Kafka, se hace necesario instalar la librería de Python, para enviar datos a Kafka.

```bash
pip install kafka-python
```

### 4) Generamos y trasnmitimos los Datos

 Posteriormente nos dirigimos a la ruta en linux **opt/project/code/producer** donde primero deberas colocar el comando cd /opt/project/code/producer/ 

```bash
python transmisor_datos_kafka.py
```

### 5) Análisis en Tiempo Real con Spark y Envío de Notificación
Para ejecutar el script 'notification.py', se ingresa al Spark Master

```bash
docker exec -it proyecto-spark-kafka-main-spark-1 bash
```

Para ejecutar el script:

```bash
spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.1.2 /opt/spark/code/consumer/notification.py
```
## Resultado

Se generan datos ficticios, se nevían al tópico DataTopic, análsis con Spark y notificación al cliente

## ATENCIÓN

Necesitarás 3 terminales para correr la maqueta, una para levantar Docker, otra para Kafka y otra para Spark. En el lado de Spark podra visualizar los datos enviados.