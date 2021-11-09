from django.db import models

# Create your models here.
class novels(models.Model):
    title=models.CharField('novel name',max_length=120)
    author=models.CharField('author',max_length=120)

    def __str__(self) :
        return self.title


class review(models.Model):
    name=models.ForeignKey(novels, on_delete=models.CASCADE)
    chapter_no=models.CharField('chapter number',max_length=10)
    date=models.DateField()
    description=models.TextField(blank=True)


    def __str__(self) :
        return self.name.title+'/'+self.chapter_no

