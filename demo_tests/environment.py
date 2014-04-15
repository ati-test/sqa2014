#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
import sys
import locale


# wild and dirty hack for windows platform for setting valid locale encoding
if sys.platform in ['win32', 'cygwin']:
    def default_enc(*args, **kwargs):
        return "utf8"
    locale.getpreferredencoding = default_enc

    
def before_all(context):
    context.browser = webdriver.Firefox()
       
def after_all(context):
    try:
        context.browser.close()
        context.browser.quit()
    except Exception:
        pass
