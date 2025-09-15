from django.contrib import admin

# Register your models here.
from comments.models import Comment

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    # add your custom setting here
    pass