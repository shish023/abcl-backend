from django.contrib import admin

# Register your models here.
from .models import User
from .models import Post
from .models import Comment
from .models import Support
from .forms import UserForm


class UserAdmin(admin.ModelAdmin):
    list_display = ["__unicode__", "email", "user_id"]
    form = UserForm


class PostAdmin(admin.ModelAdmin):
    list_display = ["__unicode__", "post_id", "user_id", "date"]

    class Meta:
        model = Post


class CommentAdmin(admin.ModelAdmin):
    list_display = ["__unicode__", "comment_id", "post_id", "user_id"]

    class Meta:
        model = Comment


class SupportAdmin(admin.ModelAdmin):
    list_display = ["__unicode__", "user_id"]

    class Meta:
        model = Support

admin.site.register(User, UserAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Support, SupportAdmin)