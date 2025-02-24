# user/adapters.py
from allauth.account.adapter import DefaultAccountAdapter


class NoPasswordValidationAdapter(DefaultAccountAdapter):
    def clean_password(self, password, user=None):
        return password
