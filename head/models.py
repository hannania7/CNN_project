# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
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
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Cinemas(models.Model):
    cine_id = models.AutoField(primary_key=True)
    cine_name = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    current_movies = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cinemas'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
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
    id = models.BigAutoField(primary_key=True)
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


class Finaldb(models.Model):
    dbid = models.CharField(max_length=30, blank=True, null=True)
    gender = models.CharField(max_length=100, blank=True, null=True)
    age = models.CharField(max_length=100, blank=True, null=True)
    shampoo_count = models.CharField(max_length=100, blank=True, null=True)
    now_hair = models.CharField(max_length=100, blank=True, null=True)
    hair_product = models.CharField(max_length=100, blank=True, null=True)
    perm = models.CharField(max_length=100, blank=True, null=True)
    color_count = models.CharField(max_length=100, blank=True, null=True)
    shampoo_buy = models.CharField(max_length=100, blank=True, null=True)
    product_want = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'finaldb'


class Members(models.Model):
    id = models.IntegerField(blank=True, null=True)
    member_id = models.CharField(primary_key=True, max_length=255)
    member_pw = models.CharField(max_length=255, blank=True, null=True)
    member_name = models.CharField(max_length=255, blank=True, null=True)
    member_tel = models.CharField(max_length=255, blank=True, null=True)
    resident_num = models.CharField(max_length=255, blank=True, null=True)
    birth = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=255, blank=True, null=True)
    like_genre = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'members'


class MovieSchedule(models.Model):
    schedule_id = models.AutoField(primary_key=True)
    cine = models.ForeignKey(Cinemas, models.DO_NOTHING, blank=True, null=True)
    movie = models.ForeignKey('Movies', models.DO_NOTHING, blank=True, null=True)
    movie_name = models.CharField(max_length=255, blank=True, null=True)
    house_num = models.CharField(max_length=255, blank=True, null=True)
    movie_time = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'movie_schedule'


class MovieSchedules(models.Model):
    schedule_id = models.IntegerField(primary_key=True)
    cine = models.ForeignKey(Cinemas, models.DO_NOTHING, blank=True, null=True)
    cine_name = models.CharField(max_length=255, blank=True, null=True)
    movie = models.ForeignKey('Movies', models.DO_NOTHING, blank=True, null=True)
    movie_name = models.CharField(max_length=255, blank=True, null=True)
    house_num = models.CharField(max_length=255, blank=True, null=True)
    movie_time = models.CharField(max_length=255, blank=True, null=True)
    movie_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'movie_schedules'


class Movies(models.Model):
    movie_id = models.IntegerField(primary_key=True)
    movie_name = models.CharField(max_length=255, blank=True, null=True)
    director = models.CharField(max_length=255, blank=True, null=True)
    actor = models.CharField(max_length=255, blank=True, null=True)
    genre = models.CharField(max_length=255, blank=True, null=True)
    age_limit = models.CharField(max_length=255, blank=True, null=True)
    story = models.TextField(blank=True, null=True)
    open_date = models.DateField(blank=True, null=True)
    close_date = models.DateField(blank=True, null=True)
    poster_src = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'movies'


class MymovieRe(models.Model):
    post_id = models.AutoField(primary_key=True)
    re_pw = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    cont = models.TextField(blank=True, null=True)
    like_genre = models.CharField(max_length=255, blank=True, null=True)
    bip = models.CharField(max_length=255, blank=True, null=True)
    bdate = models.DateTimeField(blank=True, null=True)
    readcnt = models.IntegerField(blank=True, null=True)
    gnum = models.IntegerField(blank=True, null=True)
    onum = models.IntegerField(blank=True, null=True)
    nested = models.IntegerField(blank=True, null=True)
    member = models.ForeignKey(Members, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mymovie_re'


class Nonmembers(models.Model):
    nm_id = models.IntegerField(primary_key=True)
    nm_birth = models.DateField(blank=True, null=True)
    nm_tel = models.CharField(max_length=255, blank=True, null=True)
    nm_pw = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nonmembers'


class Survey(models.Model):
    id = models.IntegerField(primary_key=True)
    gender = models.CharField(max_length=255, blank=True, null=True)
    age = models.CharField(max_length=255, blank=True, null=True)
    shampoo = models.CharField(max_length=255, blank=True, null=True)
    perm = models.CharField(max_length=255, blank=True, null=True)
    dye = models.CharField(max_length=255, blank=True, null=True)
    current_hair = models.CharField(max_length=255, blank=True, null=True)
    product = models.CharField(max_length=255, blank=True, null=True)
    care_prefer = models.CharField(max_length=255, blank=True, null=True)
    buying_point = models.CharField(max_length=255, blank=True, null=True)
    label = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'survey'


class Tickets(models.Model):
    ticket_id = models.IntegerField(primary_key=True)
    ticket_date = models.DateTimeField(blank=True, null=True)
    cine_name = models.CharField(max_length=255, blank=True, null=True)
    seat = models.CharField(max_length=255, blank=True, null=True)
    movie = models.ForeignKey(Movies, models.DO_NOTHING, blank=True, null=True)
    movie_name = models.CharField(max_length=255, blank=True, null=True)
    member = models.ForeignKey(Members, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tickets'


class TicketsNm(models.Model):
    ticket_id = models.IntegerField(primary_key=True)
    ticket_date = models.DateTimeField(blank=True, null=True)
    cine_name = models.CharField(max_length=255, blank=True, null=True)
    seat = models.CharField(max_length=255, blank=True, null=True)
    movie_id = models.IntegerField(blank=True, null=True)
    movie_name = models.CharField(max_length=255, blank=True, null=True)
    nm = models.ForeignKey(Nonmembers, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'tickets_nm'


class Voc(models.Model):
    post_id = models.AutoField(primary_key=True)
    voc_pw = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    cont = models.TextField(blank=True, null=True)
    voc_type = models.CharField(max_length=255, blank=True, null=True)
    bip = models.CharField(max_length=255, blank=True, null=True)
    bdate = models.DateTimeField(blank=True, null=True)
    readcnt = models.IntegerField(blank=True, null=True)
    gnum = models.IntegerField(blank=True, null=True)
    onum = models.IntegerField(blank=True, null=True)
    nested = models.IntegerField(blank=True, null=True)
    member = models.ForeignKey(Members, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'voc'
