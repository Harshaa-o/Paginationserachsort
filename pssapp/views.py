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

    # Construct the base SQL query
    base_query = """
        SELECT id, name FROM pssapp_subject
    """

    # Add WHERE clause if search query is provided
    params = []
    if query:
        base_query += """
            WHERE LOWER(name) LIKE %s
        """
        params.append('%' + query.lower() + '%')

    # Add ORDER BY clause for sorting
    if sort_option == 'asc':
        base_query += """
            ORDER BY name ASC
        """
    elif sort_option == 'desc':
        base_query += """
            ORDER BY name DESC
        """

    # Calculate pagination limit and offset
    limit = 10
    offset = (page_number - 1) * limit
    base_query += " LIMIT %s OFFSET %s;"
    params.extend([limit, offset])

    with connection.cursor() as cursor:
        cursor.execute(base_query, params)
        results = cursor.fetchall()

        # Convert query results into a list of dictionaries
        subjects = [{'id': row[0], 'name': row[1]} for row in results]

        # Get total subjects count from database (without limit and offset)
        total_subjects_count_query = "SELECT COUNT(*) FROM pssapp_subject"
        cursor.execute(total_subjects_count_query)
        total_subjects_count = cursor.fetchone()[0]

    # Calculate total pages
    total_pages = (total_subjects_count + limit - 1) // limit

    # Generate page range
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
    cursor = connection.cursor()
    sql = """
        SELECT name 
        FROM pssapp_subject
        WHERE name ILIKE %s
        LIMIT 10
    """
    params = ['%' + query + '%']
    cursor.execute(sql, params)
    subjects = cursor.fetchall()
    data = [{'name': subject[0]} for subject in subjects]
    return JsonResponse(data, safe=False)