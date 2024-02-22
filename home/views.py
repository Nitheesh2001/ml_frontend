from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Details, Cadidate
from .forms import CandidateForm  # Import CandidateForm

def index(request):
    context = {
        "variable1": "this is send",
        "variable2": "new one"
    }
    return render(request, 'index.html', context)

def details(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        new_details = Details(name=name, email=email, subject=subject)
        new_details.save()
        messages.success(request, "Your Message Has Been Sent!")
    return render(request, 'details.html')



def cadidate(request):
    details = Details.objects.last()  # Get the latest Details object
    if request.method == "POST":
        form = CandidateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Candidate details have been saved successfully!")
            return redirect('home')
        else:
            # Display form errors if validation fails
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"Error in {field}: {error}")
    else:
        form = CandidateForm()  # Initialize empty form
    context = {'form': form, 'subject': details.subject if details else None}
    return render(request, 'cadidate.html', context)

def cadidate_details(request):
    cadidates = Cadidate.objects.all()
    return render(request, 'cadidate_details.html', {'cadidates': cadidates})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')
