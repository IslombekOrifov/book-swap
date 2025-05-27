from django.db import models

from account.models import CustomUser
from book.models import Book


class Exchange(models.Model):
    class Status(models.TextChoices):
        ACTIVE = 'ac', 'Active'
        ACCEPTED = 'ad', 'Accepted'
        REJECTED = 'rd', 'Rejected'
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    from_user = models.ForeignKey(CustomUser, related_name='sent_exchanges', on_delete=models.CASCADE)
    to_user = models.ForeignKey(CustomUser, related_name='received_exchanges', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.ACTIVE)
    is_completed = models.BooleanField(default=False)