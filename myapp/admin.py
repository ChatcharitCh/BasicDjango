from django.contrib import admin
from myapp.models import Person

# Register your models here.
admin.site.register(Person) # เอาโมเดล Person ให้ admin จัดการ
