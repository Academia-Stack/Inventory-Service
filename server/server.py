from flask import Blueprint

inventory_bp = Blueprint("inventory", __name__, url_prefix="/inventory")

# TODO: Import all routes
from server.routes.addItem import add_item
from server.routes.getAllItems import get_all_items
from server.routes.getItem import get_item
from server.routes.assignItem import assign_item
from server.routes.deleteItem import delete_item