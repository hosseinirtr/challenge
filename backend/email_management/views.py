from django.shortcuts import render
from email_management.tasks import send_email_task

def send_email_view(request, customer_id):
    # Assuming you have a subject and message to send
    subject = 'Your Subject'
    message = 'Your Message'

    # Trigger the Celery task
    send_email_task.delay(customer_id, subject, message)

    return render(request, 'email_sent.html')
