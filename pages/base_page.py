class BasePage:
    def __init__(self, page):
        self.page = page

    def navigate(self, url: str):
        self.page.goto(url)

    def get_title(self):
        return self.page.title()