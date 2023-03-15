from django.shortcuts import render
from django.http import HttpResponse # ส่งข้อความตอบกลับ

# Create your views here.
def index(request): # สร้างฟังก์ชั่นส่งข้อความไปแสดงผลหน้าเว็ป
    return HttpResponse("<h1>Hello Mr.Chatcharit</h1>")

def about(request):
    return HttpResponse("<h1>About Me</h1>")

def form(request):
    return HttpResponse("<h1>Information Form</h1>")