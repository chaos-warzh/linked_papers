from django.contrib import admin
from .models import Paper
from .models import Citation

# Register your models here.
admin.site.register(Paper)
admin.site.register(Citation)