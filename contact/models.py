""" Models found in the contact app """
from django.db import models


class Contact(models.Model):
    """ Model storing the contact form """
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20)
    message = models.TextField()
    sent_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        Meta class specifying how messages should be ordered.
        Also changes verbose name from Contacts to Messages.
        """
        verbose_name_plural = 'Messages'
        ordering = ['-sent_on']

    def __str__(self):
        return f"{self.full_name} on {self.sent_on}"
