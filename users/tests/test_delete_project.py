from django.urls import reverse, resolve

from utils.test_bases import ProjectsTestBase
from users import views


class DeleteProjectTest(ProjectsTestBase):
    def test_delete_project_view_function(self):
        view = resolve(reverse('users:delete_project'))

        self.assertIs(view.func, views.delete_project)

    def test_delete_project_succesful(self):
        self.make_project_and_login()
        response = self.base_test_function(
            'users:delete_project', method='post', data={'project_id': 1}
        )
        msg = 'Projeto "Project title" deletado com sucesso!'

        self.assertIn(msg, response.content.decode('utf-8'))

    def test_delete_project_receive_get_method(self):
        self.make_project_and_login()
        response = self.base_test_function('users:delete_project')

        self.assertEqual(response.status_code, 404)

    def test_project_doesnt_exist(self):
        self.register_and_login()
        response = self.base_test_function(
            'users:delete_project', method='post', data={'project_id': 1}
        )

        self.assertEqual(response.status_code, 404)
