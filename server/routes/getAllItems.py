from models.inventoryItem import InventoryItem
from server.server import inventory_bp
from server.errorHandler import handle_error

from flask import jsonify

@inventory_bp.route("/all", methods=["GET"])
def get_all_items():
    try:
        items = InventoryItem.query.all()

        return jsonify([
            {
                "id": str(item.id),
                "type": item.type.name,
                "modelName": item.model_name,
                "assignedTo": str(item.assigned_to) if item.assigned_to else None,
                "assigneeType": item.assignee_type.name if item.assignee_type else None
            }
            for item in items
        ]), 200

    except Exception as e:
        return handle_error(e, str(e))