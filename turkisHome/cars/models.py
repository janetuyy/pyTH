from django.db import models

class Cars(models.Model):
    title = models.CharField('Название', max_length=50)
    cover = models.ImageField('Фото', upload_to='images/', blank=True)
    anons = models.CharField('Анонс', max_length=250)
    full_text = models.TextField('Основная информация')

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Машина в аренду'
        verbose_name_plural = 'Машины в аренду'