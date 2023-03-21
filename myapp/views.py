from django.shortcuts import render, redirect
from django.http import HttpResponse # ส่งข้อความตอบกลับ
from myapp.models import Person
from django.contrib import messages 

# Create your views here.
def index(request): # สร้างฟังก์ชั่นส่งข้อความไปแสดงผลหน้าเว็ป
    all_person = Person.objects.all() # ดึงข้อมูลประชากรทั้งหมดมาทำงานที่ views.py
    return render(request, "index.html", {"all_person": all_person}) # แทรกตัวแปรในหน้าเว็บ

def about(request):
    return render(request, "about.html")

def form(request):
    if request.method == "POST":
        # รับข้อมูล
        name = request.POST["name"]
        age = request.POST["age"]
        print(name, age)
        
        # บันทึกข้อมูล
        person = Person.objects.create(
            name = name, # ด้านหน้าเป็นชื่อฟิลด์ ด้านหลังเป็นข้อมูลที่จะมาทำงานกับฟิลด์
            age = age
        )
        person.save()
        messages.success(request, "Save Successful")
        # เปลี่ยนเส้นทางกลับหน้าแรก
        return redirect("/")
    else :
        return render(request, "form.html")
    
def edit(request, person_id):
    if request.method == "POST": # ถ้ามีการส่งข้อมูลมาแก้ไขจะให้
        person = Person.objects.get(id = person_id)
        person.name = request.POST["name"] # ส่งชื่อมาเปลี่ยนที่ person.name
        person.age = request.POST["age"]
        person.save()
        messages.success(request, "Updated Successful")    
        return redirect("/")
    else :    
        person = Person.objects.get(id = person_id) # ดึงข้อมูลประชากรที่ต้องการแก้ไข
        return render(request, "edit.html", {"person": person})