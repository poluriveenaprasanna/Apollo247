@functionaltests
Feature: LabTests
Background:
      Given Chrome is opened and Apollo app is opened
      When User clicks on later button

  Scenario: Validate TOP BOOKED TESTS (42) ViewAll Button

      When User clicks on TOP BOOKED TESTS (42) ViewAll Button
      Then It Navigates to Top Booked Tests webpage.

  Scenario: Validate POPULAR CATEGORIES (33) ViewAll Button

      When User clicks on POPULAR CATEGORIES (33) ViewAll Button
      Then It Navigates to Popular Categories webpage.

  Scenario: Validate Reports on same day  link

      When User clicks on Reports on same day link
      Then It Navigates to full body checkup  webpage.

  Scenario: Validate WOMEN CARE (4) ViewAll Button

      When User clicks on WOMEN WELLNESS (19) ViewAll Button
      Then It Navigates to Women Wellness Webpage

  Scenario: Validate VITAL ORGANS (8) ViewAll Button

      When User clicks on VITAL ORGANS (8) ViewAll Button
      Then It Navigates to Vital Organs Webpage