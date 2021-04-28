from django.db import models
from django.contrib.auth import get_user_model


CustomUser = get_user_model()

def image_storage_path(instance, filename):

    filename = instance.user.email + ".png"

    return "profile_pictures/UserID_{instance}/{filename}/".format(
        instance=instance.user.id,
        filename=filename
        )


class CustomerUser(CustomUser):

    is_customer = models.BooleanField(default=True)
    is_premium_account = models.BooleanField(default=False)

    class Meta:

        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'

    def __str__(self):

        return self.email


class MerchantUser(CustomUser):

    initial_name = models.CharField(verbose_name='A.k.a', max_length=100, blank=False, null=False, unique=True)
    is_merchant = models.BooleanField(default=True)

    class Meta:

        verbose_name = 'Merchant'
        verbose_name_plural = 'Merchants'

    def __str__(self):

        return self.email


class UserProfile(models.Model):

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    
    dates_of_birth = models.DateField(verbose_name='DoB', blank=True, null=True)
    phone_number = models.CharField(verbose_name='Phone Number', max_length=255, blank=True, null=True)
    address_line_1 = models.CharField(verbose_name='Address Line 1', max_length=255, blank=False, null=False)
    address_line_2 = models.CharField(verbose_name='address Line 2', max_length=255, blank=True, null=True)
    profile_picture = models.ImageField(upload_to=image_storage_path, verbose_name='Profile Picture', blank=True, null=True)
    postal_code = models.CharField(verbose_name='Postal Code', max_length=255, blank=True, null=True)
    city = models.CharField(verbose_name='City', max_length=255, blank=True, null=True)
    state = models.CharField(verbose_name='State', max_length=255, blank=True, null=True)
    country = models.CharField(verbose_name='Country', max_length=255, blank=True, null=True)

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:

        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'
        ordering = ['-date_created', ]

    def __str__(self):

        return self.user.first_name

    def get_full_address(self):

        full_address = self.address_line_1 + self.address_line_2
        full_region = self.postal_code + self.city + self.country

        return full_address + ', ' + full_region
