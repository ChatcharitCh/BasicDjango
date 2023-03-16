from django.shortcuts import render
from django.http import HttpResponse # ส่งข้อความตอบกลับ

# Create your views here.
def index(request): # สร้างฟังก์ชั่นส่งข้อความไปแสดงผลหน้าเว็ป
    fname = "Chatcharit"
    lname = "Choocherd"
    age = 27
    return render(request, "index.html", {"fname": fname, "lname": lname,"age": age}) # แทรกตัวแปรในหน้าเว็บ

def about(request):
    return render(request, "about.html")

def form(request):
    return render(request, "form.html")