from django.db import models

from ckeditor.fields import RichTextField

# Create your models here.

class Team_Member(models.Model):
    name = models.CharField(max_length=50)
    discription = models.CharField(max_length=50)
    img = models.ImageField()

    facebook = models.URLField( max_length=200 , blank=True)
    youtube = models.URLField( max_length=200 , blank=True)
    instgram = models.URLField( max_length=200 , blank=True)
    twitter = models.URLField( max_length=200 , blank=True)


    class Meta:
        verbose_name : "Team_Member"
        verbose_name_plural : "Team_Members"

    def __str__(self):
        return self.name

class rapper(models.Model):

    name = models.CharField(max_length=50)
    nickname = models.CharField(max_length=50)
    img = models.ImageField()

    date_of_born = models.DateField()
    place_of_born = models.CharField(max_length=100)

    about_him = RichTextField()

    
    facebook = models.URLField( max_length=200 , blank=True)
    instgram = models.URLField( max_length=200 , blank=True)
    twitter = models.URLField( max_length=200 , blank=True)

    youtube = models.URLField( max_length=200 , blank=True)
    anghami = models.URLField( max_length=200 , blank=True)
    spotify = models.URLField( max_length=200 , blank=True)
    deezer = models.URLField( max_length=200 , blank=True)

    class Meta:
        verbose_name : "rapper"
        verbose_name_plural : "rappers"

    def __str__(self):
        return f"{self.name} || {self.nickname}" 

class article(models.Model):
    title = models.CharField(max_length=50,null=True)
    img = models.ImageField(null=True)
    rapper =  models.ForeignKey(rapper, verbose_name="article", on_delete=models.CASCADE)
    article_content = RichTextField()
    created_dt = models.DateTimeField(auto_now_add=True,null=True)
    class Meta:
        verbose_name : "article"
        verbose_name_plural :"articles"

    def __str__(self):
        return self.title



class ad(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone =  models.CharField(max_length=11)
    msg = models.TextField(max_length=250)
    class Meta:
        verbose_name : "ad"
        verbose_name_plural :"ads"

    def __str__(self):
        return self.name

