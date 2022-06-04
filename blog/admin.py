from django.contrib import admin
from .models import Post,Knowme
# Register your models here.

class Knowmelist(admin.ModelAdmin):
    list_display = (
        'Your_Name',
        'Your_Email',
        'Your_PH',
        'Your_Address',
        'Your_JobRole',
        'Your_Website',
        'Your_FB',
        'Your_TW',
        'Your_INSTA',
        'Your_GITHUB',
    )
    


class PostOrder(admin.ModelAdmin):
    list_display = (
        'Title',
        'Post_Slug',
        'Created_at'
    )


admin.site.register(Post, PostOrder)
admin.site.register(Knowme,Knowmelist)
