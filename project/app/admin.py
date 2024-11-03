from django.contrib import admin
from app.models import *

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(RecruiterProfile)
admin.site.register(SeekerProfile)