from django.db import models

# ไฟล์นี้จะให้เราออกแบบว่าข้อมูลที่จะจัดเก็บในฐานข้อมูลมีโครงสร้างเป็นอย่างไร
class Person(models.Model): # ต้องสืบทอดมาจากคลาสโมเดล
    
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    age = models.IntegerField()
    date = models.DateField(auto_now_add=True)
