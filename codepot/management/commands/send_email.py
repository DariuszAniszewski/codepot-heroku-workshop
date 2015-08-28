from time import sleep

from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.mail.message import EmailMultiAlternatives
from django.core.management.base import BaseCommand
from django.core.validators import validate_email


class Command(BaseCommand):
    help = 'Send email to Dariusz and you in CC'

    def handle(self, *args, **options):
        if not settings.EMAIL_HOST:
            print("Please add Mailgun first and try again")
            return
        if not settings.MY_EMAIL:
            print("Please set MY_EMAIL environment variable and try again")
            return
        if not settings.MY_NAME:
            print("Please set MY_NAME environment variable and try again")
            return

        try:
            validate_email(settings.MY_EMAIL)
        except ValidationError:
            print("Aw please...")
            print("Did you really expect I will accept {} as an email?")
            sleep(2)
            print("Really??")
            print("Please set MY_EMAIL environment variable correctly and try again")
            return

        EmailMultiAlternatives(
            "Hey, I'm done!",
            "My name is {} and I've completed this task!".format(settings.MY_NAME),
            settings.FROM_EMAIL,
            [settings.DARIUSZ_EMAIL],
            cc=[settings.MY_EMAIL],
            reply_to=[settings.MY_EMAIL],
        ).send()
        print("Looks like your email was send! Check your email, you're in CC :)")