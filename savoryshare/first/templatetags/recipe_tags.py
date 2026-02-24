from django import template
from ..models import Favorite

register = template.Library()

@register.filter
def is_favorite(recipe, user):
    return Favorite.objects.filter(user=user, recipe=recipe).exists()
