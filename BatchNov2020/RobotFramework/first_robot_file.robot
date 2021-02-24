*** Settings ***
Documentation    Suite description
Library     SeleniumLibrary

*** Test Cases ***
Search Data on Google
    Open Browser    https://www.google.co.in    chrome
    Input Text      name=q       selenium
    sleep   5s
    Click Element   name=btnk
    sleep   5s
    Close Browser

*** Keywords ***
Provided precondition
    Setup system under test