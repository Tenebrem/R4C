from django.db.models.signals import post_save
from django.dispatch import receiver
from robots.models import Robot
from .models import Order
from django.core.mail import send_mail


@receiver(post_save, sender=Robot)
def post_save_robot(sender, instance, **kwargs):
    """Отправляет меил при если робот создан и он был в очереди"""
    existing_orders = Order.objects.filter(
        robot_serial=instance.serial
    )

    if existing_orders.exists():
        subject = 'Добрый день!'
        message = (f'Недавно вы интересовались нашим роботом модели {instance.model}, версии {instance.version}.'
                    'Этот робот теперь в наличии. Если вам подходит этот вариант - пожалуйста, свяжитесь с нами'
        )
        from_email = 'robot@gmail.com'
        for order in existing_orders:
            recipient_email = order.customer.email
            send_mail(subject, message, from_email, [recipient_email])
        # сообщение отпрвлено, больше ему не надо находиться в очереди
        existing_orders.delete()
