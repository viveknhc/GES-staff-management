from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import Group, Permission

from django.db.models import Sum
from django.utils import timezone


class CustomUserManager(BaseUserManager):
    def create_user(self, usename, password, **extra_fields):
        if not usename:
            raise ValueError(_('The usename must be set'))
        user = self.model(username=usename, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('user_type', 'management')
        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(username, password, **extra_fields)


USER_TYPE_COICES = (('detailer', 'Detailer'),
                    ('management', 'Management'),
                    ('checker', 'Checker'))


class User(AbstractUser):
    user_type = models.CharField(choices=USER_TYPE_COICES, max_length=50)
    username = models.CharField(max_length=200, unique=True)
    email = models.EmailField(verbose_name='email address',
                              max_length=255, unique=True, null=True, blank=True)
    phone = models.TextField(null=True, blank=True)
    is_staff = models.BooleanField(default=True, null=True, blank=True)
    is_active = models.BooleanField(default=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    first_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    last_login = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    groups = models.ManyToManyField(Group, related_name='custom_user_groups')
    user_permissions = models.ManyToManyField(
        Permission, related_name='custom_user_permissions')

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['password']

    objects = CustomUserManager()


class Detailer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    phone = models.IntegerField()

    def __str__(self):
        return self.name


class Checker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    phone = models.IntegerField()

    def __str__(self):
        return self.name


class Client(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    assumed_no_of_sheet = models.IntegerField()
    assumed_wt = models.FloatField()
    submission_date = models.DateField()
    first_check_complete = models.DateField(default=None,blank=True, null=True)
    comments = models.TextField(default=None,blank=True, null=True)
    second_check_complete = models.DateField(default=None,blank=True, null=True)
    actual_submission = models.DateField(default=None,blank=True, null=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    assigned_detailer = models.ForeignKey(Detailer, on_delete=models.CASCADE)
    assigned_checker = models.ForeignKey(Checker, on_delete=models.CASCADE)



    def __str__(self):
        return self.title
    def latest_percentage(self):
        latest_status = self.projectstatus_set.order_by('-updated_at').first()
        return latest_status.percentage if latest_status else 0


class ProjectStatus(models.Model):
    Status_Choice = (('start', 'Start'),
                     ('Ongoing', 'Ongoing'),
                     ('Completed', 'Completed'))
    project_status = models.CharField(choices=Status_Choice, max_length=200)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    percentage = models.IntegerField(default=0)
    daily_description = models.TextField(blank=True, null=True)
    wt_mt = models.FloatField()
    no_sheet = models.FloatField()
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.project.title


class MonthlyReport(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    monthly_wt_mt = models.FloatField()
    monthly_no_sheet = models.FloatField()
    
    def __str__(self):
        return self.project.title
    
    
    def update_monthly_totals(cls, user):
        projects = Project.objects.all()

        for project in projects:
            monthly_entries = ProjectStatus.objects.filter(
                project=project,
                user=user,
                updated_at__month=timezone.now().month
            )
            monthly_totals = monthly_entries.aggregate(
                total_wt_mt=Sum('wt_mt'),
                total_no_sheet=Sum('no_sheet')
            )
            
            monthly_wt_mt = monthly_totals['total_wt_mt'] or 0
            monthly_no_sheet = monthly_totals['total_no_sheet'] or 0

            monthlyReport.objects.update_or_create(
                user=user,
                project=project,
                defaults={
                    'monthly_wt_mt': monthly_wt_mt,
                    'monthly_no_sheet': monthly_no_sheet
                }
            )