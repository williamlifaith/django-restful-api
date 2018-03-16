from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class NewsType(models.Model):
    type_name = models.CharField(max_length=15)

    def __str__(self):
        return self.type_name


class News(models.Model):
    title = models.CharField(max_length=50)
    news_type = models.ForeignKey(NewsType, on_delete=models.DO_NOTHING)
    # content = RichTextUploadingField()
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    # read_details = GenericRelation(ReadDetail)
    created_time = models.DateTimeField(auto_now_add=True)
    last_updated_time = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="media/%Y/%m", max_length=100, null=True, blank=True)
    is_top = models.CharField(max_length=50, null=True)

    def __str__(self):
        return "<News: %s>" % self.title

    class Meta:
        ordering = ['-created_time']
