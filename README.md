# Inventory Service API Documentation

## Data Model for Inventory Item

```json
{
  "id": "UUID",
  "type": "LAPTOP | HEADPHONE | MOUSE | SPEAKER | WEBCAM",
  "modelName": "string",
  "assignedTo": "UUID | null",
  "assigneeType": "STUDENT | TEACHER | null"
}
```

---

## Endpoints

### 1. Create Inventory Item

**Endpoint**

```http
POST /inventory/add
```

**Description**
Creates a new inventory item.

**Request Body**

```json
{
  "type": "LAPTOP",
  "modelName": "Dell XPS 13",
  "assignedTo": null,
  "assigneeType": null
}
```

**Response**

```json
{
  "message": "Item added",
  "id": "uuid"
}
```

**Status Codes**

* 201 Created — Item successfully created
* 500 Internal Server Error — Failure during processing

---

### 2. Get Inventory Item by ID

**Endpoint**

```http
GET /inventory/{id}
```

**Description**
Retrieves a single inventory item by its unique identifier.

**Response**

```json
{
  "id": "uuid",
  "type": "LAPTOP",
  "modelName": "Dell XPS 13",
  "assignedTo": null,
  "assigneeType": null
}
```

**Status Codes**

* 200 OK — Item retrieved successfully
* 404 Not Found — Item does not exist
* 500 Internal Server Error — Failure during processing

---

### 3. Get All Inventory Items

**Endpoint**

```http
GET /inventory/all
```

**Description**
Retrieves all inventory items.

**Response**

```json
[
  {
    "id": "uuid",
    "type": "MOUSE",
    "modelName": "Logitech G102",
    "assignedTo": null,
    "assigneeType": null
  }
]
```

**Status Codes**

* 200 OK — Items retrieved successfully
* 500 Internal Server Error — Failure during processing

---

### 4. Assign Inventory Item

**Endpoint**

```http
PUT /inventory/assign/{id}
```

**Description**
Assigns an inventory item to a user (student or teacher).

**Request Body**

```json
{
  "assignedTo": "uuid",
  "assigneeType": "STUDENT"
}
```

**Response**

```json
{
  "message": "Item assigned"
}
```

**Status Codes**

* 200 OK — Item assigned successfully
* 404 Not Found — Item does not exist
* 500 Internal Server Error — Failure during processing

---

### 5. Delete Inventory Item

**Endpoint**

```http
DELETE /inventory/delete/{id}
```

**Description**
Deletes an inventory item by its unique identifier.

**Response**

```json
{
  "message": "Item deleted",
  "id": "uuid"
}
```

**Status Codes**

* 200 OK — Item deleted successfully
* 404 Not Found — Item does not exist
* 500 Internal Server Error — Failure during processing
***
## Command to run app
## Start virtual environment
```bash
source .myVenv/bin/activate
```
## Start the server
```bash
gunicorn -b 127.0.0.1:5000 main:app
```
***
