from django.db import models

# Create your models here.

from django import forms
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.core import validators

from django.utils.translation import ugettext_lazy as _

from decimal import Decimal

class UserManager(BaseUserManager):
  def create_user(self, first_name, last_name, user_handle, email, password):

    user = self.model(
      first_name=first_name,
      last_name=last_name,
      user_handle=user_handle,
      email=email,
    )

    user.set_password(password)
    user.save(using=self._db)
    return user


class User(AbstractBaseUser):
  first_name = models.CharField(_('First Name'),max_length=30, blank=False)
  last_name = models.CharField(_('Last Name'), max_length=30, blank=False)
  
  user_handle = models.CharField(max_length=20, unique=True)

  email = models.EmailField(_('Email Address'), max_length=255, unique=True)
  
  #new fields - profile_pic, donation_total
  profile_pic = models.FileField(_('Profile Picture'), null=True)
  ###############
  
  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['first_name', 'last_name', 'user_handle']

  is_active = models.BooleanField(default=True)

  objects = UserManager()
  
  def get_full_name(self):
    return self.user_handle
  
  
  def get_short_name():
    return self.user_handle

  def __unicode__(self):
    return  self.user_handle + "  id:" + str(self.id)


class UserCreatorForm(forms.ModelForm):  
  password1 = forms.CharField(label=_("Password"), widget=forms.PasswordInput)
  password2 = forms.CharField(label=_("Password confirmation"), widget=forms.PasswordInput)

  class Meta:
    model = User
    fields = ("first_name", "last_name", "user_handle", "email")

  def clean_username(self):
    username = self.cleaned_data["user_handle"]
    try:
      User._default_manager.get(username=username)
    except User.DoesNotExist:
      return username
    raise forms.ValidationError(
      self.error_messages['duplicate_username'],
      code='duplicate_username',
    )

  def clean_password2(self):
    password1 = self.cleaned_data.get("password1")
    password2 = self.cleaned_data.get("password2")
    if password1 and password2 and password1 != password2:
      raise forms.ValidationError(
        self.error_messages['password_mismatch'],
        code='password_mismatch',
      )
    return password2

  def save(self, commit=True):
    user = super(UserCreatorForm, self).save(commit=False)
    user.set_password(self.cleaned_data["password1"])
    if commit:
      user.save()
    return user
