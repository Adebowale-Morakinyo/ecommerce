import falcon
from db import engine
from models import Base
from resources.payment_resource import PaymentResource
from resources.invoice_resource import InvoiceResource
from resources.config_resource import ConfigResource
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize Falcon API
app = falcon.App()

# Route definitions
payment_resource = PaymentResource()
invoice_resource = InvoiceResource()
config_resource = ConfigResource()

app.add_route('/payments', payment_resource)
app.add_route('/invoices', invoice_resource)
app.add_route('/configs', config_resource)


# Create tables automatically when the app starts
def create_tables():
    logger.info("Creating all tables if they don't exist.")
    Base.metadata.create_all(bind=engine)


# App startup hook to create tables
create_tables()

# Gunicorn will be used in production, no need for __main__ block
"""
if __name__ == '__main__':
    # For local development, you can run the app using a WSGI server like Gunicorn
    logger.info("Starting the app...")
    from wsgiref import simple_server

    httpd = simple_server.make_server('127.0.0.1', 8000, app)
    httpd.serve_forever()
"""
