
class DeleteAccountPage:
    __instance = None

    @staticmethod
    def get_instance():
        if DeleteAccountPage.__instance is None:
            DeleteAccountPage.__instance = DeleteAccountPage()
        return DeleteAccountPage.__instance