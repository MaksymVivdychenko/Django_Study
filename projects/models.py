from django.db import models
import uuid

# Create your models here.
class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    demo_link = models.URLField(max_length=2000, null=True, blank=True)
    tags = models.ManyToManyField('Tag', blank=True)
    vote_total = models.IntegerField(default=0, null=True, blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)
    source_link = models.URLField(max_length=2000, null=True, blank=True)
    date_created = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.title
    
class Review(models.Model):
    VOTE_TYPE = (
        ('up', 'Up vote'),
        ('down', 'Down vote'),
    )
    #owner
    project = models.ForeignKey(Project, on_delete= models.CASCADE)
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=200, choices=VOTE_TYPE)
    date_created = models.DateField(auto_now_add=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    def __str__(self):
        return f'{self.project.title} --- {self.value}'
    
class Tag(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=200)
    date_created = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.name