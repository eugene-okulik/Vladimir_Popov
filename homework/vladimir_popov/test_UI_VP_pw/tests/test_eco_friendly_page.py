import pytest

first_item_page = "ana-running-short.html"


@pytest.mark.positive
def test_add_item_to_compare(eco_friendly_collection_page):
    eco_friendly_collection_page.open_page()
    eco_friendly_collection_page.add_to_compare()
    eco_friendly_collection_page.check_compared_item_added()


@pytest.mark.positive
def test_add_item_to_cart(eco_friendly_collection_page):
    eco_friendly_collection_page.open_page()
    eco_friendly_collection_page.add_item_to_cart()
    eco_friendly_collection_page.check_page_url(first_item_page)


def test_clear_comare_items(eco_friendly_collection_page):
    eco_friendly_collection_page.open_page()
    eco_friendly_collection_page.add_to_compare()
    eco_friendly_collection_page.check_compared_item_added()
    eco_friendly_collection_page.clear_compare_items()
    eco_friendly_collection_page.check_compare_item_is_not_visible()
