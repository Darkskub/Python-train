from django.urls import reverse
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Gingerbreads(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержание")
    date_published = models.DateTimeField(default=timezone.now ,verbose_name="Дата публикации")
    images = models.ImageField(upload_to="images/", verbose_name="Изображение")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор", null=True, blank=True)
    def __str__(self):
       return f"{self.title}"
    
    def get_absolute_url(self):
        return reverse("news:Gingerbreads_detail", kwargs={"pk": self.pk})
    
    
        

class Comment(models.Model):
    blog = models.ForeignKey(Gingerbreads, on_delete=models.CASCADE, verbose_name="Блог")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор", null=True, blank=True)
    text = models.TextField(verbose_name="Текст комментария")
    date_published = models.DateTimeField(default=timezone.now ,verbose_name="Дата публикации")

    def __str__(self):
        return str(self.text)
    
   
        