from django.db import models

# Create your models here.
class Victim(models.Model):

    slug = models.SlugField(max_length=255)

    image = models.ImageField(upload_to='victim_images', blank=True, null=True)

    name = models.CharField(verbose_name='Victim Name', max_length=255, blank=False, null=False)
    address = models.CharField(verbose_name='Address', max_length=255, blank=True, null=True)
    occupation = models.CharField(verbose_name='Occupation', max_length=255, blank=True, null=True)
    social_status = models.CharField(verbose_name='Social Status', max_length=255, blank=True, null=True)

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:

        verbose_name = 'Victim'
        verbose_name_plural = 'Victims'
        ordering = ('-date_created',)

    def __str__(self):

        return self.name
