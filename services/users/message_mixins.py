
from typing import Any, Callable

from django.conf import settings
from django.contrib.auth import get_user_model, login
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.models import Site
from django.db.models import Model
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import loader
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.core.mail import send_mail








