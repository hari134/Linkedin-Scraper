from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class ScraperInit:
    _SECTION_TAGS = {'profile_section': 'profile-sticky-header-toggle',
                     'about': 'about',
                     'education': 'education',
                     'skills': 'skills',
                     'projects': 'projects'}

    _LINKEDIN_LOGIN_URL = "https://linkedin.com/uas/login"

    def __init__(self, linkedin_url, ):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("window-size=1024,768")
        options.add_argument("--no-sandbox")
        self.driver = webdriver.Chrome(options=options)
        self.linkedin_url = linkedin_url
        self.details = {"experiences": [], "educations": []}
        self.sections = {}

    def get_sections(self):
        # //main[@id="main"]/section[.//div[contains(@id,"education")]]
        for key, value in self._SECTION_TAGS.items():
            self.sections[key] = self.driver.find_element(By.XPATH,
                                                          '//main[@id="main"]/section[.//div[contains(@id,{id})]]'.format(
                                                              id=value))

    def set_credentials(self, email, password):
        self._CREDENTIALS = {"email": email, "password": password}

    def login(self):
        self.driver.get(self._LINKEDIN_LOGIN_URL)
        time.sleep(5)
        username = self.driver.find_element(By.ID, "username")
        username.send_keys(self._CREDENTIALS["email"])
        passwd = self.driver.find_element(By.ID, "password")
        passwd.send_keys(self._CREDENTIALS["password"])

        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()

    def get_profile_page(self):
        self.driver.get(self.linkedin_url)
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(2)
