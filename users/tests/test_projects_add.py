from django.urls import resolve, reverse

from projects.models import Pictures, Project
from users import views
from utils.test_bases import ProjectsTestBase


class ProjectsAddTest(ProjectsTestBase):
    def test_projects_view_function(self):
        view = resolve(reverse('users:projects_add'))

        self.assertIs(view.func, views.projects_add)

    def test_projects_add_succesful(self):
        self.register_and_login()
        response = self.base_test_function(
            'users:projects_add',
            method='post',
            data=self.form_data,
        )
        msg = 'Post criado com sucesso!'

        self.assertIn(msg, response.content.decode('utf-8'))
        self.assertEqual(Pictures.objects.count(), 1)
        self.assertEqual(Project.objects.count(), 1)

    def test_projects_add_receive_get_method(self):
        self.register_and_login()
        response = self.base_test_function('users:projects_add')

        self.assertEqual(response.status_code, 404)
