from django.db import models


class Peoples(models.Model):
    FIO = models.CharField(max_length=128)

    class Meta:
        verbose_name = 'Тренер'
        verbose_name_plural = 'Тренера'

    def __str__(self):
        return self.FIO


class Class(models.Model):
    train = models.CharField(max_length=128)

    class Meta:
        verbose_name = 'Занятие'
        verbose_name_plural = 'Занятия'

    def __str__(self):
        return self.train


class Time(models.Model):
    time = models.CharField(max_length=128)


    class Meta:
        verbose_name = 'Время'
        verbose_name_plural = 'Время'

    def __str__(self):
        return self.time


class Week(models.Model):
    week = models.CharField(max_length=128,  null=True)
    time = models.ForeignKey('Time', on_delete=models.CASCADE, null=True)
    train = models.ForeignKey('Class', on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=128, null=True)
    FIO = models.ForeignKey('Peoples', on_delete=models.CASCADE, null=True)
    date = models.DateField('дата')




    class Meta:
        verbose_name = 'День недели'
        verbose_name_plural = 'Дни недели'


    def __str__(self):
        return f'{self.week} {self.time}'





