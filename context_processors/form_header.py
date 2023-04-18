from projects.forms import ProjectForm


def projects_add(request):
    return {'form': ProjectForm()}
