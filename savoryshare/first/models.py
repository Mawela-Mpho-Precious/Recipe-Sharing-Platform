from django.db import models
from django.contrib.auth.models import User

# ----------------------
# Category Model
# ----------------------
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


# ----------------------
# Recipe Model
# ----------------------
class Recipe(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    )

    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='recipes/', null=True, blank=True)
    serves = models.CharField(max_length=50, null=True, blank=True)
    cook_time = models.CharField(max_length=50, null=True, blank=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    ingredients = models.TextField(null=True, blank=True)
    instructions = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    locked = models.BooleanField(default=False)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    rejection_reason = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']

    



# ----------------------
# Favorite Model
# ----------------------
class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} likes {self.recipe.title}"
    
class RecipePayment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    paid = models.BooleanField(default=False)
    amount = models.DecimalField(max_digits=6, decimal_places=2, default=150.00)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'recipe')

from django.db import models
from django.contrib.auth.models import User

class RecipeRating(models.Model):
    recipe = models.ForeignKey(
        "Recipe", on_delete=models.CASCADE, related_name="ratings"
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)  # ✅ auto timestamp
    updated_at = models.DateTimeField(auto_now=True)      # ✅ auto update timestamp

    class Meta:
        unique_together = ("recipe", "user")  # prevents duplicate ratings










# Create your models here.
