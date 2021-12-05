import parse
from behave import given, when, then, step, register_type
from selenium.webdriver.support.select import Select
from locaters import locator

# To enable eampty rows
@parse.with_pattern(r'.*')
def parse_nullable_string(text):
    return text


register_type(NullableString=parse_nullable_string)



@given('The search field is filled with "{parameter:NullableString}"')
def open_website(context, parameter):
    context.driver.find_element(*locator["search_input"]).send_keys(parameter)

@when('The search button is clicked')
def search_impl(context):
    context.driver.find_element(*locator["search_button"]).click()
    


@then('The "{msg}" search error message is shown')
def result_msg(context, msg):
    fail_search = context.driver.find_element(*locator["search_erro_msg"]).text
    assert fail_search == msg, f"{msg}"