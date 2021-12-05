from selenium.webdriver.common.by import By

locator = {
    "sign_in_link": (By.XPATH, '//*[@id="header"]/div[2]/div/div/nav/div[1]/a'),
    "sign_in_email": (By.ID, "email"),
    "sign_in_pass": (By.ID, "passwd"),
    "sign_in_button": (By.ID, "SubmitLogin"),
    "my_account": (By.XPATH, '//*[@id="center_column"]/h1'),
    "error_msg": (By.XPATH, '//*[@id="center_column"]/div[1]/ol/li'),
    "sign_up_email": (By.ID, "email_create"),
    "account_name": (By.XPATH, '//*[@id="header"]/div[2]/div/div/nav/div[1]/a/span'),
    "create_account_button": (By.ID, "SubmitCreate"),
    "gender_radiobutton_mr": (By.ID, "id_gender1"),
    "gender_radiobutton_mrs": (By.ID, "id_gender2"),
    "firstname": (By.ID, "customer_firstname"),
    "lastname": (By.ID, "customer_lastname"),
    "sign_up_password": (By.ID, "passwd"),
    "days_dropdown": (By.ID, "days"),
    "months_dropdown": (By.ID, "months"),
    "years_dropdown": (By.ID, "years"),
    "newsletter_checkbox": (By.ID, "newsletter"),
    "optin_checkbox": (By.ID, "optin"),
    "sign_up_address": (By.ID, "address1"),
    "city": (By.ID, "city"),
    "state_dropdown": (By.ID, "id_state"),
    "postcode": (By.ID, "postcode"),
    "mobile": (By.ID, "phone_mobile"),
    "register_button": (By.ID, "submitAccount"),
    "contact_us": (By.XPATH, "//*[@id='contact-link']/a"),
    "subject_heading": (By.ID, "id_contact"),
    "contact_email": (By.ID, "email"),
    "contact_message": (By.ID, "message"),
    "attach_file_button": (By.ID, "fileUpload"),
    "submit_message_contact": (By.ID, "submitMessage"),
    "succ_contact_msg": (By.XPATH, '//*[@id="center_column"]/p'),
    "fail_contact_msg": (By.XPATH, '//*[@id="center_column"]/div/ol/li'),    
    "casual_printed_dress": (By.XPATH, '//*[@id="center_column"]/ul/li/div/div[2]/h5/a'),
    "evening_printed_dress": (By.XPATH, '//*[@id="center_column"]/ul/li/div/div[2]/h5/a'),
    "error_fial_msg" : (By.XPATH, '//*[@id="center_column"]/div/ol/li'),
    "search_button" : (By.XPATH, '//*[@id="searchbox"]/button'),
    "search_input" : (By.XPATH, '//*[@id="search_query_top"]'),
    "search_erro_msg" : (By.XPATH, '//*[@id="center_column"]/p'),
    "add_to_cart" : (By.XPATH, '//*[@id="add_to_cart"]'),
    "product_item" : (By.XPATH, '//*[@id="center_column"]/ul/li[1]'),
    "proceed_to_checkout" : (By.XPATH, '//*[@id="layer_cart"]/div[1]/div[2]/div[4]/a/span'),
    "quantity_counter" : (By.XPATH, '//*[@id="quantity_wanted"]'),
    "plus_button" : (By.XPATH, '//*[@id="quantity_wanted_p"]/a[2]/span'),
    "size_dropdown" : (By.XPATH, '//*[@id="group_1"]'),
    "white_color" : (By.XPATH, '//*[@id="color_to_pick_list"]/li[1]'),
    "process_order" : (By.XPATH, '//*[@id="layer_cart"]/div[1]/div[2]/div[4]/a/span'),
    "black_color" : (By.XPATH, '//*[@id="color_11"]'),
    "minus_button" : (By.XPATH, '//*[@id="cart_quantity_down_5_19_0_0"]/span'),
    "input_counter" : (By.XPATH, '//*[@id="product_5_19_0_0"]/td[5]/input[1]')
}
