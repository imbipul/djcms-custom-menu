# -*- coding: utf-8 -*-
'''
Created on Jan 30, 2017

@author: jakob
'''
from django.conf import settings

CACHE_DURATION = getattr(settings, 'DJCMS_CUSTOM_MENU_CACHE_DURATION', 0)
ALLOWED_NAMESPACES = getattr(settings, 'DJCMS_CUSTOM_MENU_NAMESPACES', ['CMSMenu','DJCMSCustomMenu',])
