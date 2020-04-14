from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper


class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/group.php")

    def return_to_homepage(self):
        wd = self.wd
        wd.find_element_by_link_text("HOME").click()

    def create_contact(self, contact):
        wd = self.wd
        self.open_add_contact_page()
        # fill contact form
        wd.find_element_by_name("firstname").send_keys(contact.first_name)
        wd.find_element_by_name("middlename").send_keys(contact.middle_name)
        wd.find_element_by_name("lastname").send_keys(contact.last_name)
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        wd.find_element_by_name("title").send_keys(contact.title)
        wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("home").send_keys(contact.phone_home)
        wd.find_element_by_name("work").send_keys(contact.phone_work)
        wd.find_element_by_name("fax").send_keys(contact.fax)
        wd.find_element_by_name("email").send_keys(contact.email)
        wd.find_element_by_name("email2").send_keys(contact.email2)
        wd.find_element_by_name("email3").send_keys(contact.email3)
        wd.find_element_by_name("homepage").send_keys(contact.homepage)
        wd.find_element_by_xpath(contact.birthday_day).click()
        wd.find_element_by_xpath(contact.birthday_month).click()
        wd.find_element_by_name("byear").send_keys(contact.birthday_year)
        wd.find_element_by_xpath(contact.anniversary_day).click()
        wd.find_element_by_xpath(contact.anniversary_month).click()
        wd.find_element_by_name("ayear").send_keys(contact.anniversary_year)
        wd.find_element_by_name("address2").send_keys(contact.secondary_address)
        wd.find_element_by_name("phone2").send_keys(contact.secondary_phone)
        wd.find_element_by_name("notes").send_keys(contact.secondary_notes)
        # submit contact creation
        wd.find_element_by_name("submit").click()
        self.return_to_homepage()

    def open_add_contact_page(self):
        wd = self.wd
        wd.find_element_by_link_text("ADD_NEW").click()

    def destroy(self):
        self.wd.quit()