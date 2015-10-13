from django.db import models


class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey('User')
    content = models.TextField(blank=False)
    date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.content


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=120, unique=True, blank=False)
    password = models.CharField(max_length=128, blank=False)
    email = models.EmailField()

    def __unicode__(self):
        return self.username


class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey('User')
    post_id = models.ForeignKey('Post')
    content = models.TextField(blank=False)
    date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.content


class Support(models.Model):
    post_id = models.ForeignKey('Post')
    user_id = models.ForeignKey('User')

    def __unicode__(self):
        return str(self.post_id)