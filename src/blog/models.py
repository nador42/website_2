from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
class Category(models.Model):
    name=models.CharField(max_length=36)
    slug=models.SlugField()


class BlogPost(models.Model):
    author=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    category=models.ManyToManyField(Category)
    title=models.CharField(max_length=100)
    slug=models.SlugField()
    published=models.BooleanField(default=False)
    date=models.DateField(blank=True,null=True)
    content=models.TextField()
    description=models.TextField()

    def publish_string(self):
        if self.published:
            return "cet article est publié"
        return "cet article n'est pas édité"

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=slugify(self.title)
        super().save(*args,**kwargs)

    def __str__(self):
        return self.title

    class Meta():
        verbose_name="Articles"
        ordering=["date","-published"]
    #chemin pour acceder à un article
    def get_absolute_url(self):
        return reverse("blog-post",kwargs={"pk":self.pk})
    @property
    def word_count(self):
        return len(self.content.split())