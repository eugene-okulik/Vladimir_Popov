import pytest
from pages.create_customer_page import CreateCustomerPage
from pages.eco_friendly_collection_page import EcoFriendlyCollectionPage
from pages.sales_page import SalesPage
from playwright.sync_api import Page


@pytest.fixture
def create_customer_page(page: Page):
    return CreateCustomerPage(page)


@pytest.fixture
def eco_friendly_collection_page(page: Page):
    return EcoFriendlyCollectionPage(page)


@pytest.fixture
def sales_page(page: Page):
    return SalesPage(page)
