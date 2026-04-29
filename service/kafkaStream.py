from kafka import KafkaProducer
from config.kafkaConfig import KafkaConfig

producer = KafkaProducer(
    bootstrap_servers=f"{KafkaConfig.HOST}:{KafkaConfig.PORT}",
    security_protocol="SSL",
    ssl_cafile=f"{KafkaConfig.CERT_DIR}/ca.pem",
    ssl_certfile=f"{KafkaConfig.CERT_DIR}/service.cert",
    ssl_keyfile=f"{KafkaConfig.CERT_DIR}/service.key",
)

if producer.bootstrap_connected():
    print(f"Kafka producer initialized for topic '{KafkaConfig.TOPIC}' at {KafkaConfig.HOST}:{KafkaConfig.PORT}")