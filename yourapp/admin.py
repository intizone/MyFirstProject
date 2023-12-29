from django.contrib import admin
from .models import Portfolio, Message

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('sort', 'title',)
    search_fields = ('title',)

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message',)
    search_fields = ('name', 'email',)
    list_filter = ('name', 'email',)
    ordering = ('id',)
    list_per_page = 20

    fieldsets = (
        ('Personal Information', {
            'fields': ('name', 'email',)
        }),
        ('Message', {
            'fields': ('message',)
        }),
    )

    readonly_fields = ('email',)
