from django.urls import resolve, reverse

from projects import views
from projects.models import Pictures
from utils.test_bases import ProjectsTestBase


class ProjectDetailTest(ProjectsTestBase):
    def test_project_detail_view_function(self):
        view = resolve(
            reverse('projects:project_detail', kwargs={'pk': 1})
        )

        self.assertIs(view.func, views.project_detail)

    def test_project_detail_view_showing_correct_project(self):
        self.make_project()

        url = reverse('projects:project_detail', kwargs={'pk': 1})
        response = self.client.get(url)
        project = 'Project title'

        self.assertIn(project, response.content.decode('utf-8'))

    def test_project_detail_view_showing_correct_pictures(self):
        project = self.make_project()
        img_url = 'image/url/test.png'
        Pictures.objects.create(
            project=project,
            image=img_url
        )
        img = 'image/url/test.png'

        url = reverse('projects:project_detail', kwargs={'pk': 1})
        response = self.client.get(url)

        self.assertIn(img, response.content.decode('utf-8'))
