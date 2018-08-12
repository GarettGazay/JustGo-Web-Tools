from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import FormBasic, Reocurring
# Register your models here.
@admin.register(Reocurring)
@admin.register(FormBasic)

class ViewAdmin(ImportExportModelAdmin):
    pass
# admin.site.register(FormBasic)
