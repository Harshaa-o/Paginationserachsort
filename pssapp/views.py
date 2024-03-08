from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.db import connection
from django.http import JsonResponse
import json;
from . import models
from pssapp.models import Subject;
from django.views.generic import ListView
from django.db.models import Q


def sublist(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        if name:
            subject = Subject.objects.create(name=name)
            return JsonResponse({'success': True, 'id': subject.id})
    return JsonResponse({'success': False})

def subject_list(request):
    
    query = request.GET.get('q', '')
    sort_option = request.GET.get('sort', 'default')
    page_number = int(request.GET.get('page', 1))

    
    subjects = Subject.objects.all()
    if query:
        subjects = subjects.filter(name__icontains=query)
    
    if sort_option == 'asc':
        subjects = subjects.order_by('name')
    elif sort_option == 'desc':
        subjects = subjects.order_by('-name')
   
    limit = 10  
    offset = (page_number - 1) * limit
    total_subjects_count = subjects.count()
    total_pages = (total_subjects_count + limit - 1) // limit
    subjects = subjects[offset: offset + limit]
    
    page_range = range(1, total_pages + 1)

    return render(request, 'subject_list.html', {
        'subjects': subjects,
        'total_pages': total_pages,
        'page_range': page_range,
        'current_page': page_number,
        'query': query,
        'sort_option': sort_option
    })

def subject_search(request):
    query = request.GET.get('q', '')
    subjects = Subject.objects.filter(name__icontains=query)[:10]
    data = [{'name': subject.name} for subject in subjects]
    return JsonResponse(data, safe=False)

