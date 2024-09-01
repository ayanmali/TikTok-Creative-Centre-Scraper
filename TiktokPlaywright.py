from playwright.sync_api import Playwright, sync_playwright
from tiktok_credentials import email, password

def run(playwright: Playwright) -> None:
    main_url = "https://ads.tiktok.com/business/creativecenter/pad/en"
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto(main_url)
    page.get_by_test_id("cc_header_login").click()

    # with page.expect_popup() as page1_info:
    #     page.get_by_text("Log in with Google").click()
    # page1 = page1_info.value
    # page1.get_by_label("Email or phone").click()
    # page1.get_by_label("Email or phone").fill(email)
    # page1.get_by_role("button", name="Next").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
