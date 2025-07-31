import time
from pprint import pprint
from playwright.sync_api import Page
def scrape_data(page: Page):
    try:
        train_button = page.locator('[data-test="practice-hub-nav"]')
        train_button.click(force=True)
        action_to_words = page.locator('[data-test="practice-hub-collection-button"]', has_text="Повторяйте слова из курса английского в любое время")
        action_to_words.scroll_into_view_if_needed()
        action_to_words.click()
        if page.locator('[data-test="plus-no-thanks"]').count() > 0:
            button = page.locator('[data-test="plus-no-thanks"]')
            button.first.click(force=True)
        while True:
            time.sleep(5)
            more_words_click = page.locator('[role="button"]', has_text="Загрузить больше")
            if more_words_click.count() > 0:
                more_words_click.scroll_into_view_if_needed()
                more_words_click.click(force=True)
            elif more_words_click.count() == 0:
                default_words = page.locator("h3").all_inner_texts()
                translate_words = page.locator("p").all_inner_texts()
                vocab_dictionary = dict(zip(default_words, translate_words))
                pprint(vocab_dictionary, sort_dicts=False, width=120)
                break
    finally:
        pass