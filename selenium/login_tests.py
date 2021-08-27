s = ['LOG IN', 'Please enter your Login ID or Nickname. (Don’t have an account? Sign Up.)\nIf you’re a Premium Member, you can also use your email address.', 'Forgot Password?']


def login_page_structure_test(driver):
    test_1 = 'pass'
    driver.get('https://stage.coolmathgames.com/login')
    t = []
    w = driver.find_elements_by_css_selector('h1')
    for i in w:
        t.append(i.text)
    p = driver.find_elements_by_class_name('col-md-8')
    for i in p:
        t.append(i.text)
    login = driver.find_element_by_id('edit-name')
    t.append(login.get_attribute('data-msg-maxlength'))
    password = driver.find_element_by_id('edit-pass')
    t.append(password.get_attribute('data-msg-maxlength'))
    forgot_password = driver.find_element_by_class_name('forgot-password')
    t.append(forgot_password.text)
    log_in = driver.find_element_by_id('edit-submit')
    t.append(log_in.text)
    for i in s:
        if i not in t:
            test_1 = 'failed'
    return test_1


def invalid_login_pass_test(driver):
    try:
        test_2 = 'pass'
        driver.get('https://stage.coolmathgames.com/login')
        driver.find_element_by_id('edit-name').send_keys('invalidlogin')
        driver.find_element_by_id('edit-pass').send_keys('invalidpass')
        driver.find_element_by_id('edit-submit').click()
        s = driver.find_element_by_class_name('alert-dismissible').text[0:-2]
        if s != 'Sorry, we don’t have a record of that nickname and/or password. Free users should enter their Login ID or Nickname, Premium Users can also enter their email address':
            test_2 = 'failed'
        return test_2
    except Exception as ex:
        return 'failed', ex


def valid_username_password(driver):
    try:
        test_3 = 'pass'
        driver.get('https://stage.coolmathgames.com/login')
        driver.find_element_by_id('edit-name').send_keys('testrafik')
        driver.find_element_by_id('edit-pass').send_keys('testrafik')
        driver.find_element_by_id('edit-submit').click()
        if driver.find_element_by_class_name('title-with-button').text != 'NEW GAMES':
            test_3 = 'failed'
        return test_3
    except Exception as ex:
        return 'failed', ex


def forgot_password(driver):
    try:
        test_4 = 'pass'
        driver.get('https://stage.coolmathgames.com/login')
        driver.find_element_by_class_name('forgot-password').click()
        if driver.find_element_by_css_selector('h1').text != 'FORGOT PASSWORD':
            test_4 = 'failed'
        return test_4
    except Exception as ex:
        return 'failed', ex


def sign_up(driver):
    try:
        test_5 = 'pass'
        driver.get('https://stage.coolmathgames.com/login')
        driver.find_element_by('forgot-password').click()
        driver.find_element_by_css_selector('body > div.dialog-off-canvas-main-canvas > div > main > div.page__content > div > div:nth-child(2) > div > p:nth-child(1) > strong > a').click()
        if driver.find_element_by_class_name('title').text != 'CREATE A FREE ACCOUNT':
            test_5 = 'failed'
        return test_5

    except Exception as ex:
        return 'failed', ex