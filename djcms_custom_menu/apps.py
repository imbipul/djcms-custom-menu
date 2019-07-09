# -*- coding: utf-8 -*-
from django.apps import AppConfig


class DJCMSCustomMenuConfig(AppConfig):
    name = 'djcms_custom_menu'
    verbose_name = 'Django CMS Custom Menu'

    def ready(self):
        import djcms_custom_menu.signals

