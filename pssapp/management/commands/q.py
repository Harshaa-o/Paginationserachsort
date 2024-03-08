from django.core.management.base import BaseCommand
from pssapp.models import Subject, Chapter, Topic, Subtopic

class Command(BaseCommand):
    help = 'Populate the database with initial data'

    def handle(self, *args, **kwargs):
        
        physics = Subject.objects.create(name="Physics")

        
        mechanics = Chapter.objects.create(subject=physics, name="Mechanics")
        thermodynamics = Chapter.objects.create(subject=physics, name="Thermodynamics")
        electromagnetism = Chapter.objects.create(subject=physics, name="Electromagnetism")

        
        newton_laws = Topic.objects.create(chapter=mechanics, name="Newton's Laws")
        energy_conservation = Topic.objects.create(chapter=thermodynamics, name="Energy Conservation")
        electromagnetic_fields = Topic.objects.create(chapter=electromagnetism, name="Electromagnetic Fields")

        
        Subtopic.objects.create(topic=newton_laws, name="Newton's First Law")
        Subtopic.objects.create(topic=newton_laws, name="Newton's Second Law")
        Subtopic.objects.create(topic=newton_laws, name="Newton's Third Law")

        Subtopic.objects.create(topic=energy_conservation, name="Potential Energy")
        Subtopic.objects.create(topic=energy_conservation, name="Kinetic Energy")
        Subtopic.objects.create(topic=energy_conservation, name="Conservation of Energy")

        Subtopic.objects.create(topic=electromagnetic_fields, name="Magnetic Field")
        Subtopic.objects.create(topic=electromagnetic_fields, name="Electric Field")
        Subtopic.objects.create(topic=electromagnetic_fields, name="Electromagnetic Waves")

        
        french = Subject.objects.create(name="French")

        grammar = Chapter.objects.create(subject=french, name="Grammar")
        vocabulary = Chapter.objects.create(subject=french, name="Vocabulary")
        literature = Chapter.objects.create(subject=french, name="Literature")

        
        verbs = Topic.objects.create(chapter=grammar, name="Verbs")
        food = Topic.objects.create(chapter=vocabulary, name="Food")
        novels = Topic.objects.create(chapter=literature, name="Novels")

        
        Subtopic.objects.create(topic=verbs, name="Regular Verbs")
        Subtopic.objects.create(topic=verbs, name="Irregular Verbs")
        Subtopic.objects.create(topic=verbs, name="Reflexive Verbs")

        Subtopic.objects.create(topic=food, name="Fruits")
        Subtopic.objects.create(topic=food, name="Vegetables")
        Subtopic.objects.create(topic=food, name="Drinks")

        Subtopic.objects.create(topic=novels, name="Classic Novels")
        Subtopic.objects.create(topic=novels, name="Contemporary Novels")
        Subtopic.objects.create(topic=novels, name="Fantasy Novels")

        
        mathematics = Subject.objects.create(name="Mathematics")

        
        algebra = Chapter.objects.create(subject=mathematics, name="Algebra")
        geometry = Chapter.objects.create(subject=mathematics, name="Geometry")
        calculus = Chapter.objects.create(subject=mathematics, name="Calculus")

        
        equations = Topic.objects.create(chapter=algebra, name="Equations")
        shapes = Topic.objects.create(chapter=geometry, name="Shapes")
        derivatives = Topic.objects.create(chapter=calculus, name="Derivatives")

        
        Subtopic.objects.create(topic=equations, name="Linear Equations")
        Subtopic.objects.create(topic=equations, name="Quadratic Equations")
        Subtopic.objects.create(topic=equations, name="Cubic Equations")

        Subtopic.objects.create(topic=shapes, name="Triangles")
        Subtopic.objects.create(topic=shapes, name="Circles")
        Subtopic.objects.create(topic=shapes, name="Polygons")

        Subtopic.objects.create(topic=derivatives, name="First Derivative")
        Subtopic.objects.create(topic=derivatives, name="Second Derivative")
        Subtopic.objects.create(topic=derivatives, name="Partial Derivatives")

        English = Subject.objects.create(name="English")
        Japanese = Subject.objects.create(name="Japanese")
        German = Subject.objects.create(name="German")
        Chemistry = Subject.objects.create(name="Chemistry")
        Commerce = Subject.objects.create(name="Commerce")

        self.stdout.write(self.style.SUCCESS('Data inserted successfully'))
