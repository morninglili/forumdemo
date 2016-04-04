from django.contrib import admin

# Register your models here.
from models import Demolis


class DemoliliAdmin(admin.ModelAdmin):
    list_display = ["example4char", "example4int", "sex", "owner", "last_update_timestamp", 'create_timestamp']
    list_filter = ("sex",)


admin.site.register(Demolis, DemoliliAdmin)
