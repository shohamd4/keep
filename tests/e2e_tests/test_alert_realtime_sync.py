import pytest
from playwright.sync_api import expect
from tests.e2e_tests.utils import init_e2e_test

def test_alert_realtime_dismiss_sync(browser):
    """
    E2E test: Dismissing an alert in one browser context should update the alert status in another context in real time.
    """
    # Open a second page in the same browser context
    context = browser.context if hasattr(browser, "context") else browser.contexts[0]
    page2 = context.new_page()

    try:
        # Go to alerts feed in both pages
        init_e2e_test(browser, next_url="/alerts/feed")
        init_e2e_test(page2, next_url="/alerts/feed")

        # Wait for both pages to load alerts
        browser.wait_for_selector("[data-testid='alerts-table']")
        page2.wait_for_selector("[data-testid='alerts-table']")

        # Dismiss the first alert in the first page
        browser.get_by_test_id("alerts-table").locator(
            "[data-column-id='alertMenu']"
        ).first.get_by_test_id("dropdown-menu-button").click()
        browser.get_by_test_id("dropdown-menu-list").get_by_role(
            "button", name="Dismiss"
        ).click()

        # Wait for the real-time update in the second page
        page2.wait_for_timeout(2000)  # Adjust as needed for your app's update speed

        # Assert the alert is dismissed in the second page
        # (Replace with your actual UI assertion for dismissed alert)
        assert "Dismissed" in page2.content() or "dismissed" in page2.content().lower()

    finally:
        page2.close() 