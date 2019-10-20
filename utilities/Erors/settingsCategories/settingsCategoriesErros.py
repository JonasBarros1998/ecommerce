import sys

class CategoriesError:
    def __init__(self):
        pass

    @classmethod
    def checkCategorie(self):

        raise NameError('''Essa categories não existe. Confirme se escreveu o nome correto
        Ou então adicione essa categoria dentro de categoriesSettings: 
        utilities.ProductsCategories.categoriesSettings''')
        