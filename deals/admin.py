from django.contrib import admin
from .models import Deal


# Register your models here.
@admin.register(Deal)
class DealAdmin(admin.ModelAdmin):
    pass
