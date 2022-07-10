from django.db import models

class News(models.Model):
    title=models.CharField(max_length=1500,verbose_name="News title")
    content=models.TextField(verbose_name="News content")
    image=models.FileField(verbose_name="News image",blank=True)
    date=models.DateField(verbose_name="Tarix",null=True,blank=True)
    draft=models.BooleanField(default=True,verbose_name="is Publish?")

    def __str__(self):
        return self.title
    class Meta:
        verbose_name="News"
        verbose_name_plural="News"
        ordering=['id']




