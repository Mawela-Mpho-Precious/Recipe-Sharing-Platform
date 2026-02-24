from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),  # Only one login route
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('recipes/', views.recipes_page, name='recipes'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('category/<str:category>/', views.category_recipes, name='category_recipes'),
    path('search/', views.search_recipes, name='search_recipes'),
    path('collection/', views.user_collection, name='collection'),
    path('favorites/<int:recipe_id>/', views.favorite_recipe, name='favorite_recipe'),
    path('admin/review/', views.review_recipes, name='review_recipes'),
    path('admin/approve/<int:recipe_id>/', views.approve_recipe, name='approve_recipe'),
    path('admin/reject/<int:recipe_id>/', views.reject_recipe, name='reject_recipe'),
    path('approved/', views.approved_recipes, name='approved_recipes'),
    path('recipes/<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),
    path('recipes/favorites/', views.favorites_page, name='favorites'),
    path('recipes/collections/', views.collections_page, name='collections'),
    path('add_recipe/', views.add_recipe, name='add_recipe'),
    path('recipe/edit/<int:recipe_id>/', views.update_recipe, name='edit_recipe'),
    path('recipe/delete/<int:recipe_id>/', views.delete_recipe, name='delete_recipe'),
    path('recipe/<int:recipe_id>/pay/', views.pay_for_recipe, name='pay_for_recipe'),
    path('recipe/<int:recipe_id>/favorite/', views.toggle_favorite, name='toggle_favorite'),
    path('favorites/', views.favorites_page, name='favorites_page'),
    path('recipe/<int:recipe_id>/success/', views.payment_success, name='payment_success'),
    path("collection/", views.user_collection, name="user_collection"),
    path('download/pdf/', views.download_recipes, name='download_recipes'),
    path('download/excel/', views.download_recipes_excel, name='download_recipes_excel'),
    path("download-users-excel/", views.download_users_excel, name="download_users_excel"),
    path("download-recipes-pdf/", views.download_recipes_pdf, name="download_recipes_pdf"),

   


    
   
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    




