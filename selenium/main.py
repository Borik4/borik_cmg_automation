from imports.imports_chrome import *
from login_tests import *

chrome_options = ChromeOptions()
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
driver.minimize_window()

print(login_page_structure_test(driver))
print(invalid_login_pass_test(driver))
print(forgot_password(driver))
print(valid_username_password(driver))
driver.close()
driver.quit()