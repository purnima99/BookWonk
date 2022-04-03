from django.contrib import admin
from .models import Book
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class BookResource(resources.ModelResource):
    
    class Meta:
        model = Book

class BookAdmin(ImportExportModelAdmin):

    resource_class = BookResource

admin.site.register(Book, BookAdmin)