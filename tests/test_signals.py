import pytest
from orders.models import Order
from orders.signals import post_save_robot
from robots.models import Robot
from django.core import mail


@pytest.mark.django_db
def test_post_save_robot_existing_orders(robot, customer):
    """Тест проверят что эмеил отправляется при вызове сигнала."""
    Order.objects.create(robot_serial=robot.serial, customer=customer)

    post_save_robot(sender=Robot, instance=robot)

    assert len(mail.outbox) == 1
    assert mail.outbox[0].subject == 'Добрый день!'
    assert 'robot@gmail.com' in mail.outbox[0].from_email
    assert 'test.email@gmil.com' in mail.outbox[0].to


@pytest.mark.django_db
def test_post_save_robot_existing_orders_false(customer, robot):
    Order.objects.create(robot_serial='R2-D3', customer=customer)

    post_save_robot(sender=Robot, instance=robot)

    assert len(mail.outbox) == 0

