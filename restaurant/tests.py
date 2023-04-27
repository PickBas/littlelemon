from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse

from restaurant.models import Menu
from restaurant.serializers import MenuItemSerializer


class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(item.__str__(), "IceCream : 80")


class MenuViewTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.user = User.objects.create_user(
            username='asdf',
        )
        self.user.set_password('asdf123!')
        self.user.save()
        self.burrito = Menu.objects.create(title='burrito', price=12, inventory=10)

    def test_view_authentication(self) -> None:
        response = self.client.get(reverse('menu'))
        self.assertEqual(response.status_code, 401)
        self.client.force_login(user=self.user)
        response = self.client.get(reverse('menu'))
        self.assertEqual(response.status_code, 200)

    def test_getall(self):
        self.client.force_login(user=self.user)
        response = self.client.get(reverse('menu'))
        self.assertEqual(response.status_code, 200)
        menu = Menu.objects.all()
        serializer = MenuItemSerializer(menu, many=True)
        self.assertEqual(response.data, serializer.data)