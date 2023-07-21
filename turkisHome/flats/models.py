from django.db import models

class Flats(models.Model):
    title = models.CharField('Название', max_length=50)
    cover1 = models.ImageField('Фото 1', upload_to='images/', blank=True)
    cover2 = models.ImageField('Фото 2', upload_to='images/', blank=True)
    cover3 = models.ImageField('Фото 3', upload_to='images/', blank=True)
    cover4 = models.ImageField('Фото 4', upload_to='images/', blank=True)
    cover5 = models.ImageField('Фото 5', upload_to='images/', blank=True)
    anons = models.CharField('Анонс', max_length=250)
    full_text = models.TextField('Основная информация')

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Квартира в аренду'
        verbose_name_plural = 'Квартиры в аренду'