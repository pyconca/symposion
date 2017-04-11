from django.http import Http404
from django.shortcuts import render

from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

User = get_user_model()


@login_required
def user_list(request):

    if not request.user.is_staff:
        raise Http404()

    return render(request, "symposion/conference/user_list.html", {
        "users": User.objects.all(),
    })
