from .models import Reference
from .forms import get_form


def get_references_for_receiver(request, receiver, return_url=None, form=True):
    references = Reference.objects.filter(receiver=receiver)
    if not form:
        return references, None

    return references, get_form(request, receiver, return_url)
