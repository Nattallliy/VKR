#from django.db import models
#from datetime import date

#from django.urls import reverse

#class Reviews(models.Model):
 #   """Отзывы"""
  #  email = models.EmailField()
   # name = models.CharField("Имя", max_length=100)
   # text = models.TextField("Сообщение", max_length=5000)
   # parent = models.ForeignKey(
    #    'self', verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True
   # )

   # def __str__(self):
    #    return f"{self.name} - {self.movie}"

    #class Meta:
     #   verbose_name = "Отзыв"
      #  verbose_name_plural = "Отзывы"