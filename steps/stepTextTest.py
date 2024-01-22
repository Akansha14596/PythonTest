import os;
from behave import given, then;
from selenium import webdriver;
from selenium.webdriver.common.by import By

@given('the user open "{pageName}" page')
def step_open_htmlpage(context, pageName):
  dir = os.getcwd()
  context.browser = webdriver.Chrome()
  context.browser.get(f'file://{dir}/{pageName}')

@when('I check if the HTML page contains the string "{string_value}"')
def step_fetch_array(context, string_value):
  body_text = context.browser.find_element(By.ID, 'index_body').text
  context.stringIsPresent = string_value in body_text

@then('the result should be "{expected_result}"')
def step_text_shouldDisplayed(context, expected_result):
     if expected_result == 'Present':
        assert context.stringIsPresent
     elif expected_result == 'NotPresent':
        assert not context.stringIsPresent
    
@then('close browser')
def step_close_browser(context):
    context.browser.quit()
	