from django.db import models


class Enquiry(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    subject = models.CharField(max_length=200)
    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    STATUS_CHOICES = [
        ('new', 'New'),
        ('replied', 'Replied'),
        ('closed', 'Closed'),
    ]

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='new'
    )

    response = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"