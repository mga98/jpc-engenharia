from projects.forms import ProjectForm, PicturesForm
from projects.models import Messages


def projects_add(request):
    return {'form': ProjectForm(), 'form2': PicturesForm()}


def messages_notification(request):
    messages = Messages.objects.filter(
        read=False,
    )

    messages_count = messages.count()

    return {'messages_count': messages_count}
