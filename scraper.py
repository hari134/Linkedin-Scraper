from scrape_functions import ScrapeFunctions


class Scraper(ScrapeFunctions):
    def __init__(self, linkedin_url):
        super().__init__(linkedin_url)

    def scrape(self):
        self.login()
        self.get_profile_page()
        self.get_sections()
        self.get_name()
        self.get_about()
        self.get_education()
        self.get_experiences()
        self.get_skills()
        # self.get_profile_pic()

    def display(self):
        print(self.details)


user_linkedin_url = "https://www.linkedin.com/in/user_you_want_to_scrape"
scraper = Scraper(user_linkedin_url)
scraper.set_credentials(email="whackiestpb@gmail.com", password="whackiest@123")
scraper.scrape()
scraper.display()
# execution time 37 seconds
