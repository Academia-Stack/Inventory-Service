from models.inventoryItem import InventoryItem, db
from server.errorHandler import handle_error
from flask import request, jsonify
from server.server import inventory_bp

@inventory_bp.route("/delete/<item_id>", methods=["GET", "DELETE"])
def delete_item(item_id):
    try:
        item = InventoryItem.query.get(item_id)

        if not item:
            return jsonify({"error": "Item not found"}), 404

        db.session.delete(item)
        db.session.commit()

        return jsonify({"message": "Item deleted", "id": item_id}), 200

    except Exception as e:
        return handle_error(e, str(e))