import time
from hamcrest import *
from behave import *
from features.pages.LabTestsClass import LabTestsClass

@given(u'Chrome is opened and Apollo app is opened')
def step_impl(context):
    time.sleep(5)
    expectedTitle = "Book Lab Tests at Home from Apollo Diagnostics, Pathology Labs near me"
    actualTitle = context.driver.title
    print("Page title is " + actualTitle)
    assert_that(expectedTitle, equal_to(actualTitle))

@when(u'User clicks on later button')
def step_impl(context):
    time.sleep(2)
    laterbutton = LabTestsClass(context.driver)
    laterbutton.click_later_Button()


@when(u'User clicks on TOP BOOKED TESTS (42) ViewAll Button')
def step_impl(context):
    time.sleep(2)
    LabTests = LabTestsClass(context.driver)
    LabTests.click_TopBookedTestsViewAll_Button()

@then(u'It Navigates to Top Booked Tests webpage.')
def step_impl(context):

    time.sleep(5)
    expectedTitle = "Top Tests to Manage Your Health at the Best Prices from Apollo 24|7"
    actualTitle = context.driver.title
    print("Page title is " + actualTitle)
    assert_that(expectedTitle, equal_to(actualTitle))

@when(u'User clicks on POPULAR CATEGORIES (33) ViewAll Button')
def step_impl(context):
    time.sleep(2)
    LabTests = LabTestsClass(context.driver)
    LabTests.click_PopularCategoriesViewAll_Button()

@then(u'It Navigates to Popular Categories webpage.')
def step_impl(context):
    time.sleep(5)
    expectedTitle = "Avail Popular Health Checkups at Affordable Prices - Apollo 24|7"
    actualTitle = context.driver.title
    print("Page title is " + actualTitle)
    assert_that(expectedTitle, equal_to(actualTitle))


@when(u'User clicks on Reports on same day link')
def step_impl(context):
    time.sleep(2)
    LabTests = LabTestsClass(context.driver)
    LabTests.click_ReportsWithin24Hours_link()

@then(u'It Navigates to full body checkup  webpage.')
def step_impl(context):
    time.sleep(5)
    expectedTitle = "Apollo Full Body Checkup - Basic Test - Price, Preparation, Range - Apollo 24|7"
    actualTitle = context.driver.title
    print("Page title is " + actualTitle)
    assert_that(expectedTitle, equal_to(actualTitle))

@when(u'User clicks on WOMEN WELLNESS (19) ViewAll Button')
def step_impl(context):
    time.sleep(2)
    LabTests = LabTestsClass(context.driver)
    LabTests.click_WomenWellnessViewAll_Button()

@then(u'It Navigates to Women Wellness Webpage')
def step_impl(context):
    time.sleep(5)
    expectedTitle = "Women Wellness Tests and Packages at the Best Prices - Apollo 24|7"
    actualTitle = context.driver.title
    print("Page title is " + actualTitle)
    assert_that(expectedTitle, equal_to(actualTitle))

@when(u'User clicks on VITAL ORGANS (8) ViewAll Button')
def step_impl(context):
    time.sleep(2)
    LabTests = LabTestsClass(context.driver)
    LabTests.click_VitalOrgansViewAll_Button()

@then(u'It Navigates to Vital Organs Webpage')
def step_impl(context):
    time.sleep(5)
    expectedTitle = "Get Vital Organ Screening at the Best Price - Apollo 24|7"
    actualTitle = context.driver.title
    print("Page title is " + actualTitle)
    assert_that(expectedTitle, equal_to(actualTitle))