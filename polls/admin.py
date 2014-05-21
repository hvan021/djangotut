from django.contrib import admin
from polls.models import Poll, Choice

# Register your models here.

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 5

class PollAdmin(admin.ModelAdmin):
    #fields = ['pub_date', 'question']
    fieldsets = [
        (None,               {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines =  [ChoiceInline]

admin.site.register(Poll, PollAdmin)


