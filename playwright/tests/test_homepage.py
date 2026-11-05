def test_wikipedia_search(page):
    page.goto("https://www.wikipedia.org/")

    search_box = page.get_by_role("searchbox")

    search_box.fill("Software Testing")

    assert search_box.input_value() == "Software Testing"