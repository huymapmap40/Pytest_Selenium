from src.wrappers.BrowserWrapper import BrowserWrapper

class TestBase:

    @staticmethod
    def SetupTest(url):
        print("Setup the test")
        global browserObj
        browserObj = BrowserWrapper()
        browserObj.MaximizeWindow()
        browserObj.GoToUrl(url)

    @staticmethod
    def CleanupTest():
        print("Setup the test")
        browserObj.Quit()
