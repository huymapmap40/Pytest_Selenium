
class NewCustomerPage:
    __instance = None

    @staticmethod
    def get_instance():
        if NewCustomerPage.__instance is None:
            NewCustomerPage.__instance = NewCustomerPage()
        return NewCustomerPage.__instance