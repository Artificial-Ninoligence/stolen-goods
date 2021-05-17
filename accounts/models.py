from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


def image_storage_path(instance, filename):

    filename = instance.user.email + ".png"

    return "profile_pictures/UserID_{instance}/{filename}/".format(
        instance=instance.user.id,
        filename=filename
    )


class MyAccountManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, email, password=None):
        if not email:
            raise ValueError('User must have an email address')

        if not username:
            raise ValueError('User must have an username')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser):
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    username = models.CharField(max_length=50, blank=False, null=False, unique=True)
    email = models.EmailField(max_length=100, blank=False, null=False, unique=True)

    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    objects = MyAccountManager()

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True

    def __str__(self):
        return self.email


class UserProfile(models.Model):

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    dates_of_birth = models.DateField(verbose_name='DoB', blank=True, null=True)
    phone_number = models.CharField(verbose_name='Phone Number', max_length=255, blank=True, null=True)
    address_line_1 = models.CharField(verbose_name='Address Line 1', max_length=255, blank=True, null=True)
    address_line_2 = models.CharField(verbose_name='address Line 2', max_length=255, blank=True, null=True)
    profile_picture = models.ImageField(
        upload_to=image_storage_path,
        default='avatar/avatar-default.png',
        verbose_name='Profile Picture',
        blank=True,
        null=True
    )
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

    def full_address(self):

        return f'{self.address_line_1} {self.address_line_2}, {self.postal_code} {self.city} {self.country}'

    def __str__(self):

        return self.user.first_name
