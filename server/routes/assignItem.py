import uuid

from models.inventoryItem import InventoryItem, db
from server.errorHandler import handle_error
from flask import request, jsonify
from server.server import inventory_bp
from models.inventoryItem import AssigneeType

@inventory_bp.route("/assign/<item_id>", methods=["PUT", "POST"])
def assign_item(item_id):
    validation_errors = []

    def add_error(field, message):
        validation_errors.append({
            "fieldName": field,
            "error": message
        })

    try:
        data = request.json

        item = InventoryItem.query.get(item_id)
        if not item:
            return jsonify({"error": "Item not found"}), 404
        
        if not data.get("assignedTo"):
            add_error("assignedTo", "Assigned To is required")

        if not data.get("assigneeType"):
            add_error("assigneeType", "Assignee Type is required")

        try:
            uuid.UUID(data["assignedTo"])
        except Exception:
            add_error("assignedTo", "Invalid UUID")

        if data["assigneeType"] not in [e.value for e in AssigneeType]:
            add_error("assigneeType", "Invalid assignee type")

        item.assigned_to = data["assignedTo"]
        item.assignee_type = data["assigneeType"]

        if len(validation_errors) > 0:
            errors = [e['error'] for e in validation_errors]
            raise ValueError(', '.join(errors))

        db.session.commit()
        return jsonify({"message": "Item assigned"})

    except ValueError as ve:
        print(f"Validation error in assign_item: {ve}")
        return handle_error(ve, validation_errors, 400)

    except Exception as e:
        return handle_error(e, str(e))