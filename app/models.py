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


class ChiTietDatHang(models.Model):
    id_nguoi_dung = models.ForeignKey('NguoiDung', models.DO_NOTHING, db_column='ID_nguoi_dung', blank=True, null=True)  # Field name made lowercase.
    id_san_pham = models.ForeignKey('SanPham', models.DO_NOTHING, db_column='ID_san_pham', blank=True, null=True)  # Field name made lowercase.
    so_luong = models.IntegerField(blank=True, null=True)
    ghi_chu = models.TextField(blank=True, null=True)
    id_dat_hang = models.ForeignKey('DatHang', models.DO_NOTHING, db_column='ID_dat_hang', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'chi_tiet_dat_hang'


class DatHang(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_nguoi_dung = models.ForeignKey('NguoiDung', models.DO_NOTHING, db_column='ID_nguoi_dung', blank=True, null=True)  # Field name made lowercase.
    ghi_chu = models.TextField(blank=True, null=True)
    ma_giam_gia = models.CharField(max_length=50, blank=True, null=True)
    trang_thai_dat_hang = models.CharField(max_length=255, blank=True, null=True)
    ngay_them = models.DateTimeField()
    dia_chi = models.TextField(blank=True, null=True)
    sdt = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dat_hang'


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


class NguoiDung(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    ho_dem = models.CharField(max_length=255, blank=True, null=True)
    ten = models.CharField(max_length=255, blank=True, null=True)
    ho_va_ten = models.CharField(max_length=255, blank=True, null=True)
    chi_tieu = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    ngay_sinh = models.DateField(blank=True, null=True)
    so_dien_thoai = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    mat_khau = models.CharField(max_length=255, blank=True, null=True)
    dia_chi = models.TextField(blank=True, null=True)
    ngay_them = models.DateTimeField()
    ngay_cap_nhat = models.DateTimeField()
    vai_tro = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nguoi_dung'


class SanPham(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    ten_san_pham = models.CharField(max_length=255, blank=True, null=True)
    gia_san_pham = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    mo_ta_san_pham = models.TextField(blank=True, null=True)
    so_luong_san_pham = models.CharField(max_length=11, blank=True, null=True)
    hinh_anh_san_pham = models.CharField(max_length=255, blank=True, null=True)
    ngay_them = models.DateTimeField()
    ngay_cap_nhat = models.DateTimeField()
    loai_san_pham = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'san_pham'


class TrangThaiNguoiDung(models.Model):
    id_nguoi_dung = models.OneToOneField(NguoiDung, models.DO_NOTHING, db_column='ID_nguoi_dung', primary_key=True)  # Field name made lowercase.
    trang_thai = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trang_thai_nguoi_dung'
