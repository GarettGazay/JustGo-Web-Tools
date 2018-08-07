from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import FormBasic, Reoccuring
# Register your models here.
@admin.register(Reoccuring)
@admin.register(FormBasic)
class ViewAdmin(ImportExportModelAdmin):
    pass
# admin.site.register(FormBasic)
