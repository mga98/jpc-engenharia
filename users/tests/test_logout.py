from django.urls import reverse, resolve

from utils.test_bases import ProjectsTestBase
from users import views


class LogoutTest(ProjectsTestBase):
    def register_and_login(self):
        self.make_author()
        self.client.login(
            username='username',
            password='123456'
        )

    def test_logout_view_function(self):
        view = resolve(reverse('users:logout_view'))

        self.assertIs(view.func, views.logout_view)

    def test_succesful_logout(self):
        self.register_and_login()
        url = reverse('users:logout_view')
        response = self.client.post(
            url, data={'username': 'username'}, follow=True
        )
        msg = 'Você foi deslogado com sucesso!'

        self.assertIn(msg, response.content.decode('utf-8'))

    def test_logout_receive_get_method(self):
        self.register_and_login()
        url = reverse('users:logout_view')
        response = self.client.get(url, follow=True)
        msg = 'Não foi possível fazer o logout!'

        self.assertIn(msg, response.content.decode('utf-8'))

    def test_invalid_user_logotu(self):
        self.register_and_login()
        url = reverse('users:logout_view')
        response = self.client.post(
            url, data={'username': 'error_username'}, follow=True
        )
        msg = 'Usuário inválido!'

        self.assertIn(msg, response.content.decode('utf-8'))
