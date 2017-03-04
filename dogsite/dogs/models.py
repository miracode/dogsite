from django.db import models


class Dog(models.Model):
    name = models.CharField(max_length=50, verbose_name=u"Dog's Name")
    owner = models.CharField(max_length=50, verbose_name=u"Owner's Name")
    photo = models.ImageField(upload_to='dogs', verbose_name=u"Photo of Dog")

    def __unicode__(self):
        return u'%s' % self.name
