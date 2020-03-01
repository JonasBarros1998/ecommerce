from utilities.Erors.settingsCategories.settingsCategoriesErros import CategoriesError
"""
    O modulo tem a função se caso precisarmos utilizar 
    alguma viewSet, em outro componente, não precisamos 
    importar diretamente, apenas utilizar o metodo 
    mothodsCategories 
"""

class AllCategories:

    def __init__(self):
        pass

    def methodsCategories(self, categories:str):

        categorieErrors = CategoriesError()

        try:
            methods = {
                "cftv": self.__fileCftv(),
                "smartwatch": self.__fileSmartWatch(),
                "airphone": self.__fileAirPhone()
            }
            return methods[categories]

        except KeyError:
            categorieErrors.checkCategorie()

    def __importFilesCategories(self):

        filesCategories = {
            "cftv": __import__('products.categories.categorieCftv.viewsets.CftvViewSet', globals(), locals(), ['CftvViewSet'], 0),
            "smartwatch": __import__('products.categories.smartWatch.viewset.smartWathViewSet', globals(), locals(), ['smartWatchViewSet'], 0),
            "airphone": __import__('products.categories.airphones.viewsets.airPhonesViewSet', globals(), locals(), ['AirphonesViewSet'], 0)
        }

        return filesCategories
    
    def __fileCftv(self):

        fileCategories = self.__importFilesCategories()
        CategorieCftv = fileCategories['cftv'].CftvViewSet()
        return CategorieCftv.list()


    def __fileSmartWatch(self):

        fileCategories = self.__importFilesCategories()
        categorieSmartWatch = fileCategories['smartwatch'].SmartWathViewSet()
        return categorieSmartWatch.list()


    def __fileAirPhone(self):

        fileCategories = self.__importFilesCategories()
        categorieAirPhone = fileCategories['airphone'].AirphonesViewSet()
        return categorieAirPhone.list()