from django.urls import resolve, reverse

from projects import views
from utils.test_bases import ProjectsTestBase


class ProjectsHomeTest(ProjectsTestBase):
    def test_home_view_function(self):
        view = resolve(reverse('projects:home'))

        self.assertIs(view.func, views.home)

    def test_home_contact_form_succesfully(self):
        contact_form_data = {
            'name': 'Testname',
            'subject': 'Subject test',
            'email': 'test@email.com',
            'message': 'Test message',
        }

        response = self.base_test_function(
            'projects:home', method='post', data=contact_form_data
        )
        msg = 'Sua mensagem foi enviada com sucesso!'

        self.assertIn(msg, response.content.decode('utf-8'))

    def test_home_showing_corrects_materials(self):
        self.add_material()
        response = self.base_test_function('projects:home')
        material = 'Material name'

        self.assertIn(material, response.content.decode('utf-8'))

    def test_home_with_no_materials_added(self):
        response = self.base_test_function('projects:home')
        msg = 'Nenhum material na loja.'

        self.assertIn(msg, response.content.decode('utf-8'))
