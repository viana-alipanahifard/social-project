from django.contrib import admin
from .models import Post
from .models import Comment,Vote



class PostAdmin(admin.ModelAdmin):
    list_display=('user','slug','update')
admin.site.register(Post,PostAdmin)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
	list_display = ('user', 'post', 'created', 'is_reply')
	raw_id_fields = ('user', 'post', 'reply')

admin.site.register(Vote)