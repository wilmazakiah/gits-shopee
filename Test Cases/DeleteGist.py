from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://github.com/")
element = browser.find_element_by_css_selector('body > div.position-relative.js-header-wrapper > header > div > div.HeaderMenu.HeaderMenu--logged-out.position-fixed.top-0.right-0.bottom-0.height-fit.position-lg-relative.d-lg-flex.flex-justify-between.flex-items-center.flex-auto > div.d-lg-flex.flex-items-center.px-3.px-lg-0.text-center.text-lg-left > a.HeaderMenu-link.no-underline.mr-3')
element.click()
element = browser.find_element_by_id('login_field')
element.send_keys('username')
element = browser.find_element_by_id('password')
element.send_keys('password')
element = browser.find_element_by_css_selector('#login > form > div.auth-form-body.mt-3 > input.btn.btn-primary.btn-block')
element.click()
element = browser.find_element_by_css_selector('body > div.position-relative.js-header-wrapper > header > div:nth-child(6) > details > summary > svg > path')
element.click()
element = browser.find_element_by_css_selector('body > div.position-relative.js-header-wrapper > header > div:nth-child(6) > details > details-menu > a:nth-child(3)')
element.click()
element = browser.find_element_by_xpath('//*[@id="gist-pjax-container"]/div[1]/div/div/ul/li[1]/div/a/strong')
element.click()
element = browser.find_element_by_xpath('//*[@id="gist-pjax-container"]/div[1]/div/div[1]/ul/li[2]/form/button')
element.click()