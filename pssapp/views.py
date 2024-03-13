from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.db import connection
from django.http import JsonResponse
import json;
from . import models
from pssapp.models import Subject;
from django.views.generic import ListView
from django.db.models import Q





def subject_list(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        if name:
            subject = Subject.objects.create(name=name)
            return JsonResponse({'success': True, 'id': subject.id})
        else:
            return JsonResponse({'success': False})
    
    query = request.GET.get('q', '')
    sort_option = request.GET.get('sort', 'default')
    page_number = int(request.GET.get('page', 1))

    # Base SQL query
    base_query = "SELECT id, name FROM pssapp_subject"
    params = []

    # Apply search filter
    if query:
        base_query += " WHERE LOWER(name) LIKE %s"
        params.append('%' + query.lower() + '%')

    # Apply sorting
    if sort_option == 'asc':
        base_query += " ORDER BY name ASC"
    elif sort_option == 'desc':
        base_query += " ORDER BY name DESC"

    # Calculate pagination parameters
    limit = 10
    offset = (page_number - 1) * limit
    base_query += " LIMIT %s OFFSET %s"
    params.extend([limit, offset])

    with connection.cursor() as cursor:
        cursor.execute(base_query, params)
        results = cursor.fetchall()
        subjects = [{'id': row[0], 'name': row[1]} for row in results]

        # Get total subjects count for pagination
        total_subjects_query = "SELECT COUNT(*) FROM pssapp_subject"
        if query:
            total_subjects_query += " WHERE LOWER(name) LIKE %s"
            cursor.execute(total_subjects_query, ['%' + query.lower() + '%'])
        else:
            cursor.execute(total_subjects_query)

        total_subjects_count = cursor.fetchone()[0]

    # Calculate total pages and page range
    total_pages = (total_subjects_count + limit - 1) // limit
    page_range = range(1, total_pages + 1)

    return render(request, 'subject_list.html', {
        'subjects': subjects,
        'total_pages': total_pages,
        'page_range': page_range,
        'current_page': page_number,
        'query': query,
        'sort_option': sort_option
    })

        
