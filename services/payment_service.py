from models import Payment
from db import get_session
from services.config_service import ConfigService


class PaymentService:
    @staticmethod
    def create_payment(invoice_id, amount):
        session = get_session()

        payment = Payment(invoice_id=invoice_id, amount=amount)
        session.add(payment)
        session.commit()

        # Trigger configuration checks based on payment
        ConfigService.check_and_update('payment', payment.id)
