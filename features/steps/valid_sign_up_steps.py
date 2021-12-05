import parse
from behave import given, when, then,register_type
from selenium.webdriver.support.select import Select
from locaters import locator


# To enable eampty rows
@parse.with_pattern(r'.*')
def parse_nullable_string(text):
    return text


register_type(NullableString=parse_nullable_string)

@given('email "{email}"')
def insert_email(context, email):
    context.driver.find_element(*locator["sign_up_email"]).send_keys(email)


@when('account button is clicked')
def create_account(context):
    context.driver.find_element(*locator["create_account_button"]).click()
    assert context.driver.title == "Login - My Store"


@when('user wants to create a record with "{gender}" as gender')
def choose_gender(context, gender):
    if gender == "Mr.":
        context.driver.find_element(*locator["gender_radiobutton_mr"]).click()
    else:
        context.driver.find_element(*locator["gender_radiobutton_mrs"]).click()


@when('user record has a first name of "{fname}" same as address')
def firstname(context, fname):
    context.driver.find_element(*locator["firstname"]).send_keys(fname)


@when('user record has a last name of "{lname}" same as address')
def lastname(context, lname):
    context.driver.find_element(*locator["lastname"]).send_keys(lname)


@when('Password "{pwd}"')
def make_password(context, pwd):
    context.driver.find_element(*locator["sign_up_password"]).send_keys(pwd)


@when('Date of birth "{dof}"')
def date_of_birth(context, dof):
    day = dof[0]
    month = dof[2:4]
    year = dof[5:]

    select = Select(context.driver.find_element(*locator["days_dropdown"]))
    select.select_by_value(day)

    select = Select(context.driver.find_element(*locator["months_dropdown"]))
    select.select_by_value(month)

    select = Select(context.driver.find_element(*locator["years_dropdown"]))
    select.select_by_value(year)



@when('Address is "{loc}"')
def addr(context, loc):
    context.driver.find_element(*locator["sign_up_address"]).send_keys(loc)


@when('City "{city}"')
def choose_city(context, city):
    context.driver.find_element(*locator["city"]).send_keys(city)


@when('State "{state}"')
def choose_state(context, state):
    print("This is State ------>", state)

    select = Select(context.driver.find_element(*locator["state_dropdown"]))
    select.select_by_visible_text(state)


@when('zip code "{zip_code}"')
def zip_code(context, zip_code):
    context.driver.find_element(*locator["postcode"]).send_keys(zip_code)



@when('Mobile num is "{num}"')
def mobile_num(context, num):
    context.driver.find_element(*locator["mobile"]).send_keys(num)



@then('User must successfully create and account with "{acc}" as account')
def final_step(context, acc):
    context.driver.find_element(*locator["register_button"]).click()
    assert context.driver.title == "My account - My Store"
    acc_name = context.driver.find_element(*locator["account_name"]).text
    if acc == acc_name:
        assert True, f"This is indeed {acc}"