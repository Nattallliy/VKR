from django.db import models

class Reviews(models.Model):
    """Отзывы"""

    name = models.CharField("Имя", max_length=100)
    text = models.TextField("Сообщение", max_length=5000)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"


class Applications(models.Model):
    """Заявка"""
    phone = models.CharField("Номер телефона", max_length=100)
    name = models.CharField("Имя", max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"

class Mails(models.Model):
    """Отзывы"""
    email = models.EmailField()
    name = models.CharField("Имя", max_length=100)
    text = models.TextField("Сообщение", max_length=5000)


    def __str__(self):
        return f'{self.name} {self.email}'

    class Meta:
        verbose_name = "Почта"
        verbose_name_plural = "Почта"

