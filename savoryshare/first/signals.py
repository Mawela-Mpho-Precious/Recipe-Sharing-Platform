# users/signals.py (create this file in your app)
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.shortcuts import redirect
from django.urls import reverse

@receiver(user_logged_in)
def redirect_after_login(sender, request, user, **kwargs):
    if user.is_staff:
        # Redirect admins to their dashboard
        return redirect(reverse('admin_dashboard')) # Use reverse for immediate redirect
    else:
        # For regular users, let Django's default LOGIN_REDIRECT_URL or 'next' handle it
        pass # No explicit redirect needed here, as the view will handle it.

# In your_app/apps.py:
# class YourAppConfig(AppConfig):
#     name = 'your_app_name'
#     def ready(self):
#         import your_app_name.signals # Connect signals here