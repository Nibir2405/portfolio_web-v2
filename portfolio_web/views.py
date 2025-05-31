from django.shortcuts import render
from django.contrib import messages
from .forms import ContactForm
from .models import Contact

def home(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            phone = form.cleaned_data["phone"]
            content = form.cleaned_data["content"]
            Contact.objects.create(name=name, email=email, phone=phone, content=content)

            messages.success(request, "You message has been send./n" \
            "Admin will contact you soon")

    return render(request, 'home.html')