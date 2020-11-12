*** Setting ***
Library    Selenium2Library

*** Variables ***
${TARGET}    http://localhost:5000/login

*** Test Cases ***

Get Page Without Logging In Using Chrome
    open app with chrome
    check labels and fields and button
    check state without logging in
    sleep3s
    close app

Get Page Without Logging In Using Firefox
    open app with firefox
    check labels and fields and button
    check state without logging in
    sleep3s
    close app

Login With Correct Pairs Using Chrome
    open app with chrome
    log in to app    admin    admin
    check labels and fields and button
    check successful login
    sleep3s
    close app

Login With Correct Pairs Using Firefox
    open app with firefox
    log in to app    admin     admin
    check labels and fields and button
    check successful login
    sleep3s
    close app

Login With Incorrect Pairs Using Chrome
    open app with chrome
    log in to app    admin    admi
    check labels and fields and button
    check unsuccessful login
    sleep 3s
    close app

Login With Incorrect Pairs Using Firefox
    open app with firefox
    log in to app    hello    hell
    check labels and fields and button
    check unsuccessful login
    sleep 3s
    close app

*** Keywords ***
open app with chrome
    Open Browser                ${TARGET}    chrome
    Wait Until Page Contains    CURRENT STATE
open app with firefox
    Open Browser                ${TARGET}    firefox
    Wait Until Page Contains    CURRENT STATE
check labels and fields and button
    Page Should Contain    USERNAME
    Page Should Contain    PASSWORD
    Page Should Contain Textfield    id:username
    Page Should Contain Element   id:password    #password field found
    Page Should Contain Button   class:btn
log in to app
    [Arguments]      ${user}    ${pwrd}
    Input Text       username       ${user}
    Input Password   password       ${pwrd}
    Click Button     SUBMIT
check state without logging in
    Page Should Contain    Complete the fields
check successful login
    Page Should Contain    successfully
check unsuccessful login
    Page Should Contain    be found
sleep3s
    sleep    3s
close app
    Close Browser
