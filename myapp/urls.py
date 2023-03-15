# สร้างไฟล์ขึ้นมา
from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index), # ตัวแรกเป็นชื่อพาท(ถ้าค่าเปล่าๆ คือ หน้าแรก) ตัวที่สองเป็นกระบวนการทำงาน
    path('about', views.about),
    path('form', views.form)
]