import falcon
from services.payment_service import PaymentService


class PaymentResource:
    def on_post(self, req, resp):
        data = req.media
        PaymentService.create_payment(data['invoice_id'], data['amount'])
        resp.status = falcon.HTTP_201
        resp.media = {'message': 'Payment added and configuration checked'}
