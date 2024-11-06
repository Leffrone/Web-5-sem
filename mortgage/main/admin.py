from django.contrib import admin
from .models import mortgage_list, calculation, calculation_content

# Register your models here.

admin.site.register(mortgage_list)
admin.site.register(calculation)
admin.site.register(calculation_content)
