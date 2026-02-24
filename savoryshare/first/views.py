from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomLoginForm
from django.contrib.auth.decorators import login_required
from .models import Recipe, Category  # Make sure Category is imported
from django.shortcuts import get_object_or_404
from django.db.models import Avg
from reportlab.platypus import Table, TableStyle, SimpleDocTemplate,  Paragraph, Spacer # type: ignore
from reportlab.lib import colors  # type: ignore
from django.shortcuts import render
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from .models import Recipe, RecipePayment  # adjust if your model is named differently
from reportlab.lib.styles import getSampleStyleSheet



def search_recipes(request):
    query = request.GET.get('q')
    recipes = Recipe.objects.filter(title__icontains=query) if query else []
    return render(request, 'search_results.html', {
        'recipes': recipes,
        'query': query
    })

from django.db.models import Q

def category_recipes(request, category):
    category_obj = get_object_or_404(Category, name__iexact=category)
    recipes = Recipe.objects.filter(category=category_obj, status='approved')  # Only approved

    # 🔍 Handle search
    query = request.GET.get("q")
    if query:
        recipes = recipes.filter(
            Q(ingredients__icontains=query) | 
            Q(title__icontains=query) |
            Q(instructions__icontains=query)  # only if you have a description field
        )

    return render(request, "category_recipes.html", {
        "recipes": recipes,
        "category": category_obj.name,
    })


def home(request):
    return render(request, 'home.html')


def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully. Please log in.")
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})


def login_view(request):
    form = CustomLoginForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                messages.error(request, "Email not found.")
                return render(request, 'login.html', {'form': form})

            user = authenticate(request, username=user.username, password=password)
            if user is not None:
                login(request, user)
                if user.is_staff:
                    return redirect('admin_dashboard')
                else:
                    return redirect('recipes')
            else:
                messages.error(request, "Invalid password.")

    return render(request, 'login.html', {'form': form})


def recipes_page(request):
    return render(request, 'recipes.html')


def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')

@login_required
def favorites_page(request):
    favorites = Favorite.objects.filter(user=request.user)
    return render(request, 'favorites.html', {'favorites': favorites})

@login_required
def toggle_favorite(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    favorite, created = Favorite.objects.get_or_create(user=request.user, recipe=recipe)
    
    if not created:
        # Already exists, so remove favorite
        favorite.delete()
    
    return redirect('recipe_detail', recipe_id=recipe.id)



# views.py
from django.shortcuts import render, redirect
from .forms import RecipeForm
from .models import Recipe, Favorite

def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.creator = request.user
            recipe.status = 'pending'
            recipe.save()
            messages.success(request, 'Thank you! Your recipe was submitted for review.')
            return redirect('collection')
    else:
        form = RecipeForm()
    return render(request, 'add_recipe.html', {'form': form})


def approved_recipes(request):
    recipes = Recipe.objects.filter(status='approved')
    return render(request, 'approved_recipes.html', {'recipes': recipes})


def favorite_recipe(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    Favorite.objects.get_or_create(user=request.user, recipe=recipe)
    return redirect('approved_recipes')

from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def review_recipes(request):
    pending_recipes = Recipe.objects.filter(status='pending')
    return render(request, 'admin_review.html', {'recipes': pending_recipes})

@staff_member_required
def approve_recipe(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    recipe.status = 'approved'
    recipe.rejection_reason = ''
    recipe.save()
    return redirect('review_recipes')

@staff_member_required
def reject_recipe(request, recipe_id):
    if request.method == 'POST':
        recipe = Recipe.objects.get(id=recipe_id)
        recipe.status = 'rejected'
        recipe.rejection_reason = request.POST.get('reason')
        recipe.save()
    return redirect('review_recipes')

@login_required
def delete_recipe(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id, creator=request.user)
    if request.method == 'POST':
        recipe.delete()
        messages.success(request, "Recipe deleted.")
        return redirect('collection')
    return render(request, 'confirm_delete.html', {'recipe': recipe})




@login_required
def user_collection(request):
    user_recipes = Recipe.objects.filter(creator=request.user)

    context = {
        'pending_recipes': user_recipes.filter(status='pending'),
        'published_recipes': user_recipes.filter(status='approved'),  # approved == published
        'rejected_recipes': user_recipes.filter(status='rejected'),
        'all_recipes': user_recipes,
    }

    return render(request, 'collection.html', context)


# first/views.py
def update_recipe(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.creator = request.user  # Ensure creator is set
            recipe.status = 'pending'  # Reset to pending on update
            recipe.save()
            return redirect('user_collection')
    else:
        form = RecipeForm(instance=recipe)
    return render(request, "recipes/update_recipe.html", {"form": form})

def collections_page(request):
    user_recipes = Recipe.objects.filter(creator=request.user)

    context = {
        'pending_recipes': user_recipes.filter(status='pending'),
        'published_recipes': user_recipes.filter(status='approved'),  # approved == published
        'rejected_recipes': user_recipes.filter(status='rejected'),
        'all_recipes': user_recipes,
    }

    return render(request, 'collection.html', context)




from django.shortcuts import render, get_object_or_404
from .models import Recipe, RecipePayment

from .forms import RatingForm
from .models import RecipeRating

@login_required
def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)

    # Paywall logic
    if recipe.locked:
        paid = RecipePayment.objects.filter(user=request.user, recipe=recipe, paid=True).exists()
        if not paid:
            return render(request, "recipes/paywall.html", {"recipe": recipe})

    # Handle rating submission
    if request.method == "POST":
        form = RatingForm(request.POST)
        if form.is_valid():
            rating_value = form.cleaned_data["rating"]
            RecipeRating.objects.update_or_create(
                recipe=recipe, user=request.user,
                defaults={"rating": rating_value}
            )
            messages.success(request, "Your rating has been submitted.")
            return redirect("recipe_detail", recipe_id=recipe.id)
    else:
        # If user already rated, prefill
        try:
            existing_rating = RecipeRating.objects.get(recipe=recipe, user=request.user)
            form = RatingForm(initial={"rating": existing_rating.rating})
        except RecipeRating.DoesNotExist:
            form = RatingForm()

    # Calculate average rating
    avg_rating = recipe.ratings.aggregate(Avg("rating"))["rating__avg"]

    context = {
        "recipe": recipe,
        "form": form,
        "avg_rating": round(avg_rating, 1) if avg_rating else "No ratings yet",
    }
    return render(request, "recipes/recipe_detail.html", context)


def pay_for_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)

    if request.method == "POST":
        # Fake payment success
        payment, created = RecipePayment.objects.get_or_create(user=request.user, recipe=recipe)
        payment.paid = True
        payment.save()

        # Redirect to thank you page
        return redirect("payment_success", recipe_id=recipe.id)

    return render(request, "recipes/payment.html", {"recipe": recipe})

@login_required
def payment_success(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    return render(request, "recipes/payment_success.html", {"recipe": recipe})

import openpyxl
from django.http import HttpResponse
from .models import Recipe

def download_recipes_excel(request):
    recipes = Recipe.objects.filter(creator=request.user)

    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = "Recipes"

    # Headers
    sheet.append([
        "Title", "Serves", "Cook Time", "Category",
        "Ingredients", "Instructions", "Status", "Rejection Reason"
    ])

    # Data rows
    for recipe in recipes:
        sheet.append([
            recipe.title,
            recipe.serves or "",
            recipe.cook_time or "",
            recipe.category.name if recipe.category else "",
            recipe.ingredients or "",
            recipe.instructions or "",
            recipe.status,
            recipe.rejection_reason or ""
        ])

    # Response
    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    response['Content-Disposition'] = 'attachment; filename="recipes.xlsx"'
    workbook.save(response)
    return response

from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph
from reportlab.lib.units import inch
from reportlab.lib.utils import simpleSplit

def download_recipes(request):
    recipes = Recipe.objects.filter(creator=request.user)

    # Response setup
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="recipes.pdf"'

    p = canvas.Canvas(response, pagesize=letter)
    width, height = letter
    y = height - 50

    p.setFont("Helvetica-Bold", 14)
    p.drawString(50, y, f"{request.user.username}'s Submitted Recipes")
    y -= 30
    p.setFont("Helvetica", 10)

    for recipe in recipes:
        p.drawString(50, y, f"Title: {recipe.title}")
        y -= 15
        if recipe.serves:
            p.drawString(70, y, f"Serves: {recipe.serves}")
            y -= 15
        if recipe.cook_time:
            p.drawString(70, y, f"Cook Time: {recipe.cook_time}")
            y -= 15
        if recipe.category:
            p.drawString(70, y, f"Category: {recipe.category.name}")
            y -= 15

        # ✅ Wrap Ingredients properly
        if recipe.ingredients:
            text_lines = simpleSplit(recipe.ingredients, "Helvetica", 10, width - 100)
            p.drawString(70, y, "Ingredients:")
            y -= 15
            for line in text_lines:
                p.drawString(90, y, line)
                y -= 12

        # ✅ Wrap Instructions properly
        if recipe.instructions:
            text_lines = simpleSplit(recipe.instructions, "Helvetica", 10, width - 100)
            p.drawString(70, y, "Instructions:")
            y -= 15
            for line in text_lines:
                p.drawString(90, y, line)
                y -= 12

        p.drawString(70, y, f"Status: {recipe.status}")
        y -= 15
        if recipe.rejection_reason:
            p.drawString(70, y, f"Reason: {recipe.rejection_reason}")
            y -= 20
        else:
            y -= 10

        # Start new page if space runs out
        if y < 100:
            p.showPage()
            y = height - 50
            p.setFont("Helvetica", 10)

    p.save()
    return response



def download_users_excel(request):
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = "Users"

    sheet.append(["ID", "Username", "Email", "Password", "Date Joined"])

    users = User.objects.all()
    for user in users:
        sheet.append([user.id, user.username, user.email, user.password,  user.date_joined.strftime("%Y-%m-%d")])

    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    response["Content-Disposition"] = 'attachment; filename="users.xlsx"'
    workbook.save(response)
    return response

from django.http import HttpResponse
from reportlab.lib.pagesizes import A4
from .models import Recipe


def download_recipes_pdf(request):
    # Setup response
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = 'attachment; filename="recipes_report.pdf"'

    # Create PDF document
    doc = SimpleDocTemplate(
        response,
        pagesize=A4,
        rightMargin=30, leftMargin=30,
        topMargin=30, bottomMargin=30,
    )

    styles = getSampleStyleSheet()
    elements = []

    # Title
    elements.append(Paragraph("🍴 Savory Share - Recipes Report", styles["Title"]))
    elements.append(Spacer(1, 12))

    # Table data (header + rows)
    data = [["ID", "Title", "Category",  "Creator"]]

    recipes = Recipe.objects.select_related("creator").all()
    if recipes.exists():
        for recipe in recipes:
            data.append([
                recipe.id,
                recipe.title,
                recipe.category,
                recipe.creator.username if recipe.creator else "Anonymous",
                
            ])
    else:
        data.append(["-", "No recipes available", "-", "-"])

    # Create table
    table = Table(data, colWidths=[50, 200, 120, 100])
    table.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), colors.HexColor("#007BFF")),
        ("TEXTCOLOR", (0,0), (-1,0), colors.white),
        ("ALIGN", (0,0), (-1,-1), "CENTER"),
        ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
        ("BOTTOMPADDING", (0,0), (-1,0), 12),

        ("BACKGROUND", (0,1), (-1,-1), colors.whitesmoke),
        ("GRID", (0,0), (-1,-1), 1, colors.grey),
    ]))

    elements.append(table)

    # Build PDF
    doc.build(elements)
    return response


