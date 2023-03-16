from django.shortcuts import render
from django.http import HttpResponse # ส่งข้อความตอบกลับ

# Create your views here.
def index(request): # สร้างฟังก์ชั่นส่งข้อความไปแสดงผลหน้าเว็ป
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def form(request):
    return render(request, "form.html")