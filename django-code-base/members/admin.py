from django.contrib import admin
from .models import Member
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class MemberResource(resources.ModelResource):

    class Meta:
        model = Member

class MemberAdmin(ImportExportModelAdmin):

    resource_class = MemberResource

admin.site.register(Member, MemberAdmin)