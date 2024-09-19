import falcon
from models import Invoice
from db import get_session


class InvoiceResource:
    def on_get(self, req, resp):
        session = get_session()
        
        # Retrieve invoices
        invoices = session.query(Invoice).all()
        resp.status = falcon.HTTP_200
        resp.media = [invoice.serialize() for invoice in invoices]
