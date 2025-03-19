from selenium.webdriver.common.by import By
from PageObject.Page import Page


class LoginPage(Page):
    def __init__(self, driver):
        super().__init__(driver)
        self.init_site()

        self.username_field = (By.CSS_SELECTOR, "input[id='user_name']")
        self.password_field = (By.CSS_SELECTOR, "input[id='password']")
        self.login_button = (By.CSS_SELECTOR, "input[id='login-button']")
        self.error_message = (By.CLASS_NAME, "error-message-container")
        self.error = (By.TAG_NAME, "h3")
        self.title = (By.CLASS_NAME, "titile")

    def get_user_name_field(self):
        return self.driver.find_element(self.username_field)

    def get_password_field(self):
        return self.driver.find_element(self.password_field)

    def get_login_button(self):
        return self.driver.find_element(self.login_button)

    def enter_username(self, username):
        """Enter Username."""
        self.driver.find_element(self.username_field).send_keys(username)

    def enter_password(self, password):
        """Enter Password."""
        self.driver.find_element(self.username_field).send_keys(password)

    def click_login(self):
        """Click on login button."""
        self.driver.find_element(self.login_button).click()

    def get_error_message_text(self):
        """Return the error message on the page if exists, else returns None."""
        return self.driver.find_element(self.error_message).text.split(":")[1]

    def error_message_exist(self):
        """Returns True if error message exists on the page else False."""
        return True if self.driver.find_element(self.error_message) else False

    def title_exists(self):
        """Returns True if the title exists after successful login else false."""
        return True if self.driver.find_element(self.title).text else False
