import pytest
from rest_framework.test import APIClient
from factories import CounterFactory
from factories import UserFactory


@pytest.mark.django_db
def test_model_counter(monkeypatch):
    """В процессе теста создаем два счетчика,
    увеличиваем и уменьшаем их значения"""

    #первый счетчик
    counter1 = CounterFactory()

    assert counter1.count == 0

    counter1.increment()
    counter1.increment()
    assert counter1.count == 2

    counter1.decrement()
    assert counter1.count == 1

    counter1.decrement()
    assert counter1.count == 0

    #проверяем не стало ли значение ниже 0
    counter1.decrement()
    assert counter1.count == 0

    #второй счетчик
    counter2 = CounterFactory()
    assert counter2.count == 0

    counter2.increment()
    counter2.increment()
    counter2.increment()
    counter2.increment()
    assert counter2.count == 4

    counter2.decrement()
    assert counter2.count == 3

    #проверяем не изменилось ли значение 1-го счетчика
    assert counter1.count == 0


@pytest.mark.django_db
def test_view_counter():
    """Тестирование механизма через вьюхи"""

    client = APIClient()

    user1 = UserFactory()
    client.force_authenticate(user=user1)

    response = client.get('/count/')
    assert response.data == 0

    response = client.post('/count/')
    assert response.data == 'ok'

    response = client.get('/count/')
    assert response.data == 1

    response = client.post('/count/')
    assert response.data == 'ok'

    response = client.get('/count/')
    assert response.data == 2

    response = client.delete('/count/')
    assert response.data == 'ok'

    response = client.get('/count/')
    assert response.data == 1

    response = client.delete('/count/')
    assert response.data == 'ok'

    response = client.get('/count/')
    assert response.data == 0

    response = client.delete('/count/')
    assert response.data == 'ok'

    response = client.get('/count/')
    assert response.data == 0

