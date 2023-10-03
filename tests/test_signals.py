import pytest
from orders.models import Order
from orders.signals import post_save_robot
from robots.models import Robot
from django.core import mail


ACCEPT_TRUE = 1
ACCEPT_FALSE = 0


@pytest.mark.django_db
def test_post_save_robot_existing_orders_true(robot, customer):
    """Тест проверят что эмеил отправляется при вызове сигнала."""
    Order.objects.create(robot_serial=robot.serial, customer=customer)

    post_save_robot(sender=Robot, instance=robot)

    assert len(mail.outbox) == ACCEPT_TRUE, (
        f'Колличество отправленных эмейлов {len(mail.outbox)}, '
        f'должно быть {ACCEPT_TRUE}'
        )
    assert Order.objects.count() == ACCEPT_FALSE, ('Объект не удалился из бд')


@pytest.mark.django_db
def test_post_save_robot_existing_orders_false(customer, robot):
    """Тест проверяет что эмеил не отправляется если в базе создан другой робот."""
    Order.objects.create(robot_serial='R2-D3', customer=customer)

    post_save_robot(sender=Robot, instance=robot)

    assert len(mail.outbox) == ACCEPT_FALSE, (
        f'Колличество отправленных эмейлов {len(mail.outbox)}, '
        f'должно быть {ACCEPT_FALSE}'
        )
    assert Order.objects.count() == ACCEPT_TRUE, ('Объект остался в базе')
