
class FillEmailGuruPage:
    __instance = None

    @staticmethod
    def get_instance():
        if FillEmailGuruPage.__instance is None:
            FillEmailGuruPage.__instance = FillEmailGuruPage()
        return FillEmailGuruPage.__instance