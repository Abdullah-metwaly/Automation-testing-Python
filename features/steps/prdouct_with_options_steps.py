from behave import given, when, then, step, register_type
from selenium.webdriver.support.select import Select
from locaters import locator


@given('The product name is "{parameter}" search button is clicked and the item is picked')
def picking_product(context, parameter):
    context.driver.find_element(*locator["search_input"]).send_keys(parameter)
    context.driver.find_element(*locator["search_button"]).click()
    context.driver.find_element(*locator["product_item"]).click()
    


@step('modify the quantity "{number}"')
def modify_item_counter(context, number):
    context.driver.find_element(*locator["quantity_counter"]).send_keys(number)

@step('choosing the size is "{size}"')
def size_of_item(context, size) :
    select = Select(context.driver.find_element(*locator["size_dropdown"]))
    select.first_selected_option

@step('Color filed is "{color}"')
def pick_color(context, color):
    if color == "White":
        context.driver.find_element(*locator["white_color"]).click()
    else:
        context.driver.find_element(*locator["black_color"]).click()


@when('Add to cart button is clicked')
def add_to_cart(context):
    context.driver.find_element(*locator["add_to_cart"]).click()


@then('process the order')
def process_the_order(context) :
    context.driver.find_element(*locator["process_order"]).click()

# @then('The "{output}" show up')
# def success_adding(context, output) :
#         success_add = context.driver.find_element(*locator["success_heading"])
#         assert success_add == output, f"{output}"