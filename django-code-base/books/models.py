from django.db import models

# Create your models here.
from django.utils import timezone
import uuid

class Book(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    date_added = models.DateTimeField(default=timezone.now)
    bookName = models.CharField("Book Name", max_length=50, null=False, blank=False)
    author = models.CharField("Author", max_length=50, null=False, blank=False)
    genre = models.CharField("Genre", max_length=20, null=False, blank=False)
    location = models.FileField("Location", null=False, blank=False, upload_to = "BookPDF/")
    titlePgImg = models.ImageField("Title Page Image", null=False, blank=False, upload_to = "BookStore/")