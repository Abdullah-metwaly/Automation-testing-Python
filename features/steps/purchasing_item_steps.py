import parse
from behave import given, when, then, step, register_type
from selenium.webdriver.support.select import Select
from locaters import locator


# To enable eampty rows
@parse.with_pattern(r'.*')
def parse_nullable_string(text):
    return text


register_type(NullableString=parse_nullable_string)

@given('The search input is filled with "{parameter:NullableString}"')
def searching_products(context, parameter):
    context.driver.find_element(*locator["search_input"]).send_keys(parameter)

@step('The button for search is clicked')
def search_clicking(context):
    # context.driver.find_element(*locator["item_in_image"]).click()
    context.driver.find_element(*locator["search_button"]).click()
    

@step('The product item button is clicked')
def clicking_prodcut_item(context):
    context.driver.find_element(*locator["product_item"]).click()

@step('The plus button is clicked')
def increasing_item(context):
    context.driver.find_element(*locator["plus_button"]).click()

@when('The add to cart button is clicked')
def adding_item_to_cart(context):
    context.driver.find_element(*locator["add_to_cart"]).click()


@then('The item count changes to "{number}"')
def quantity_counter(context, number) :
    assert context.driver.find_element(*locator["quantity_counter"]).text != str(number), "assertion failed"

