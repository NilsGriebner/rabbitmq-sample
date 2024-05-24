# rabbitmq-sample

This is quickstart code on how to send and receive messages with RabbitMQ. The code was taken from the
[RabbitMQ tutorial - "Hello World!"](https://www.rabbitmq.com/tutorials/tutorial-one-python) and briefly
modified to work with AwsMQ.

## Run the code

In order to run the code credentials and the hostname of an AwsMQ instance are needed.

Install dependencies with

```
pipenv sync
pipenv shell
```

Then you can use this code like this:

Open two shell sessions. In the first run

```shell
python receive.py
```

and in the second

```shell
python send.py
```

You should see something like:

```
 [*] Waiting for messages. To exit press CTRL+C
 [x] Sent 'Hello World!'
 [x] Received b'Hello World!'
```

