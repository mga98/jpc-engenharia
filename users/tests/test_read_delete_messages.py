from django.urls import resolve, reverse

from projects.models import Messages
from users import views
from utils.test_bases import ProjectsTestBase


class ReadDeleteMessageTest(ProjectsTestBase):
    def test_read_delete_views_functions(self):
        read_view = resolve(reverse('users:read_message'))
        delete_view = resolve(reverse('users:delete_message'))

        self.assertIs(read_view.func, views.read_message)
        self.assertIs(delete_view.func, views.delete_message)

    def test_read_delete_views_receive_get_method(self):
        self.register_and_login()

        # READ MESSAGE
        response_read = self.base_test_function('users:read_message')

        # DELETE MESSAGE
        response_delete = self.base_test_function('users:delete_message')
        error = 'Mensagem não pode ser deletada!'

        self.assertEqual(response_read.status_code, 404)
        self.assertIn(error, response_delete.content.decode('utf-8'))

    def test_read_message_succesful(self):
        self.register_and_login()
        self.send_message()
        self.base_test_function(
            'users:read_message', method='post', data={'message_id': 1}
        )
        message = Messages.objects.get(id=1)

        self.assertEqual(message.read, True)

    def test_delete_message_succesful(self):
        self.register_and_login()
        self.send_message()
        response = self.base_test_function(
            'users:delete_message',
            method='post',
            data={'delete_msg_id': 1}
        )
        msg = 'Mensagem deletada com sucesso!'

        self.assertIn(msg, response.content.decode('utf-8'))

    def test_delete_message_not_found(self):
        self.register_and_login()
        response = self.base_test_function(
            'users:delete_message',
            method='post',
            data={'delete_msg_id': 1},
        )

        self.assertEqual(response.status_code, 404)
