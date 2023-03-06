from selenium.webdriver.common.by import By

class LabTestsClass:
    def __init__(self, driver):
        self.driver = driver


        # Element Locators Values
        self.laterButtonElement="//*[@id='wzrk-cancel']"
        self.TopBookedTestsViewAllButtonElement= "(//*[text()='View All'])[1]"
        self.PopularCategoriesViewAllButtonElement= "(//*[text()='View All'])[3]"
        self.ReportsWithin24HoursLinkElement="//*[text()='Reports on same day']"
        self.WomenWellnessViewAllButtonElement= "(//*[text()='View All'])[8]"
        self.VitalOrgansViewAllButtonElement= "(//*[text()='View All'])[6]"


        # Creating Element Methods

    def click_later_Button(self):
            laterButton= self.driver.find_element(By.XPATH, self.laterButtonElement)
            laterButton.click()

    def click_TopBookedTestsViewAll_Button(self):
            TopBookedTestsViewAllButton=self.driver.find_element(By.XPATH, self.TopBookedTestsViewAllButtonElement)
            TopBookedTestsViewAllButton.click()


    def click_PopularCategoriesViewAll_Button(self):
            PopularCategoriesViewAllButton=self.driver.find_element(By.XPATH, self.PopularCategoriesViewAllButtonElement)
            PopularCategoriesViewAllButton.click()

    def click_ReportsWithin24Hours_link(self):
            ReportsWithin24HoursLink=self.driver.find_element(By.XPATH, self.ReportsWithin24HoursLinkElement)
            ReportsWithin24HoursLink.click()

    def click_WomenWellnessViewAll_Button(self):
            WomenWellnessViewAllButton=self.driver.find_element(By.XPATH, self.WomenWellnessViewAllButtonElement)
            WomenWellnessViewAllButton.click()


    def click_VitalOrgansViewAll_Button(self):
            VitalOrgansViewAllButton=self.driver.find_element(By.XPATH, self.VitalOrgansViewAllButtonElement)
            VitalOrgansViewAllButton.click()
