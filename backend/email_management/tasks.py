from celery import shared_task, current_task
from django.core.mail import send_mail
from .models import Customer

@shared_task(bind=True)
def send_email_task(self, customer_id, subject, message):
    try:
        customer = Customer.objects.get(id=customer_id)
        send_mail(subject, message, customer.sender, [customer.email])
        customer.status = 'sent'
        customer.save()
    except Customer.DoesNotExist:
        # Handle the case where the customer doesn't exist
        pass
    except Exception as e:
        # Report failure
        self.update_state(state='FAILURE', meta={'exception': str(e)})
    finally:
        # Report completion
        async_to_sync(self.send_progress)({'message': 'Email sent successfully!'})
