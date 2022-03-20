from operator import mod
import uuid
from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True) #blank allows the form to be empty
    demo_link = models.CharField(max_length=2000, null=True, blank=True) #blank allows the form to be empty
    source_link = models.CharField(max_length=2000, null=True, blank=True) #blank allows the form to be empty
    tags = models.ManyToManyField('Tag', blank=True)
    vote_total = models.IntegerField(default=0, null=True, blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    public_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False) #editable - means no one can edit this.

    def __str__(self) -> str:
        return self.title


class Review(models.Model):

    VOTE_TYPE = (
        ('up', 'Up Vote'),
        ('down', 'Down Vote')
    )

    # owner =
    project = models.ForeignKey(Project, on_delete=models.CASCADE) # models.CASCADE will delete all the review 
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=200, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)

    public_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False) #editable - means no one can edit this.

    def __str__(self) -> str:
        return self.value


class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    public_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False) #editable - means no one can edit this.

    def __str__(self) -> str:
        return self.name