from projects.forms import ProjectForm, PicturesForm


def projects_add(request):
    return {'form': ProjectForm(), 'form2': PicturesForm()}
