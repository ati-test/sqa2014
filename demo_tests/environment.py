#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver


def before_all(context):
    context.browser = webdriver.Firefox()
    
    
def after_all(context):
    try:
        context.browser.close()
        context.browser.quit()
    except Exception:
        pass
