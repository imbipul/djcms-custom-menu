import json
from pprint import pprint

from django.utils.functional import Promise
from django.utils.encoding import force_text

from django.contrib.sites.shortcuts import get_current_site
from django.conf import settings
from django.contrib import admin

from djcms_custom_menu.models import DJCMSCustomMenu
from djcms_custom_menu.nodes import get_nodes
from djcms_custom_menu.settings import ALLOWED_NAMESPACES

class LazyEncoder(json.JSONEncoder):
    """Encodes django's lazy i18n strings.
        Used to serialize translated strings to JSON, because
        simplejson chokes on it otherwise. """

    def default(self, obj):
        if isinstance(obj, Promise):
            return force_text(obj)
        return obj


class SimpleNode(object):
    id = None
    title = None
    url = None
    children = []

    def __init__(self, node):
        self.id = node.id
        self.title = node.title
        self.url = node.url


class DJCMSCustomMenuAdmin(admin.ModelAdmin):
    change_form_template = 'djcms_custom_menu/change_form.html'

    readonly_fields = ('site',)

    list_display = ('name', 'slug', 'site')

    def get_queryset(self, request):
        qs = super(DJCMSCustomMenuAdmin, self).get_queryset(request)
        current_site = get_current_site(request)
        return qs.filter(site=current_site)

    def add_view(self, request, form_url='', extra_context=None):
        if extra_context is None:
            extra_context = {}
        nodes, menu_renderer = get_nodes(request)
        available_pages = self.serialize_navigation(nodes)
        menu_pages = None
        extra_context = {
            'menu_pages': menu_pages,
            'available_pages': available_pages,
            'available_pages_json': json.dumps(available_pages, cls=LazyEncoder),
            'debug': settings.DEBUG,
        }
        return super(DJCMSCustomMenuAdmin, self).add_view(request, form_url, extra_context)

    def change_view(self, request, object_id, form_url='', extra_context=None):
        if extra_context is None:
            extra_context = {}
        nodes, menu_renderer = get_nodes(request)
        available_pages = self.serialize_navigation(nodes)
        menu_pages = DJCMSCustomMenu.objects.get(id=object_id).pages
        extra_context = {
            'menu_pages': menu_pages,
            'available_pages': available_pages,
            'available_pages_json': json.dumps(available_pages, cls=LazyEncoder),
            'debug': settings.DEBUG,
        }
        return super(DJCMSCustomMenuAdmin, self).change_view(request, object_id, form_url, extra_context)

    def serialize_navigation(self, all_nodes):
        # Recursively convert nodes to simple nodes
        cleaned = []
        for node in all_nodes:
            if not node.parent_id:
                cleaned_node = self.get_cleaned_node([node])
                if cleaned_node:
                    cleaned += cleaned_node

        return cleaned

    def get_cleaned_node(self, nodes):
        # Clean node to be a simple title/id/children class
        cleaned_nodes = []
        for node in nodes:
            # Limit the namespaces, typically to CMS Page only, can be set to None to ignore this
            if ALLOWED_NAMESPACES and node.namespace not in ALLOWED_NAMESPACES:
                continue
            cleaned_node = SimpleNode(node)
            if node.children:
                child_nodes = self.get_cleaned_node(node.children)
                if child_nodes:
                    cleaned_node.children = child_nodes
            cleaned_nodes.append(cleaned_node.__dict__)

        return cleaned_nodes # json.dumps(cleaned_nodes, cls=LazyEncoder)


admin.site.register(DJCMSCustomMenu, DJCMSCustomMenuAdmin)
