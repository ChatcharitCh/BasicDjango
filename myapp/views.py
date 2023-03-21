from django.shortcuts import render
from django.http import HttpResponse # ส่งข้อความตอบกลับ
from myapp.models import Person

# Create your views here.
def index(request): # สร้างฟังก์ชั่นส่งข้อความไปแสดงผลหน้าเว็ป
    all_person = Person.objects.all() # ดึงข้อมูลประชากรทั้งหมดมาทำงานที่ views.py
    return render(request, "index.html", {"all_person": all_person}) # แทรกตัวแปรในหน้าเว็บ

def about(request):
    return render(request, "about.html")

def form(request):
    return render(request, "form.html")