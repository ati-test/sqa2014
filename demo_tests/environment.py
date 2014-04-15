#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
import sys
import locale

def before_all(context):
    context.browser = webdriver.Firefox()
    
    
def after_all(context):
    try:
        context.browser.close()
        context.browser.quit()
    except Exception:
        pass


# wild and dirty hack for windows platform for setting valid locale encoding
if sys.platform in ['win32', 'cygwin']:
    # override builtin method which returns default encoding used for opening
    # files
    def default_enc(*args, **kwargs):
        return "utf8"
    locale.getpreferredencoding = default_enc
