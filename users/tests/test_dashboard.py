from django.urls import resolve, reverse
from parameterized import parameterized

from users import views
from utils.test_bases import ProjectsTestBase


class DashboardTest(ProjectsTestBase):
    def test_dashboard_view_function(self):
        view = resolve(reverse('users:dashboard'))

        self.assertIs(view.func, views.dashboard)

    def test_dashboard_loads_correct_projects(self):
        self.make_project()
        self.client.login(
            username='username',
            password='123456',
        )
        response = self.base_test_function('users:dashboard')
        project = 'Project title'

        self.assertIn(project, response.content.decode('utf-8'))

    def test_dashboard_loads_correct_messages(self):
        self.send_message()
        self.register_and_login()

        response = self.base_test_function('users:dashboard')
        message = 'Message subject'

        self.assertIn(message, response.content.decode('utf-8'))

    def test_dashboard_register_succesful(self):
        self.register_and_login()
        response = self.base_test_function(
            'users:register_create',
            method='post',
            data=self.register_form_data,
        )
        msg = 'Usuário cadastrado com sucesso!'

        self.assertIn(msg, response.content.decode('utf-8'))

    def test_dashboard_register_receive_get_method(self):
        self.register_and_login()
        response = self.base_test_function('users:register_create')

        self.assertEqual(response.status_code, 404)

    @parameterized.expand([
        ('username', 'É necessário um nome de usuário!'),
        ('first_name', 'Você precisa preencher o campo de primeiro nome!'),
        ('last_name', 'Você precisa preencher o campo de último nome!'),
        ('email', 'Você precisa preencher o campo de E-mail!'),
        ('password', 'Você precisa preencher o campo de senha!'),
        ('password_2', 'Você precisa confirmar a senha!'),
    ])
    def test_dashboard_register_empty_fields(self, field, error):
        self.register_and_login()
        self.register_form_data[field] = ''

        response = self.base_test_function(
            'users:register_create',
            method='post',
            data=self.register_form_data,
        )

        self.assertIn(error, response.content.decode('utf-8'))

    def test_passwords_match(self):
        self.register_and_login()
        self.register_form_data['password'] = 'error_password'

        response = self.base_test_function(
            'users:register_create',
            method='post',
            data=self.register_form_data,
        )
        error = 'Verifique se as senhas são iguais'

        self.assertIn(error, response.content.decode('utf-8'))

    def test_new_user_can_login(self):
        self.register_and_login()
        response = self.base_test_function(
            'users:register_create',
            method='post',
            data=self.register_form_data,
        )
        self.client.logout()
        self.client.login(
            username='usertest',
            password='123456',
        )

        dashboard_url = reverse('users:dashboard')
        response = self.client.get(dashboard_url)
        msg = 'Bem vindo(a), User!'

        self.assertIn(msg, response.content.decode('utf-8'))
