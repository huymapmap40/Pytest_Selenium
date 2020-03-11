
class DeleteCustomerPage:
    __instance = None

    @staticmethod
    def get_instance():
        if DeleteCustomerPage.__instance is None:
            DeleteCustomerPage.__instance = DeleteCustomerPage()
        return DeleteCustomerPage.__instance

