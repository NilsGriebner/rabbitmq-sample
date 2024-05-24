import ssl
import pika, sys, os


def main():
    creds = pika.PlainCredentials("user", "password")

    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    ssl_options = pika.SSLOptions(context)

    connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='host',
        ssl_options=ssl_options,
        credentials=creds
    ))
    channel = connection.channel()

    channel.queue_declare(queue='hello')

    def callback(ch, method, properties, body):
        print(f" [x] Received {body}")

    channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
