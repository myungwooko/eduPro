from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'phone', 'username', 'is_staff', 'is_active')
    search_fields = ('email', 'phone')

    def get_ordering(self, request):
        return ['email']


