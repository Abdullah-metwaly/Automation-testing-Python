import random
import parse
from behave import given, when, then, step, register_type
from selenium.webdriver.support.select import Select
import sys

import os
dir_path = os.path.dirname(os.path.realpath(__file__))

sys.path.append(dir_path)

from locaters import locator


# To enable eampty rows
@parse.with_pattern(r'.*')
def parse_nullable_string(text):
    return text


register_type(NullableString=parse_nullable_string)


@given('The Sign In link is clicked')
def click_signin_link(context):
    assert context.driver.find_element(*locator["sign_in_link"]).is_displayed()
    context.driver.find_element(*locator["sign_in_link"]).click()
    assert context.driver.title == "Login - My Store"


@given('Enter email "{email}"')
def enter_email(context, email):
    context.driver.find_element(*locator["sign_up_email"]).send_keys(str(random.randint(0, 1000000)) + email)


@when('Create an account button is clicked')
def click_create_account(context):
    context.driver.find_element(*locator["create_account_button"]).click()
    assert context.driver.title == "Login - My Store"


@when('Chosen filed is "{gender}" as gender')
def pick_gender(context, gender):
    if gender == "Mr.":
        context.driver.find_element(*locator["gender_radiobutton_mr"]).click()
    else:
        context.driver.find_element(*locator["gender_radiobutton_mrs"]).click()


@when('first name of the user is "{fname:NullableString}"')
def first_name(context, fname):
    context.driver.find_element(*locator["firstname"]).send_keys(fname)


@when('last name of the user is "{lname:NullableString}"')
def last_name(context, lname):
    context.driver.find_element(*locator["lastname"]).send_keys(lname)


@when('Password is "{pwd:NullableString}"')
def create_password(context, pwd):
    context.driver.find_element(*locator["sign_up_password"]).send_keys(pwd)


@when('Date of Birth is "{dof}"')
def dof(context, dof):
    day = dof[0]
    month = dof[2:4]
    year = dof[5:]

    select = Select(context.driver.find_element(*locator["days_dropdown"]))
    select.select_by_value(day)

    select = Select(context.driver.find_element(*locator["months_dropdown"]))
    select.select_by_value(month)

    select = Select(context.driver.find_element(*locator["years_dropdown"]))
    select.select_by_value(year)


@when('the Address is "{address}"')
def address(context, address):
    context.driver.find_element(*locator["sign_up_address"]).send_keys(address)


@when('the City is "{city:NullableString}"')
def pick_city(context, city):
    context.driver.find_element(*locator["city"]).send_keys(city)


@when('the State is "{state:NullableString}"')
def pick_state(context, state):
    print("This is State ------>", state)

    select = Select(context.driver.find_element(*locator["state_dropdown"]))
    select.select_by_visible_text(state)


@when('zip code is "{zipcode:NullableString}"')
def write_zip_code(context, zipcode):
    context.driver.find_element(*locator["postcode"]).send_keys(zipcode)


@when('Country is set to default which is United States')
def step_impl(context):
    assert True, "No need to change country"


@when('Mobile Phone is "{mobile}"')
def pick_mobile_num(context, mobile):
    context.driver.find_element(*locator["mobile"]).send_keys(mobile)


@when('Address ref. is default: My Address')
def addr_impl(context):
    assert True, "No need to change Address Reference"


@then('the "{output}" is shown.')
def step_impl(context, output):
        context.driver.find_element(*locator["register_button"]).click()
        fail_signup = context.driver.find_element(*locator["error_fial_msg"]).text
        assert fail_signup == output, f"{output}"

