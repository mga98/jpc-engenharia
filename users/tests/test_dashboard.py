from django.urls import reverse, resolve
from parameterized import parameterized

from utils.test_bases import ProjectsTestBase
from users import views


class DashboardTest(ProjectsTestBase):
    def setUp(self, *args, **kwargs):
        self.form_data = {
            'first_name': 'User',
            'last_name': 'Test',
            'username': 'usertest',
            'password': '123456',
            'password_2': '123456',
            'email': 'test@email.com',
        }

        return super().setUp(*args, **kwargs)

    def register_and_login(self, username='username', password='123456'):
        self.make_author()
        self.client.login(
            username=username,
            password=password,
        )

    def test_dashboard_view_function(self):
        view = resolve(reverse('users:dashboard'))

        self.assertIs(view.func, views.dashboard)

    def test_dashboard_loads_correct_projects(self):
        self.make_project()
        self.client.login(
            username='username',
            password='123456',
        )

        url = reverse('users:dashboard')
        response = self.client.get(url, follow=True)
        project = 'Project title'

        self.assertIn(project, response.content.decode('utf-8'))

    def test_dashboard_register_succesful(self):
        self.register_and_login()

        url = reverse('users:register_create')
        response = self.client.post(
            url, data=self.form_data, follow=True
        )
        msg = 'Usuário cadastrado com sucesso!'

        self.assertIn(msg, response.content.decode('utf-8'))

    def test_dashboard_register_receive_get_method(self):
        self.register_and_login()

        url = reverse('users:register_create')
        response = self.client.get(url, follow=True)

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
        self.form_data[field] = ''

        url = reverse('users:register_create')
        response = self.client.post(
            url, data=self.form_data, follow=True,
        )

        self.assertIn(error, response.content.decode('utf-8'))

    def test_passwords_match(self):
        self.register_and_login()

        self.form_data['password'] = 'error_password'

        url = reverse('users:register_create')
        response = self.client.post(
            url, data=self.form_data, follow=True
        )
        error = 'Verifique se as senhas são iguais'

        self.assertIn(error, response.content.decode('utf-8'))

    def test_new_user_can_login(self):
        self.register_and_login()

        register_url = reverse('users:register_create')
        self.client.post(
            register_url, data=self.form_data, follow=True
        )

        self.client.logout()

        self.client.login(
            username='usertest',
            password='123456',
        )

        dashboard_url = reverse('users:dashboard')
        response = self.client.get(dashboard_url)
        msg = 'Bem vindo(a), usertest!'

        self.assertIn(msg, response.content.decode('utf-8'))
