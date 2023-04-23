from projects.forms import ProjectForm, PicturesForm
from projects.models import Messages


def projects_add(request):
    return {'form': ProjectForm(), 'form2': PicturesForm()}


def messages_notification(request):
    messages = Messages.objects.filter(
        read=False,
    ).order_by('-id')

    return {'messages_count': messages.count(), 'contact_messages': messages}
