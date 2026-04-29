from service.dbConnection import db, create_flask_app
from models.inventoryItem import InventoryItem

# TODO: Import Kafka
from service.kafkaStream import producer

# TODO: Import server components
from server.server import inventory_bp

# important: the app needs to be initialized in the wsgi entry-point (main.py) so that gunicorn can find it when running in production.
# If we initialize it in server/server.py, gunicorn won't be able to find the app and will throw an error.
app = create_flask_app()
app.register_blueprint(inventory_bp)

# Create tables if they don't exist
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    print(app.url_map)
    app.run(debug = True, host = "127.0.0.1", port = 5000)

# gunicorn entry point
if __name__ == "main":
    print("Starting Inventory Service...")
    print(app.url_map)
    # app.run(debug = True) not needed when running with gunicorn, as gunicorn will handle the server startup