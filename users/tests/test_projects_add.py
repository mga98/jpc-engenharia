from django.urls import resolve, reverse

from users import views
from projects.models import Pictures, Project
from utils.test_bases import ProjectsTestBase


class ProjectsAddTest(ProjectsTestBase):
    def setUp(self, *args, **kwargs):
        self.form_data = {
            'title': 'Project title',
            'status-select': 'Pronto',
            'thumbnail': '/thumb.png',
            'image': '/picture.png'
        }

        return super().setUp(*args, **kwargs)

    def test_projects_view_function(self):
        view = resolve(reverse('users:projects_add'))

        self.assertIs(view.func, views.projects_add)

    def test_projects_add_succesful(self):
        self.register_and_login()
        url = reverse('users:projects_add')
        response = self.client.post(
            url, data=self.form_data, follow=True
        )
        msg = 'Post criado com sucesso!'

        self.assertIn(msg, response.content.decode('utf-8'))
        self.assertEqual(Pictures.objects.count(), 1)
        self.assertEqual(Project.objects.count(), 1)

    def test_projects_add_receive_get_method(self):
        self.register_and_login()
        url = reverse('users:projects_add')
        response = self.client.get(url, follow=True)

        self.assertEqual(response.status_code, 404)
