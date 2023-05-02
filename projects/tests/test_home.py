from django.test import TestCase
from django.urls import reverse, resolve

from projects import views


class ProjectsHomeTest(TestCase):
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

        url = reverse('projects:home')
        response = self.client.post(
            url, data=contact_form_data, follow=True
        )
        msg = 'Sua mensagem foi enviada com sucesso!'

        self.assertIn(msg, response.content.decode('utf-8'))
