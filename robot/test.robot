*** Setting ***
Library    Selenium2Library
Library    mylib.py
Test Setup        Steps to setup 
Test Teardown     Steps to teardown

*** Variables ***
${TARGET}    http://localhost:5000/login
${TIMEOUT}   5 seconds

*** Test Cases ***

Get Page Without Logging In Using Chrome
    Open app with chrome
    Check labels and fields and button
    Check state without logging in

Get Page Without Logging In Using Firefox
    Open app with firefox
    Check labels and fields and button
    Check state without logging in

Login With Correct Pairs Using Chrome
    Open app with chrome
    Log in to app    admin    admin
    Check labels and fields and button
    Check successful login

Login With Correct Pairs Using Firefox
    Open app with firefox
    Log in to app    admin     admin
    Check labels and fields and button
    Check successful login

Login With Incorrect Pairs Using Chrome
    Open app with chrome
    Log in to app    admin    admi
    Check labels and fields and button
    Check unsuccessful login

Login With Incorrect Pairs Using Firefox
    Open app with firefox
    Log in to app    hello    hell
    Check labels and fields and button
    Check unsuccessful login

*** Keywords ***
Steps to setup
    Set Selenium Timeout        ${TIMEOUT}
    Should Be True              mylib.is_destination_reachable()

Steps to teardown
    sleep    3s
    Close Browser

Open app with chrome
    Open Browser                ${TARGET}    chrome
    Wait Until Page Contains    CURRENT STATE

Open app with firefox
    Open Browser                ${TARGET}    firefox
    Wait Until Page Contains    CURRENT STATE

Check labels and fields and button
    Page Should Contain    USERNAME
    Page Should Contain    PASSWORD
    Page Should Contain Textfield    id:username
    Page Should Contain Element   id:password    #password field found
    Page Should Contain Button   class:btn

Log in to app
    [Arguments]      ${user}    ${pwrd}
    Input Text       username       ${user}
    Input Password   password       ${pwrd}
    Click Button     SUBMIT

Check state without logging in
    Page Should Contain    Complete the fields

Check successful login
    Page Should Contain    successfully

Check unsuccessful login
    Page Should Contain    be found
