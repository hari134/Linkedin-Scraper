from scraper_init import ScraperInit
from selenium.webdriver.common.by import By
import time


class ScrapeFunctions(ScraperInit):

    def __init__(self, linkedin_url):
        super().__init__(linkedin_url)

    def get_name(self):
        name_loc = self.sections["profile_section"].find_element(By.TAG_NAME, "h1")
        name = name_loc.text
        self.details["name"] = name

    def get_about(self):
        about = self.sections['about'].find_element(
            By.XPATH, '//div[@class="display-flex ph5 pv3"]'
        )
        self.details["about"] = about.text

    def get_profile_pic(self):
        image_bar = self.sections["profile_section"].find_element(
            By.CLASS_NAME,
            "pv-top-card-profile-picture__image pv-top-card-profile-picture__image--show ember-view",
        )
        image_url = image_bar.get_attribute("src")
        self.details["profile_pic_url"] = image_url

    def get_experiences(self):
        experience_section = self.driver.find_element(
            By.XPATH, '//main[@id="main"]/section[.//div[contains(@id,"experience")]]'
        )
        experiences_footer = experience_section.find_element(
            By.XPATH, './/div[@class="pvs-list__footer-wrapper"]'
        )

        experiences_link = experiences_footer.find_element(By.XPATH, './/a').get_attribute('href')

        if experiences_link:
            self.driver.get(experiences_link)
            time.sleep(2)
            self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            time.sleep(2)
            experience_section = self.driver.find_element(
                By.XPATH, '//main[@id="main"]//section[1]'
            )

        experiences = experience_section.find_elements(
            By.XPATH,
            './/div[@class="display-flex flex-column full-width align-self-center"]',
        )

        for experience in experiences:
            title = experience.find_element(
                By.XPATH, './/span[@class="mr1 t-bold"]/span[@aria-hidden="true"]'
            ).text

            company_and_role = experience.find_element(
                By.XPATH, './/span[@class="t-14 t-normal"]/span[@aria-hidden="true"]'
            ).text

            duration_and_location_bar = experience.find_elements(
                By.XPATH,
                './/span[@class="t-14 t-normal t-black--light"]/span[@aria-hidden="true"]',
            )
            try:
                duration = duration_and_location_bar[0].text
            except:
                duration = ""
            try:
                location = duration_and_location_bar[1].text
            except:
                location = ""

            experience_dict = {
                "title": title,
                "company_and_role": company_and_role,
                "duration": duration,
                "location": location,
            }
            self.details["experiences"].append(experience_dict)
        self.driver.back()
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(2)

    def get_education(self):
        education_section = self.driver.find_element(
            By.XPATH, '//main[@id="main"]/section[.//div[contains(@id,"education")]]'
        )
        educations = education_section.find_elements(By.XPATH,
                                                     './/div[@class="display-flex flex-column full-width align-self-center"]')
        for education in educations:
            institute_name = education.find_element(By.XPATH,
                                                    './/span[@class="mr1 hoverable-link-text t-bold"]/span[@aria-hidden="true"]').text
            try:
                course = education.find_element(By.XPATH,
                                                './/span[@class="t-14 t-normal"]/span[@aria-hidden="true"]').text
            except:
                course = ""
            try:
                duration = education.find_element(By.XPATH,
                                                  './/span[@class="t-14 t-normal t-black--light"]/span[@aria-hidden="true"]').text
            except:
                duration = ""

            try:
                description = education.find_element(By.XPATH,
                                                     './/div[@class="pvs-list__outer-container"]').text
            except:
                description = ""

            education_details = {'intitute_name': institute_name,
                                 'course': course,
                                 'duration': duration,
                                 'description': description}

            self.details["educations"].append(education_details)

    def get_skills(self):
        # skill_section = self.sections["skills"]
        skill_section = self.driver.find_element(
            By.XPATH, '//main[@id="main"]/section[.//div[contains(@id,"skills")]]'
        )

        skill_footer = skill_section.find_element(
            By.XPATH, './/div[@class="pvs-list__footer-wrapper"]'
        )

        skill_link = skill_footer.find_element(By.XPATH, './/a').get_attribute('href')

        if skill_link:
            self.driver.get(skill_link)
            time.sleep(2)
            self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            time.sleep(2)
            skill_section = self.driver.find_element(
                By.XPATH, '//main[@id="main"]//section[1]'
            )
        skills = skill_section.find_elements(By.XPATH,
                                             './/div[@class="display-flex flex-column full-width align-self-center"]')
        skill_list = []
        for skill in skills:
            skill_name = skill.find_element(By.XPATH,
                                            './/span[@class="mr1 hoverable-link-text t-bold"]/span[@aria-hidden="true"]').text
            if skill_name == '':
                continue
            skill_list.append(skill_name)
        self.details["skills"] = skill_list
