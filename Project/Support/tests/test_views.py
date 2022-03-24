from django.test import TestCase
from django.urls import reverse

from Support.models import CategoryMessage, StatusMessage, Message
from users.models import User


class MessageListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.cat = CategoryMessage(name='Авторизация')
        cls.cat.save()
        cls.stat = StatusMessage(name='Решённые')
        cls.stat.save()

        cls.userr = User(email='testik@gmail.ru', username='Testik', password='poiuytrewq123')
        cls.userr.save()

        number_of_message = 10
        for mes_num in range(number_of_message):
            Message.objects.create(user=cls.userr, addressee=cls.userr,
                                   title=f"Заголовок{mes_num}",
                                   content=f"Какой-то текст{mes_num}",
                                   cat=cls.cat, status=cls.stat)

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get(reverse('message-list'))
        self.assertEqual(resp.status_code, 200)
