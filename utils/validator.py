import re
import uuid
from models.inventoryItem import ItemType, AssigneeType

class InventoryValidator:

    MODEL_NAME_REGEX = re.compile(r'^[a-zA-Z0-9 .\-]+$')
    SUSPICIOUS_PATTERNS = ["<script", "</script", "javascript:", "onerror=", "onload="]

    @staticmethod
    def validate(data: dict):
        errors = []

        def add_error(field, message):
            errors.append({
                "fieldName": field,
                "error": message
            })

        # --- TYPE VALIDATION ---
        item_type = data.get("type")
        if item_type not in [e.value for e in ItemType]:
            add_error("type", "Invalid item type")

        # --- MODEL NAME VALIDATION ---
        model_name = (data.get("modelName") or "").strip()

        if not model_name:
            add_error("modelName", "Model name cannot be empty")

        elif len(model_name) > 100:
            add_error("modelName", "Model name cannot exceed 100 characters")

        elif not InventoryValidator.MODEL_NAME_REGEX.match(model_name):
            add_error("modelName", "Model name contains invalid characters")

        else:
            # XHR / XSS check ONLY for modelName
            lower_model = model_name.lower()
            for pattern in InventoryValidator.SUSPICIOUS_PATTERNS:
                if pattern in lower_model:
                    add_error("modelName", "Model name contains suspicious input")
                    break

        # --- ASSIGNMENT VALIDATION ---
        assigned_to = data.get("assignedTo")
        assignee_type = data.get("assigneeType")

        if (assigned_to and not assignee_type) or (assignee_type and not assigned_to):
            add_error("assignment", "assignedTo and assigneeType must be provided together")

        if assigned_to:
            try:
                uuid.UUID(assigned_to)
            except Exception:
                add_error("assignedTo", "Invalid UUID")

        if assignee_type:
            if assignee_type not in [e.value for e in AssigneeType]:
                add_error("assigneeType", "Invalid assignee type")

        return errors