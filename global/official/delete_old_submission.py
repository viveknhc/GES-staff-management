# from django.core.management.base import BaseCommand
# from datetime import timedelta
# from your_app.models import Student

# class Command(BaseCommand):
#     help = 'Deletes students older than two days.'

#     def handle(self, *args, **options):
#         two_days_ago = timezone.now() - timedelta(days=2)
#         Student.objects.filter(registration_date__lt=two_days_ago).delete()
#         self.stdout.write(self.style.SUCCESS('Successfully deleted old students.'))