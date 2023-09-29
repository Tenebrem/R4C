import pytest
from customers.models import Customer
from robots.models import Robot
from datetime import datetime
from orders.models import Order


@pytest.fixture
def customer():
    return Customer.objects.create(email='test.email@gmil.com')


@pytest.fixture
def robot():
    robots = Robot(
              model='R3',
              version='D2',
              created=datetime.now()
        )

    return robots


@pytest.fixture
def order(customer):
    order = Order.objects.create(
        customer=customer,
        robot_serial='R2-D2'
    )
    return order
