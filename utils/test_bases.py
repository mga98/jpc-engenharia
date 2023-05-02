from django.test import TestCase

from projects.models import Project, User


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


class ProjectsTestBase(TestCase, ProjectMixin):
    def setUp(self) -> None:
        return super().setUp()
