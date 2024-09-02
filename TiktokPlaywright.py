from playwright.sync_api import Playwright, sync_playwright
import sys
sys.path.insert(1, 'c:/Users/ayan_/Desktop/Desktop/Coding/Cursor Workspace/Scrapers')
from tiktok_credentials import email, password
import time

def run(playwright: Playwright) -> None:
    main_url = "https://ads.tiktok.com/business/creativecenter/pad/en"
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(ignore_https_errors=True, user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.81")
    page = context.new_page()

    # Navigating to the page
    page.goto(main_url)
    # Clicking the login button
    page.get_by_test_id("cc_header_login").click()
    time.sleep(5)
    #

    page.get_by_text("Log in with phone/email").click()
    page.get_by_placeholder("Enter your email address").click()
    page.get_by_placeholder("Enter your email address").fill(email)
    page.get_by_placeholder("Enter your password").click()
    page.get_by_placeholder("Enter your password").fill(password)
    page.click("#TikTok_Ads_SSO_Login_Btn")
    
    time.sleep(5)

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
