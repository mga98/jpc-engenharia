from django.urls import reverse, resolve

from utils.test_bases import ProjectsTestBase
from users import views


class EditProjectTest(ProjectsTestBase):
    def test_edit_project_view_function(self):
        view = resolve(reverse('users:edit_project', kwargs={'pk': 1}))

        self.assertIs(view.func, views.edit_project)

    def test_edit_project_succesful(self):
        self.make_project_and_login()
        response = self.base_test_function(
            'users:edit_project',
            url_kwargs=True,
            method='post',
            data=self.form_data
        )
        msg = 'Projeto editado com sucesso!'

        self.assertIn(msg, response.content.decode('utf-8'))

    def test_project_not_found(self):
        self.register_and_login()
        response = self.base_test_function(
            'users:edit_project',
            url_kwargs=True,
            method='post'
        )

        self.assertEqual(response.status_code, 404)
