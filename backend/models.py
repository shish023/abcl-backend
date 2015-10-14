from django.db import models

class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey('User')
    content = models.TextField(blank=False)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']

    def __unicode__(self):
        return self.content

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=120,unique=True,blank=False)
    email = models.EmailField()
    password = models.CharField(max_length=30,blank=False)

    def __unicode__(self):
        return self.username

class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey('User')
    post_id = models.ForeignKey('Post')
    content = models.TextField(blank=False)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date']

    def __unicode__(self):
        return self.content

class Support(models.Model):
    post_id = models.ForeignKey('Post')
    user_id = models.ForeignKey('User')

    class Meta:
        unique_together = ('post_id', 'user_id')

    def __unicode__(self):
        return str(self.post_id)