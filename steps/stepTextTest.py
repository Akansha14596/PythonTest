import os;
from behave import given, then;
from selenium import webdriver;
from selenium.webdriver.common.by import By

@given('the user open "{pageName}" page')
def step_open_htmlpage(context, pageName):
  dir = os.getcwd()
  context.browser = webdriver.Chrome()
  context.browser.get(f'file://{dir}/{pageName}')

@then('the "{text}" text should be displayed on the page')
def step_text_shouldDisplayed(context,text):

    body_text = context.browser.find_element(By.TAG_NAME, 'body').text
    assert text in body_text

@then('close browser')
def step_close_browser(context):
    context.browser.quit()
	