from django.contrib import admin

# Register your models here.
from models import Demolis
from models import Tribe


class DemoliliAdmin(admin.ModelAdmin):
    list_display = ["example4char", "example4int", "sex", "owner", "last_update_timestamp", 'create_timestamp']
    list_filter = ("sex",)


class Demo4tribeAdmin(admin.ModelAdmin):
    list_display = ["name", "descrip", 'manager']

admin.site.register(Demolis, DemoliliAdmin)
admin.site.register(Tribe, Demo4tribeAdmin)
