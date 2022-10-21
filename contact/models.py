from django.db import models


class Contact(models.Model):
    """ A model to save the contact form to the db """

    first_name = models.CharField(max_length=55,  blank=False, null=True)
    last_name = models.CharField(max_length=55,  blank=False, null=True)
    email = models.EmailField(max_length=254,  blank=False)
    subject = models.CharField(max_length=55, blank=False)
    message = models.TextField(max_length=1000, blank=False)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
