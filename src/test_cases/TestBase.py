from src.wrappers.browser_wrapper import BrowserWrapper

class TestBase:

    @staticmethod
    def setup_test(url):
        print("Setup the test")
        global browserObj
        browserObj = BrowserWrapper()
        browserObj.maximize_window_browser()
        browserObj.go_to_url(url)

    @staticmethod
    def cleanup_test():
        print("Setup the test")
        browserObj.quit()
