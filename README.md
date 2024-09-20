---

## Project Title: **Dynamic Configuration Payment System**

### Project Overview:
This project is a simple payment management system that allows dynamic configuration of payment thresholds for customers. It includes functionality to:
- Add and manage customer payments.
- View invoices and manage payment-related configurations dynamically.
- Ensure scalability and easy maintenance via configurable settings stored in a database.

### Features:
- API to add payments.
- API to view invoices.
- API to configure payment-related settings.
- SQLite database used for local testing and development.
- Automatic table creation at app startup.
- Centralized logging and database session management.

---

## Installation Instructions

### 1. Clone the Repository:
```bash
git clone <repo-url>
cd <project-directory>
```

### 2. Create and Activate Virtual Environment (Optional but recommended):
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### 3. Install Dependencies:
```bash
pip install -r requirements.txt
```

### 4. Run the Application:
```bash
python app.py
```
The app will start on `http://127.0.0.1:8000`.

---

## Testing the Endpoints with Postman:

### 1. Add Payment
**Endpoint**: `POST /payments`

**Request**:
```json
{
    "invoice_id": 1,
    "amount": 500
}
```

**Response**:
```json
{
    "message": "Payment added and configuration checked"
}
```

### 2. View Invoices
**Endpoint**: `GET /invoices`

**Response**:
```json
[
    {
        "invoice_id": 1,
        "customer_id": 101,
        "amount_due": 500,
        "status": "Paid",
        "payment_date": "2023-09-19"
    },
    {
        "invoice_id": 2,
        "customer_id": 102,
        "amount_due": 300,
        "status": "Unpaid",
        "payment_date": null
    }
]
```

### 3. Add/Update Configurations
**Endpoint**: `POST /configs`

**Request**:
```json
{
    "instance_type": "payment",
    "conditions": {
        "check_field": "status",
        "expected_value": "Unpaid"
    },
    "actions": [
        {
            "action_type": "update",
            "target_field": "status",
            "new_value": "Paid"
        }
    ]
}
```

**Response**:
```json
{
    "message": "Configuration added successfully"
}
```

---

## Database Configuration:
This app uses SQLite for local testing. The database will automatically be created and updated when the app starts. The database schema includes:
- **Customers**: Stores customer details.
- **Invoices**: Manages invoices related to payments.
- **Payments**: Logs payments made by customers.
- **Configurations**: Stores dynamic configurations for customers (e.g., payment thresholds).

---

## Project Structure:

```
/project-directory
├── app.py                 # Main application file
├── db.py                  # Centralized database connection and session management
├── models.py              # SQLAlchemy models
├── services/              # Business logic for payments, invoices, and configurations
│   ├── payment_service.py
│   ├── invoice_service.py
│   └── config_service.py
├── resources/             # API resource classes
│   ├── payment_resource.py
│   ├── invoice_resource.py
│   └── config_resource.py
├── requirements.txt       # Project dependencies
└── README.md              # Project documentation
```

---

## Logging:
The project has basic logging enabled. Logs can be viewed in the console when the application runs. You can adjust the logging level in `app.py`.

---

## Future Improvements:
- Integrate more advanced error handling and input validation.
- Implement authentication and authorization.
- Add support for more robust database systems for production (PostgreSQL, MySQL).

---