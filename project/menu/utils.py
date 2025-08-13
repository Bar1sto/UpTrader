from django.core.cache import cache
from .models import MenuItem


def build_menu_tree(menu_name, current_path):
    cache_key = f'menu_{menu_name}_{current_path}'
    cached_menu = cache.get(cache_key)
    
    if cached_menu:
        return cached_menu
    
    menu_items = MenuItem.objects.filter(menu_name=menu_name).select_related('parent')
    
    items_dict = {item.id: item for item in menu_items}
    
    for item in menu_items:
        if item.parent_id and item.parent_id == item.id:
            item.parent_id = None
            item.save()
    
    root_items = []
    for item in menu_items:
        if item.parent_id:
            parent = items_dict.get(item.parent_id)
            if parent and parent.id != item.id:  
                if not hasattr(parent, 'children_list'):
                    parent.children_list = []
                parent.children_list.append(item)
        else:
            root_items.append(item)
    
    active_items = set()
    for item in menu_items:
        if item.is_active(current_path):
            active_items.add(item.id)
            parent = item.parent
            while parent:
                if parent.id in active_items:
                    break
                active_items.add(parent.id)
                parent = parent.parent
    
    def process_item(item):
        children_data = []
        if hasattr(item, 'children_list'):
            for child in item.children_list:
                if child.id != item.id:
                    children_data.append(process_item(child))
        
        return {
            'item': item,
            'children': children_data,
            'is_active': item.id in active_items,
            'has_active_child': any(
                child.id in active_items or child_data['has_active_child']
                for child, child_data in zip(
                    getattr(item, 'children_list', []),
                    children_data
                )
            ) if hasattr(item, 'children_list') else False
        }
    
    menu_tree = [process_item(item) for item in root_items]
    
    cache.set(cache_key, menu_tree, 3600)
    return menu_tree