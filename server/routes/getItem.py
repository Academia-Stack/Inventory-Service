from models.inventoryItem import InventoryItem
from server.server import inventory_bp
from flask import jsonify

from server.errorHandler import handle_error

@inventory_bp.route("/<item_id>", methods=["GET"])
def get_item(item_id):
    try:
        item = InventoryItem.query.get(item_id)

        if not item:
            return jsonify({"error": "Item not found"}), 404

        return jsonify({
            "id": str(item.id),
            "type": item.type.name,
            "modelName": item.model_name,
            "assignedTo": str(item.assigned_to) if item.assigned_to else None,
            "assigneeType": item.assignee_type.name if item.assignee_type else None
        }), 200

    except Exception as e:
        return handle_error(e, str(e))