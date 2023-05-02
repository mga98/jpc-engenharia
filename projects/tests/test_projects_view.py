from django.urls import resolve, reverse

from utils.test_bases import ProjectsTestBase
from projects import views


class ProjectsViewTest(ProjectsTestBase):
    def test_project_view_function(self):
        view = resolve(reverse('projects:projects_all'))

        self.assertIs(view.func, views.projects_view)

    def test_project_view_showing_correct_projects(self):
        self.make_project()

        url = reverse('projects:projects_all')
        response = self.client.get(url)
        project = 'Project title'

        self.assertIn(project, response.content.decode('utf-8'))
