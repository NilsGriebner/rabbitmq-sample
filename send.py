import ssl
import pika


creds = pika.PlainCredentials("user", "password")
context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
ssl_options = pika.SSLOptions(context)
connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host='host',
        port=5671,
        credentials=creds,
        ssl_options=ssl_options
    ))
channel = connection.channel()
channel.queue_declare(queue='catia')
channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')

print(" [x] Sent 'Hello World!'")

connection.close()
