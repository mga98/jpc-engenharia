from django.test import TestCase
from django.urls import reverse

from projects.models import Project, User, Messages
from users.models import Materials


class ProjectMixin:
    def make_author(
        self,
        first_name='user',
        last_name='name',
        username='username',
        password='123456',
        email='username@email.com',
    ):

        return User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=password,
            email=email,
        )

    def make_project(
        self,
        title='Project title',
        slug='project-title',
        status=True,
        author_data=None,
    ):

        if author_data is None:
            author_data = {}

        return Project.objects.create(
            author=self.make_author(**author_data),
            title=title,
            slug=slug,
            status=status,
        )

    def send_message(
        self,
        name='Message author',
        email='message@email.com',
        subject='Message subject',
        message='Message test',
    ):
        return Messages.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message,
        )

    def add_material(
        self,
        material='Material name',
        short_description='Material description',
        stocked=True,
    ):
        return Materials.objects.create(
            material=material,
            short_description=short_description,
            stocked=stocked,
        )

    def register_and_login(self, username='username', password='123456'):
        self.make_author()
        self.client.login(
            username=username,
            password=password,
        )

    def make_project_and_login(self):
        self.make_project()
        self.client.login(
            username='username',
            password='123456'
        )

    def base_test_function(
        self, url, url_kwargs=False, pk=1, method='get', data=None, follow=True
    ):
        if url_kwargs:
            reversed_url = reverse(url, kwargs={'pk': pk})

        else:
            reversed_url = reverse(url)

        if method == 'get':
            response = self.client.get(
                reversed_url, data=data, follow=follow
            )
        elif method == 'post':
            response = self.client.post(
                reversed_url, data=data, follow=follow
            )

        return response


class ProjectsTestBase(TestCase, ProjectMixin):
    def setUp(self, *args, **kwargs):
        self.form_data = {
            'title': 'Project title',
            'status-select': 'Pronto',
            'thumbnail': '/thumb.png',
            'image': '/picture.png'
        }

        self.material_form_data = {
            'material': 'Material name',
            'short_description': 'Material description',
            'stocked': True,
        }

        self.register_form_data = {
            'first_name': 'User',
            'last_name': 'Test',
            'username': 'usertest',
            'password': '123456',
            'password_2': '123456',
            'email': 'test@email.com',
        }

        return super().setUp(*args, **kwargs)
