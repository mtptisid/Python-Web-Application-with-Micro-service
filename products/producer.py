import pika, json

params = pika.URLParameters('amqps://wyfmfnce:QBUxqUgh2jzR9hzdZfWOKMAfWCu5ZvcS@puffin.rmq2.cloudamqp.com/wyfmfnce')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)