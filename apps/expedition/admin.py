from django.contrib import admin
from .models import Expedition

class ExpeditionAdmin(admin.ModelAdmin):
    list_display = ('name', 'leader', 'description', 'date_published', )
    search_fields = ['name', 'description']


# Register your models here.
admin.site.register(Expedition, ExpeditionAdmin)