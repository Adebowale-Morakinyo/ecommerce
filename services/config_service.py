from models import Configuration, Payment
from db import get_session
import logging

logger = logging.getLogger(__name__)


class ConfigService:
    @staticmethod
    def check_and_update(instance_type, instance_id):
        session = get_session()
        logger.info(f"Checking configuration for {instance_type} with ID {instance_id}")

        # Fetch relevant configuration
        config = session.query(Configuration).filter_by(instance_type=instance_type).first()

        if not config:
            logger.info(f"No configuration found for {instance_type}.")
            return

        logger.info(f"Configuration found for {instance_type}, applying updates.")

        # Fetch the instance based on type (payment, invoice, etc.)
        if instance_type == 'payment':
            payment = session.query(Payment).get(instance_id)
            invoice = payment.invoice  # Related invoice

            # Check the conditions in the config
            check_field = config.conditions['check_field']
            expected_value = config.conditions['expected_value']

            if getattr(invoice, check_field) == expected_value:
                # Perform actions (e.g., updating invoice status)
                for action in config.actions:
                    if action['action_type'] == 'update':
                        setattr(invoice, action['target_field'], action['new_value'])
                    if action['action_type'] == 'notify':
                        # Send notification logic (e.g., send email)
                        pass

                session.commit()
