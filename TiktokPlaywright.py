from playwright.sync_api import Playwright, sync_playwright
import sys
sys.path.insert(1, 'c:/Users/ayan_/Desktop/Desktop/Coding/Cursor Workspace/Scrapers')
# from tiktok_credentials import email, password
import time

# User agent string
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"

# Declaring variables to store request cookies
user_sign = ""
timestamp = ""
web_id = ""

# Main function
def run(playwright: Playwright) -> None:
    main_url = "https://ads.tiktok.com/business/creativecenter/inspiration/topads/pc/en"
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context(user_agent=USER_AGENT)
    page = context.new_page()

    # Executes for every request that is sent from the browser
    def handle_request(request):
        # Specifically looking for the access_token request
        if "access_token" in request.url:
            # print(request.headers)

            # Storing those request headers
            global user_sign, timestamp, web_id
            user_sign = request.headers['user-sign']
            timestamp = request.headers['timestamp']
            web_id = request.headers['web-id']
            print("Cookies stored")

    page.on('request', handle_request)

    print("Grabbing cookies...")

    # # Navigating to the page
    page.goto(main_url)
    time.sleep(10)
    
    # Closing the browser
    context.close()
    browser.close()

def get_cookies():
    with sync_playwright() as playwright:
        run(playwright)
        print(user_sign, timestamp, web_id)
        return (user_sign, timestamp, web_id)