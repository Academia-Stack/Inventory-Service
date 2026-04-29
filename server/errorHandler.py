from models.logEntry import LogEntry
from config.kafkaConfig import KafkaConfig
from service.kafkaStream import producer

import json
from flask import request, jsonify

def handle_error(e, obj, status_code = 500):
    log = LogEntry.create(
        message=str(e),
        endpoint=request.path,
        method=request.method,
        exception_class=e.__class__.__name__
    )
    print(f"Error occurred: {log.to_dict()}")

    bytes_data = json.dumps(log.to_dict()).encode("utf-8")
    producer.send(
        key = log.logId.encode("utf-8"),
        topic = KafkaConfig.TOPIC,
        value = bytes_data)
    return jsonify({"error(s)": obj}), status_code
