from django import template
from django.urls import resolve, Resolver404, reverse
from ..utils import build_menu_tree

register = template.Library()

@register.inclusion_tag('menu/menu_template.html', takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    current_path = request.path_info
    
    try:
        resolved = resolve(current_path)
        current_path = reverse(resolved.url_name, args=resolved.args, kwargs=resolved.kwargs)
    except Resolver404:
        pass
    
    menu_tree = build_menu_tree(menu_name, current_path)
    return {
        'menu_tree': menu_tree,
        'menu_name': menu_name,
        'request': request,
    }