Feature: Map
  In order to get broader weather information,
  As a visitor
  I want to see history and forecast on the map

  Scenario: Past rain activity
    Given the main page displayed
     When I visit the rain map
     Then last 24 hours rain activity map is included
     And can save the result as "image"

  Scenario: Actual heatmap
    Given the main page displayed
     When I visit the heatmap
     Then actual heat map is included
     And can save the result as "image"