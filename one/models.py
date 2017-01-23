# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models
import sys
reload(sys)
sys.setdefaultencoding('utf8')

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Daily(models.Model):
    id = models.IntegerField(primary_key=True)
    hpcontent_id = models.CharField(max_length=11, blank=True, null=True)
    hp_title = models.CharField(max_length=255, blank=True, null=True)
    author_id = models.IntegerField(blank=True, null=True)
    hp_img_url = models.CharField(max_length=255, blank=True, null=True)
    hp_img_original_url = models.CharField(max_length=255, blank=True, null=True)
    hp_author = models.CharField(max_length=255, blank=True, null=True)
    ipad_url = models.CharField(max_length=255, blank=True, null=True)
    hp_content = models.CharField(max_length=800, blank=True, null=True)
    hp_makettime = models.CharField(max_length=255, blank=True, null=True)
    hide_flag = models.CharField(max_length=255, blank=True, null=True)
    last_update_date = models.CharField(max_length=255, blank=True, null=True)
    web_url = models.CharField(max_length=255, blank=True, null=True)
    wb_img_url = models.CharField(max_length=255, blank=True, null=True)
    image_authors = models.CharField(max_length=255, blank=True, null=True)
    text_authors = models.CharField(max_length=255, blank=True, null=True)
    image_from = models.CharField(max_length=255, blank=True, null=True)
    text_from = models.CharField(max_length=255, blank=True, null=True)
    content_bgcolor = models.CharField(max_length=255, blank=True, null=True)
    maketime = models.CharField(max_length=255, blank=True, null=True)
    praisenum = models.IntegerField(blank=True, null=True)
    sharenum = models.IntegerField(blank=True, null=True)
    commentnum = models.IntegerField(blank=True, null=True)
    template_category = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'daily'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class RangoCategory(models.Model):
    name = models.CharField(unique=True, max_length=128)

    class Meta:
        managed = False
        db_table = 'rango_category'


class RangoPage(models.Model):
    title = models.CharField(max_length=128)
    url = models.CharField(max_length=200)
    views = models.IntegerField()
    category = models.ForeignKey(RangoCategory, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'rango_page'
