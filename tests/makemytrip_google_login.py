from playwright.sync_api import sync_playwright, TimeoutError
from playwright_stealth import stealth
import time

def mmt_google_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,
            args=[
                "--start-maximized",
                "--disable-blink-features=AutomationControlled",
                "--disable-notifications",
                "--disable-popup-blocking",
                "--disable-http2"
            ]
        )
        
        # Use a realistic User-Agent
        context = browser.new_context(
            no_viewport=True,
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        
        page = context.new_page()
        
        # Apply stealth module to bypass WAF (Akamai/Cloudflare)
        stealth(page)
        
        try:
            print("Navigating to MakeMyTrip...")
            page.goto("https://www.makemytrip.com/", timeout=60000, wait_until="domcontentloaded")
            
            # Wait for layout to stabilize
            page.wait_for_timeout(3000)
            
            # Close promotional ad if present
            print("Checking for promotional ads...")
            try:
                ad_close_btn = page.locator(".commonModal__close")
                if ad_close_btn.count() > 0:
                    ad_close_btn.first.click(timeout=3000)
                    print("Closed promotional ad.")
            except Exception:
                pass
            
            # Check if login modal is automatically open
            print("Checking if login modal is open...")
            modal_wrapper = page.locator("div[data-cy='LoginFlow'], section.modalMain, div.makeFlex.column.flexOne.whiteText.latoBold")
            
            try:
                modal_wrapper.first.wait_for(state="visible", timeout=3000)
                print("Login modal is open.")
            except TimeoutError:
                print("Login modal not open, clicking main login button...")
                try:
                    # Click the "Login or Create Account" button
                    page.locator("li[data-cy='account']").click(timeout=5000)
                    page.wait_for_timeout(2000)
                except Exception as e:
                    print(f"Failed to open login modal: {e}")
            
            print("Looking for Google Login iframe/button...")
            
            # Playwright uses frame_locator to easily interact with iframes
            google_frame = page.frame_locator("iframe[src*='accounts.google.com']")
            
            try:
                # Option 1: Google Identity Services iframe
                google_btn = google_frame.locator("#container")
                # Wait for the button inside the iframe to be visible and click it
                google_btn.wait_for(state="visible", timeout=5000)
                print("Found Google iframe, clicking button...")
                google_btn.click()
            except TimeoutError:
                print("Google iframe not found. Trying direct MMT Google login button...")
                
                # Option 2: Direct button on the MMT modal
                google_direct_btn = page.get_by_text("Google", exact=False).first
                google_direct_btn.wait_for(state="visible", timeout=5000)
                print("Clicking direct Google login button...")
                google_direct_btn.click()
                
            print("Google login window should be opening...")
            
            # Wait to observe the action
            page.wait_for_timeout(8000)
            
        except Exception as e:
            print(f"An error occurred: {e}")
            page.screenshot(path="mmt_playwright_error.png")
            with open("mmt_playwright_source.html", "w", encoding="utf-8") as f:
                f.write(page.content())
        finally:
            print("Closing browser...")
            browser.close()

if __name__ == "__main__":
    mmt_google_login()
