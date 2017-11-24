from Pages.SignUp.SignUpPage import SignUpPage


# All fields is empty. Check massage "Required"
def test_all_required_massage_is_displayed(driver):
    sign_up = SignUpPage(driver)
    sign_up.open_signup_page()
    sign_up.is_all_required_massage()


# Shop url. Massage: "Required"
def test_shop_url_required_massage(driver):
    sign_up = SignUpPage(driver)
    sign_up.open_signup_page()
    sign_up.send_keys_email_field('some@email.com')
    sign_up.send_keys_password('some_text')
    sign_up.send_keys_first_name_field('some_name')
    sign_up.click_signup_button()
    assert sign_up.is_shop_url_field_required_massage()


# Email. Massage: "Required"
def test_email_required_massage(driver):
    sign_up = SignUpPage(driver)
    sign_up.open_signup_page()
    sign_up.send_keys_shop_url_field('some-url.com')
    sign_up.send_keys_password('some_text')
    sign_up.send_keys_first_name_field('some_name')
    sign_up.click_signup_button()
    assert sign_up.is_email_field_required_massage()


# Password. Massage: "Required"
def test_password_url_required_massage(driver):
    sign_up = SignUpPage(driver)
    sign_up.open_signup_page()
    sign_up.send_keys_email_field('some@email.com')
    sign_up.send_keys_shop_url_field('some-url.com')
    sign_up.send_keys_first_name_field('some_name')
    sign_up.click_signup_button()
    assert sign_up.is_password_field_required_massage()


# First name. Massage: "Required"
def test_first_name_url_required_massage(driver):
    sign_up = SignUpPage(driver)
    sign_up.open_signup_page()
    sign_up.send_keys_email_field('some@email.com')
    sign_up.send_keys_shop_url_field('some-url.com')
    sign_up.send_keys_password('some_text')
    sign_up.click_signup_button()
    assert sign_up.is_first_name_field_required_massage()


def test_one(driver, industry='Fashion'):
    sign_up = SignUpPage(driver)
    sign_up.open_signup_page()
    sign_up.chose_industry(industry)
    assert sign_up.is_selected_industry(industry)
