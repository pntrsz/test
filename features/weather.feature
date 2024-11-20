Feature: Weather
  In order to get weather information,
  As a visitor
  I want to find hand on information about the weather

  Scenario: How to dress up
    Given the main page displayed
     Then dress advisement is written
     And can save the result as "text"

  Scenario: Rain forecast
    Given the main page displayed
     Then rain forecast is shown at laast for "4" days
     And can save the result as "comma separated"