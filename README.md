# Linkedin-Scraper
Linkedin Scraper written in python using selenium

A simple scraper that scrapes the following details of a linkedin user by their public linkedin url:
1. <strong><em>Name</em></strong>
2. <strong><em>About</em></strong>
3. <strong><em>Educational qualifications</em></strong>
4. <strong><em>Experiences</em></strong>
5. <strong><em>Skills</em></strong>

To use the scraper initlialize a scraper object with the url to be scraped and set the credentials of a valid linkedin account to the scraper object 
```python
user_linkedin_url = "https://www.linkedin.com/in/user_you_want_to_scrape"
scraper = Scraper(user_linkedin_url)
scraper.set_credentials(email="your@email.com", password="your_password")
scraper.scrape()
scraper.display()
# execution time 37 seconds
```
