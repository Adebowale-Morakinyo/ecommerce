from models import Payment
from db import get_session
from services.config_service import ConfigService
import logging


logger = logging.getLogger(__name__)


class PaymentService:
    @staticmethod
    def create_payment(invoice_id, amount):
        session = get_session()
        logger.info(f"Creating payment for invoice {invoice_id} with amount {amount}")

        payment = Payment(invoice_id=invoice_id, amount=amount)
        session.add(payment)
        session.commit()

        # Trigger configuration checks based on payment
        ConfigService.check_and_update('payment', payment.id)
        logger.info(f"Payment {payment.id} created and processed for configuration.")
