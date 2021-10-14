from .base_page import BasePage
from .locators import BasketPageLocals


class BasketPage(BasePage):

    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocals.BASKET_FORMSET), \
            "Products in basket presented, but should not be"

    def should_be_empty_basket_message(self):
        assert self.is_element_present(*BasketPageLocals.EMPTY_BASKET_MESSAGE), \
            "\"Your basket is empty\" message is not presented, but should be"
