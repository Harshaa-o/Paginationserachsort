from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    

class Chapter(models.Model):
    subject = models.ForeignKey(Subject, related_name='chapters', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Topic(models.Model):
    chapter = models.ForeignKey(Chapter, related_name='topics', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Subtopic(models.Model):
    topic = models.ForeignKey(Topic, related_name='subtopics', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Meta:
    ordering = ['id']