from django.test import TestCase
from django.contrib.auth import get_user_model
from accounts.models import UserProfile


CustomUser = get_user_model()


class TestCustomUser(TestCase):

    def setUp(self):
        email = 'customusertest@unittest.com'
        username = 'usertest'
        password = 'foo'
        first_name = 'Tester'
        last_name = 'Unitester'

        self.custom_user = CustomUser.objects.create_user(
            email=email,
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name
        )

        self.admin_user = CustomUser.objects.create_superuser(
            email='adminusertest@unittest.com',
            username='admintest',
            password=password,
            first_name=first_name,
            last_name=last_name
        )

    def test_user_creation(self):
        custom_user = self.custom_user

        self.assertTrue(isinstance(custom_user, CustomUser))
        self.assertFalse(custom_user.is_active)
        self.assertFalse(custom_user.is_admin)
        self.assertFalse(custom_user.is_staff)
        self.assertFalse(custom_user.is_superadmin)
        self.assertEqual(custom_user.username, 'usertest')
        self.assertEqual(custom_user.first_name, 'Tester')
        self.assertEqual(custom_user.last_name, 'Unitester')
        self.assertEqual(custom_user.email, 'customusertest@unittest.com')
        self.assertEqual(custom_user.full_name(), f"{custom_user.first_name} {custom_user.last_name}")

    def test_superuser_creation(self):
        admin_user = self.admin_user

        self.assertTrue(isinstance(admin_user, CustomUser))
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_admin)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superadmin)
        self.assertEqual(admin_user.__str__(), admin_user.email)


class TestUserProfile(TestCase):

    def setUp(self):

        email = 'customusertest@unittest.com'
        username = 'usertest'
        password = 'foo'
        first_name = 'Tester'
        last_name = 'Unitester'

        self.custom_user = CustomUser.objects.create_user(
            email=email,
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name
        )

        self.user_profile = UserProfile.objects.create(
            user=self.custom_user,
            address_line_1='Storkower Str. 108',
            address_line_2='17/07',
            postal_code='10407',
            city='Berlin',
            country='Germany'
        )

    def test_userprofile_creation(self):

        user_profile = self.user_profile

        self.assertTrue(isinstance(user_profile, UserProfile))
        self.assertEqual(user_profile.profile_picture, 'avatar/avatar-default.png')
        self.assertEqual(user_profile.__str__(), user_profile.user.first_name)
        self.assertEqual(
            user_profile.full_address(),
            f"{user_profile.address_line_1} {user_profile.address_line_2}, " +
            f"{user_profile.postal_code} {user_profile.city} {user_profile.country}"
        )
