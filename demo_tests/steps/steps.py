#!/usr/bin/env python
# -*- coding: utf-8 -*-

from behave import step, given, when, then

#шаги для теста switch_language.feature

@when('зайти на сайт {url}')
def open_url(context, url):
    context.browser.get(url)
    

@when('нажать на ссылку {link_text}')
def link_click(context, link_text):
    link = context.browser.find_element_by_link_text(link_text)
    assert link, 'ссылка ' + link_text + ' не найдена'
    link.click()
    

@then('на странице будет текст "{text}"')
def find_text(context, text):
    page = context.browser.find_element_by_css_selector('body')
    page_text = page.text
    assert text in page_text, 'на странице не найден текст: ' + text
    
# шаги для теста partners.feature
    
@step('нажать на {banner_id} партнера')
def assert_page_name(context, banner_id):
    banner = context.browser.find_element_by_css_selector('img[alt="{}"]'.format(banner_id))
    assert banner, "баннер не найден"
    banner.click()
    
    
@step('в соседнем окне откроется {site_url}')
def assert_page_name(context, site_url):
    try:
        _windows_list = context.browser.window_handles
        _root_window = context.browser.current_window_handle
        try:
            _windows_list.remove(_root_window)
            window2switch = _windows_list.pop()
            context.browser.switch_to_window(window2switch)
        except Exception:
            raise Exception("Failed to switch to popup ")
    except Exception as e:
        pass
    url = context.browser.current_url
    assert url == site_url, url + ' не совпадает с ожидаемым ' + site_url
    context.browser.close()
    context.browser.switch_to_window(_root_window)