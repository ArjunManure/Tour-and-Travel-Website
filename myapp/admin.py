from django.contrib import admin
from myapp.models import contact_view
from myapp.models import register_view
# Register your models here.

admin.site.register(contact_view)

admin.site.register(register_view)