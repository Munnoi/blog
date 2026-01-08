from django.db import models
from django.db import models
from django.conf import settings
from django.utils.text import slugify


class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="posts"
    )

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    content = models.TextField()

    is_published = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug: # Only generate a slug if it doesn't already exist
            base_slug = slugify(self.title) # Converts the title into a URL-friendly string
            slug = base_slug
            counter = 1 # This number will be appended if duplicates exist

            while Post.objects.filter(slug=slug).exists(): # Checks if any post already have this slug
                slug = f"{base_slug}-{counter}"
                counter += 1

            self.slug = slug # Assigns the final unique slug to the post
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
