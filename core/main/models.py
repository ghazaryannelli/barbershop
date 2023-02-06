from django.db import models

# Create your models here.
class HomeLogo(models.Model):
    img = models.ImageField('HomeLogo image', upload_to='media')

class HomeBG(models.Model):
    img = models.ImageField('HomeBG image', upload_to='media')

class HomeBgInfo(models.Model):
    name1 = models.CharField('Homebg name1', max_length=30)
    name2 = models.CharField('Homebg name2', max_length=30)
    name3 = models.CharField('Homebg name3', max_length=30)
    name4 = models.CharField('Homebg name4', max_length=30)


    def __str__(self):
        return self.name1
    
class HomeBest(models.Model):
    name5 = models.CharField('Homebest name5', max_length=30)
    name6 = models.CharField('Homebest name6', max_length=1000)
    img1 = models.ImageField('HomeBest image', upload_to='media')
    img2 = models.ImageField('HomeBest image', upload_to='media')

    def __str__(self):
        return self.name5
    
class HomeGet(models.Model):
    name7 = models.CharField('Homeget name7', max_length=100)
    name8 = models.CharField('Homeget name8', max_length=100)
    name9 = models.CharField('Homeget name9', max_length=100)
    

    def __str__(self):
        return self.name7
    

    
class HomeServices(models.Model):
    name10 = models.CharField('Homeservices name10', max_length=100)
    name11 = models.CharField('Homeservices name11', max_length=1000)
    img11 = models.ImageField('Homeservices image', upload_to='media')
    price11 = models.IntegerField('Homeservices price')

    name12 = models.CharField('Homeservices name12', max_length=1000)
    img12 = models.ImageField('Homeservices image', upload_to='media')
    price12 = models.IntegerField('Homeservices price')

    name13 = models.CharField('Homeservices name13', max_length=1000)
    img13 = models.ImageField('Homeservices image', upload_to='media')
    price13 = models.IntegerField('Homeservices price')


    name14 = models.CharField('Homeservices name14', max_length=1000)
    img14 = models.ImageField('Homeservices image', upload_to='media')
    price14 = models.IntegerField('Homeservices price')

    def __str__(self):
        return self.name10
    
class HomePrice(models.Model):
    name1 = models.CharField('Homeprice name1', max_length=100)
    name2 = models.CharField('Homeprice name2', max_length=100)
    name3 = models.CharField('Homeprice name3', max_length=100)
    name4 = models.CharField('Homeprice name4', max_length=100)
    name5 = models.CharField('Homeprice name5', max_length=100)
    name6 = models.CharField('Homeprice name6', max_length=100)
    name7 = models.CharField('Homeprice name7', max_length=100)
    img = models.ImageField('Homeprice image', upload_to='media')
    price1 = models.IntegerField('Homeprice price')
    price2 = models.IntegerField('Homeprice price')
    price3 = models.IntegerField('Homeprice price')
    price4 = models.IntegerField('Homeprice price')
    price5 = models.IntegerField('Homeprice price')

    def __str__(self):
        return self.name1
    
class HomeHello(models.Model):
    name = models.CharField('Homehello name1', max_length=100)

    def __str__(self):
        return self.name
    
class HomeOur(models.Model):
    name = models.CharField('Homeour name', max_length=100)
    name1 = models.CharField('Homeour name1', max_length=100)
    name2 = models.CharField('Homeour name2', max_length=100)
    name3 = models.CharField('Homeour name3', max_length=100)
    name4 = models.CharField('Homeour name4', max_length=100)
    name5 = models.CharField('Homeour name5', max_length=100)
    name6 = models.CharField('Homeour name6', max_length=100)


    def __str__(self):
        return self.name