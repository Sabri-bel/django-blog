from django.shortcuts import render
from django.contrib import messages
from .models import About
from .forms import CollaborateForm


def About_me(request):
    """
    Renders the most recent information about the website author and allows
    users to request collaboration
    displays an individual instance of model:'about.about'
    **context**
    ``about``
        the most recent instance of :model:'about.About'
    ``collaborate_form``
        an instance of :form:'about.CollaborateForm'
    **template**
    :template:'about/about.html
    """
    if request.method == "POST":
        collaborate_form = CollaborateForm(data=request.POST)
        if collaborate_form.is_valid():
            collaborate_form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'collaboration request received! I will respond within 2 working days'
            )
    about = About.objects.all().order_by('-updated_on').first()

    collaborate_form = CollaborateForm()

    return render(
        request,
        "about/about.html",
        {
        "about": about,
        "collaborate_form": collaborate_form
        },
    )
