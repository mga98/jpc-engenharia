from django.test import TestCase

from projects.models import Project, User, Messages


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
        read='False',
    ):
        return Messages.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message,
            read=read
        )

    def register_and_login(self, username='username', password='123456'):
        self.make_author()
        self.client.login(
            username=username,
            password=password,
        )


class ProjectsTestBase(TestCase, ProjectMixin):
    def setUp(self) -> None:
        return super().setUp()
