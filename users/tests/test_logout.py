from django.urls import reverse, resolve

from utils.test_bases import ProjectsTestBase
from users import views


class LogoutTest(ProjectsTestBase):
    def register_and_login(self):
        """
        create an user and make login using it
        """
        self.make_author()
        self.client.login(
            username='username',
            password='123456'
        )

    def base_test_function(self, message, method='post', username='username'):
        """
        base function for logout_view tests.
        """
        self.register_and_login()
        url = reverse('users:logout_view')
        if method == 'post':
            response = self.client.post(
                url, data={'username': username}, follow=True
            )
        elif method == 'get':
            response = self.client.get(
                url, data={'username': username}, follow=True
            )
        msg = message

        self.assertIn(msg, response.content.decode('utf-8'))

    def test_logout_view_function(self):
        view = resolve(reverse('users:logout_view'))

        self.assertIs(view.func, views.logout_view)

    def test_succesful_logout(self):
        self.base_test_function(
            message='Você foi deslogado com sucesso!'
        )

    def test_logout_receive_get_method(self):
        self.base_test_function(
            message='Não foi possível fazer o logout!',
            method='get'
        )

    def test_invalid_user_logotu(self):
        self.base_test_function(
            message='Usuário inválido!',
            username='error_username',
        )
