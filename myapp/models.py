from django.db import models

# Create your models here.
class Person(models.Model): # สร้างคลาสข้อมูลประชากร
    
    name = models.CharField(max_length = 100)
    age = models.IntegerField()
    date = models.DateField(auto_now_add = True)

    # แปลง object ให้เป็น string
    def __str__(self) -> str:
        return self.name + " ," + str(self.age)
