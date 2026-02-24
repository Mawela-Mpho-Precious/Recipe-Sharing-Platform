# C:\Users\Admin\Documents\Sign\savoryshare\first\templatetags\first_filters.py

from django import template

register = template.Library()

@register.filter(name='add_attr')
def add_attr(field, css_class):
    """
    Add a CSS class or other attribute to a field.
    Example usage: {{ field|add_attr:'{"class": "my-class", "placeholder": "Enter value"}' }}
    The attribute_dict should be a JSON-like string.
    """
    try:
        # Safely parse the JSON-like string into a dictionary
        import json
        attrs = json.loads(css_class)
    except json.JSONDecodeError:
        # Fallback if it's not valid JSON, perhaps just a class string
        attrs = {'class': css_class} # Default to just a class

    # Ensure the field has a widget
    if not hasattr(field, 'field') or not hasattr(field.field, 'widget'):
        return field

    # Update widget attributes
    existing_attrs = field.field.widget.attrs
    updated_attrs = existing_attrs.copy()
    updated_attrs.update(attrs)

    # Return a new BoundField with the updated widget
    from django.forms.boundfield import BoundField
    from django.forms.widgets import Widget

    # For forms.widgets.Widget (most common)
    if isinstance(field.field.widget, Widget):
        field.field.widget.attrs = updated_attrs
        return field
    # If it's a more complex widget, we might need a different approach,
    # but for simple inputs, this covers it.

    return field # Return original if unable to modify