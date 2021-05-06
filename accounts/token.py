from django.contrib.auth.tokens import PasswordResetTokenGenerator
from six import text_type


class CustomAccountActivationTokenGenerator(PasswordResetTokenGenerator):

    def _make_hash_value(self, user, date_joined):
        return (text_type(user.pk) + text_type(date_joined) + text_type(user.is_active))


custom_activation_token_generator = CustomAccountActivationTokenGenerator()
