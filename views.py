from django.shortcuts import render, redirect, get_object_or_404
from .models import Study
from django.http import HttpResponse

# View for the main page that lists all studies
def index(request):
    studies = Study.objects.all()
    return render(request, 'index.html', {'studies': studies})

# View to add a new study
def add_study(request):
    if request.method == 'POST':
        study_name = request.POST['study_name']
        study_description = request.POST['study_description']
        study_phase = request.POST['study_phase']
        sponsor_name = request.POST['sponsor_name']
        
        # Create a new study object and save it to the database
        new_study = Study(
            study_name=study_name,
            study_description=study_description,
            study_phase=study_phase,
            sponsor_name=sponsor_name
        )
        new_study.save()
        return redirect('index')  # Redirect to main page after saving

    return render(request, 'add_study.html')

# View to edit an existing study
def edit_study(request, id):
    study = get_object_or_404(Study, pk=id)
    if request.method == 'POST':
        study.study_name = request.POST['study_name']
        study.study_description = request.POST['study_description']
        study.study_phase = request.POST['study_phase']
        study.sponsor_name = request.POST['sponsor_name']
        study.save()
        return redirect('index')  # Redirect to main page after updating

    return render(request, 'edit_study.html', {'study': study})

# View to display details of a selected study
def view_study(request, id):
    study = get_object_or_404(Study, pk=id)
    return render(request, 'view_study.html', {'study': study})

# View to delete a study
def delete_study(request, id):
    study = get_object_or_404(Study, pk=id)
    study.delete()
    return redirect('index')  # Redirect to main page after deletion
