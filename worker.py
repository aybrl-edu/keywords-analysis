import json
from kafka import KafkaConsumer


def consume_kafka(topic):
    print("reading from kafka topic...")

    consumer = KafkaConsumer(
        topic,
        bootstrap_servers=['172.31.253.152:9092'],
        auto_offset_reset='earliest',
        enable_auto_commit=False,
        group_id=None
    )

    messages = []
    timeout_ms = 1000  # Set the timeout in milliseconds

    while True:
        msg_pack = consumer.poll(timeout_ms=timeout_ms)

        if not msg_pack:
            break

        for tp, msgs in msg_pack.items():
            for msg in msgs:
                msg_dict = json.loads(msg.value.decode('utf-8'))
                msg_str = json.dumps(msg_dict, ensure_ascii=False)
                messages.append(msg_str)

    consumer.close()
    return messages
