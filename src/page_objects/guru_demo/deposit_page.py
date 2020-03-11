
class DepositPage:
    __instance = None

    @staticmethod
    def get_instance():
        if DepositPage.__instance is None:
            DepositPage.__instance = DepositPage()
        return DepositPage.__instance