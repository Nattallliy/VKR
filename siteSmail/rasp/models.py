from django.db import models


class Peoples(models.Model):
    FIO = models.CharField("ФИО", max_length=128)

    class Meta:
        verbose_name = 'Тренер'
        verbose_name_plural = 'Тренера'

    def __str__(self):
        return self.FIO

class Month(models.Model):
    month = models.CharField("Месяц", max_length=128)

    class Meta:
        verbose_name = 'Месяц'
        verbose_name_plural = 'Месяцы'

    def __str__(self):
        return self.month

class Class(models.Model):
    train = models.CharField("Тренировка", max_length=128)

    class Meta:
        verbose_name = 'Занятие'
        verbose_name_plural = 'Занятия'

    def __str__(self):
        return self.train


class Time(models.Model):
    time = models.CharField("Время", max_length=128)


    class Meta:
        verbose_name = 'Время'
        verbose_name_plural = 'Время'

    def __str__(self):
        return self.time


class Week(models.Model):
    month = models.ForeignKey('Month', on_delete=models.CASCADE, null=True)
    week = models.CharField("День недели", max_length=128,  null=True)
    time = models.ForeignKey('Time', on_delete=models.CASCADE, null=True)
    train = models.ForeignKey('Class', on_delete=models.CASCADE, null=True)
    title = models.CharField("Доп. запись", max_length=128, null=True)
    FIO = models.ForeignKey('Peoples', on_delete=models.CASCADE, null=True)
    date = models.DateField('дата')




    class Meta:
        verbose_name = 'Расписание занятий'
        verbose_name_plural = 'Расписание занятий'


    def __str__(self):
        return f'{self.month} {self.week} {self.time}'





