def test_wikipedia_search(page):
    page.goto("https://www.wikipedia.org/")

    search_box = page.get_by_role("searchbox")
    search_box.fill("Software Testing")

    search_button = page.get_by_role("button", name="Search")
    search_button.click()

    page.wait_for_url("**/wiki/Software_testing")

    assert "Software testing" in page.title()