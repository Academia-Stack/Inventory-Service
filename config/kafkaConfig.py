import os
from dotenv import load_dotenv

# TODO: Load environment variables from .env file
load_dotenv()

class KafkaConfig:
    HOST = os.getenv("KAFKA_HOST_NAME")
    PORT = os.getenv("KAFKA_PORT")
    TOPIC = os.getenv("TOPIC")
    CERT_DIR = os.getenv("CERT_DIR")