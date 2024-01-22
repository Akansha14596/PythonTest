import os;
from behave import given, then;
from selenium import webdriver;
from selenium.webdriver.common.by import By

@given('the user open "{pageName}" page')
def step_open_htmlpage(context, pageName):
  dir = os.getcwd()
  context.browser = webdriver.Chrome()
  print("Hello from html")
  context.browser.get(f'file://{dir}/{pageName}')

@given("I have the following items in an array")
def step_fetch_array(context):
  print(context.text);
  context.item_list = context.text.split(',')
  print("hello world")

@then('the array should be displayed on the page')
def step_text_shouldDisplayed(context):
    body_text0 = context.browser.find_element(By.ID, 'id0').text
    assert context.item_list[0] in body_text0
    body_text1 = context.browser.find_element(By.ID, 'id1').text
    assert context.item_list[1] in body_text1
    body_text2 = context.browser.find_element(By.ID, 'id2').text
    assert context.item_list[2] in body_text2

@then('the "{text}" should not be displayed on the page')
def step_text_shouldDisplayed(context,text):
    body_text = context.browser.find_element(By.TAG_NAME, 'body').text
    context.text_notPresent = text not in body_text
    print(context.text_notPresent)
    assert context.text_notPresent is True
	
@then('close browser')
def step_close_browser(context):
    context.browser.quit()
	