from django.contrib import admin
from .models import project
# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
  list_display = ("projectname", "from_date", "end_date","image")

admin.site.register(project,ProjectAdmin)