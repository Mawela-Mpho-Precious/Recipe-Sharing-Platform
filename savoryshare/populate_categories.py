# populate_categories.py

import os
import django

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "savoryshare.settings")
django.setup()

# Now we can safely import models
from first.models import Category

# Define your default categories
categories = ['Dessert', 'Lunch', 'Vegan', 'Dinner', 'Breakfast', 'Bakery']

# Populate the database
for name in categories:
    Category.objects.get_or_create(name=name)


