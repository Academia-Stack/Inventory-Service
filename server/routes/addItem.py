from models.inventoryItem import InventoryItem, db
from server.errorHandler import handle_error
from flask import request, jsonify
from server.server import inventory_bp
from utils.validator import InventoryValidator

@inventory_bp.route("/add", methods=["POST"])
def add_item():
    validation_errors = []

    try:
        data = request.json

        item = InventoryItem(
            type=data["type"],
            model_name=data["modelName"],
            assigned_to=data.get("assignedTo"),
            assignee_type=data.get("assigneeType")
        )

        validation_errors = InventoryValidator.validate(data)

        if len(validation_errors) > 0:
            errors = [e['error'] for e in validation_errors]
            raise ValueError(', '.join(errors))

        db.session.add(item)
        db.session.commit()

        return jsonify({"message": "Item added", "id": str(item.id)}), 201

    except ValueError as ve:
        print(f"Validation error in add_item: {ve}")
        return handle_error(ve, validation_errors, 400)

    except Exception as e:
        print(f"Error in add_item: {str(e)}")
        return handle_error(e, str(e))