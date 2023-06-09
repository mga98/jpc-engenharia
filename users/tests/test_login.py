from django.urls import resolve, reverse
from parameterized import parameterized

from users import views
from users.forms import LoginForm
from utils.test_bases import ProjectsTestBase


class LoginTest(ProjectsTestBase):
    def setUp(self, *args, **kwargs):
        self.form_data = {
            'username': 'username',
            'password': '123456',
        }

    def test_login_view_function(self):
        view = resolve(reverse('users:login_view'))

        self.assertIs(view.func, views.login_view)

    def test_login_create_view_function(self):
        view = resolve(reverse('users:login_create'))

        self.assertIs(view.func, views.login_create)

    def test_login_create_receive_get_method(self):
        response = self.base_test_function('users:login_create')

        self.assertEqual(response.status_code, 404)

    @parameterized.expand([
        ('username', 'Usuário'),
        ('password', 'Senha'),
    ])
    def test_login_form_labels(self, field, label):
        form = LoginForm()
        current_label = form[field].field.label

        self.assertEqual(label, current_label)

    @parameterized.expand([
        ('username', 'Nome de usuário'),
        ('password', 'Digite sua senha')
    ])
    def test_login_form_placeholders(self, field, placeholder):
        form = LoginForm()
        current_placeholder = form[field].field.widget.attrs['placeholder']

        self.assertEqual(placeholder, current_placeholder)

    def test_succesful_login(self):
        user = self.make_author()
        response = self.base_test_function(
            'users:login_create', method='post', data=self.form_data
        )
        msg = f'Bem vindo, {user.username}!'

        self.assertIn(msg, response.content.decode('utf-8'))

    def test_incorrect_authentication(self):
        self.make_author(
            username='error_username'
        )
        response = self.base_test_function(
            'users:login_create', method='post', data=self.form_data
        )
        msg = 'Usuário ou senha inválidos!'

        self.assertIn(msg, response.content.decode('utf-8'))

    def test_login_form_not_valid(self):
        self.form_data.update({
            'username': '',
            'password': '',
        })
        response = self.base_test_function(
            'users:login_create', method='post', data=self.form_data
        )
        msg = 'Não foi possível fazer o login!'

        self.assertIn(msg, response.content.decode('utf-8'))
