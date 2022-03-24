from django.test import TestCase
from django.urls import reverse

from Support.models import CategoryMessage, StatusMessage, Message
from users.models import User


class BaseModelTestCase(TestCase):

    @classmethod
    def setUpClass(cls):
        super(BaseModelTestCase, cls).setUpClass()
        cls.cat = CategoryMessage(name='Авторизация')
        cls.cat.save()
        cls.stat = StatusMessage(name='Решённые')
        cls.stat.save()

        # c = Client()
        # c.post('http://127.0.0.1:8000/app2/auth/users/',
        #                   {'email': 'testik@gmail.ru', 'username': 'Testik', 'password': 'poiuytrewq123'})
        # otvet = c.login(email='testik@gmail.ru', username='Testik', password = 'poiuytrewq123')
        #
        # print(otvet)

        cls.userr = User(email='testik@gmail.ru', username='Testik', password='poiuytrewq123')
        cls.userr.save()

        cls.first_mes = Message(user=cls.userr, addressee=cls.userr, title="Заголовок", content="Какой-то текст",
                                cat=cls.cat, status=cls.stat)
        cls.first_mes.save()

    def test_model(self):
        rez = self.first_mes
        print(rez.status)
        self.assertEqual(rez.title, "Заголовок")

    def test_model_length(self):
        mes = Message.objects.get(id=1)
        max_length = mes._meta.get_field('title').max_length
        self.assertEqual(max_length, 255)

    def test_first_message_user(self):
        mes = Message.objects.get(id=1)
        field_user = mes._meta.get_field('user').verbose_name
        self.assertEqual(field_user, 'User')

    def test_absolute_url(self):
        self.assertEqual(self.first_mes.get_absolute_url(), reverse('message-detail', kwargs={'pk': 1}))
