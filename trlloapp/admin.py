from django.contrib import admin

# Register your models here.
from trlloapp.models import Team,Team_Type,Board

admin.site.register(Team)
admin.site.register(Team_Type)
admin.site.register(Board)