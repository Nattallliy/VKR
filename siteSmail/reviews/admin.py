from django.contrib import admin

from .models import Reviews, Applications, Mails

admin.site.register(Reviews)
admin.site.register(Applications)
admin.site.register(Mails)