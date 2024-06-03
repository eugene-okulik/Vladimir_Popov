womens_sales_page = "promotions/women-sale.html"
mens_sales_page = "promotions/men-sale.html"
womens_sales_page_button_text = "Shop Women’s Deals"


def test_open_womens_deals_page(sales_page):
    sales_page.open_page()
    sales_page.open_women_sales()
    sales_page.check_page(womens_sales_page)


def test_open_mens_deals_page(sales_page):
    sales_page.open_page()
    sales_page.open_men_sales()
    sales_page.check_page(mens_sales_page)


def test_check_women_sales_page_button_text(sales_page):
    sales_page.open_page()
    sales_page.check_element_text(sales_page.womens_sales_button_locator, text=womens_sales_page_button_text)
