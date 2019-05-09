from django.db import models
from roomswap.settings import HOSTEL_CHOICES

class room(models.Model):
    hostel = models.TextField(choices=HOSTEL_CHOICES)
    room_no = models.CharField(max_length=8)
    desire = models.TextField(verbose_name='Enter the Room details you desire')
    contact = models.TextField(verbose_name="Enter your Email_id or Phone no")
    codeword = models.CharField(max_length=10, null=True, blank=True)
    status = models.BooleanField(default=True)

    class Meta:
        unique_together = (("hostel", "room_no"),)
