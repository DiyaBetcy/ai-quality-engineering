from playwright.sync_api import expect

def test_wikipedia_search(page):
    page.goto("https://www.wikipedia.org/")

    search_box = page.get_by_role("searchbox")
    search_box.fill("Software Testing")
    
    expect(search_box).to_have_value("Software Testing")


    search_button = page.get_by_role("button", name="Search")
    search_button.click()

    page.wait_for_url("**/wiki/Software_testing")

    expect(page).to_have_title("Software testing - Wikipedia")