from django.contrib import admin
from portfolio_web.models import Contact

class ContactMenuAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "content", "date")
    list_filter = ("date",)

admin.site.register(Contact, ContactMenuAdmin)
