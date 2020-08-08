from django.contrib import admin

from .models import Post,Comments

class PostAdmin(admin.ModelAdmin):
    list_display = ['title','slug','auther','body','publish','created','updated','status']
    list_filter = ('status','auther')
    search_fields = ('title','body')
    raw_id_fields = ('auther',)
    date_hierarchy = 'publish'
    prepopulated_fields = {'slug':('title',)}

class CommentsAdmin(admin.ModelAdmin):
    list_display = ['name','email','post','body','created','updated','active']
    list_filter = ('active','created','updated')
    search_fields = ('name','email','body')

admin.site.register(Post,PostAdmin)
admin.site.register(Comments,CommentsAdmin)
