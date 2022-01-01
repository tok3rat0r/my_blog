from django.db import models
from django.core.validators import RegexValidator
from django.utils.text import slugify

# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email_address = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Tag(models.Model):
    tag = models.CharField(
        primary_key=True,
        max_length=30,
        validators=[RegexValidator(
            regex=r'^\w+$',
            message="Invalid tag. Only alphanumeric characters and underscores allowed."
        )]
    )

    def __str__(self):
        return f"#{self.tag}"


class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    excerpt = models.CharField(max_length=240)
    image = models.ImageField(upload_to='images', null=True)
    date = models.DateField(auto_now_add=True)
    slug = models.SlugField(max_length=100, editable=False)
    content = models.TextField()
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return f"{self.title}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
