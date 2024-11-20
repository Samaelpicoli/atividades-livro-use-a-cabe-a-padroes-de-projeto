from abc import ABC, abstractmethod



class CaffeineBeverageWithHook(ABC):

    """
    Classe abstrata que define o método template para preparar
    bebidas de cafeína com a opção de personalizar a adição de condimentos.

    O padrão Template Method permite que subclasses definam o esqueleto
    de um algoritmo, enquanto algumas etapas do algoritmo são deixadas para
    serem implementadas pelas subclasses.
    
    O método template `prepare_recipe` define o fluxo de preparação da bebida,
    incluindo a fervura da água, a preparação da bebida (método abstrato), 
    o despejo na xícara e a adição de condimentos. A adição de condimentos
    é controlada pelo método `customerWantsCondiments`, que pode ser
    sobrescrito pelas subclasses.
    """

    def prepare_recipe(self):
        """Prepara a bebida de cafeína usando o método template."""
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        if self.customer_wants_condiments():
            self.add_condiments()


    @abstractmethod
    def brew(self):
        """Método abstrato para a preparação da bebida."""
        pass


    @abstractmethod
    def add_condiments(self):
        """Método abstrato para adicionar condimentos."""
        pass


    def boil_water(self):
        """Ferve a água."""
        print("Boiling water")


    def pour_in_cup(self):
        """Despeja a bebida na xícara."""
        print("Pouring into cup")


    def customer_wants_condiments(self):
        """Método que determina se o cliente deseja condimentos.
        
        O comportamento padrão é retornar True, mas pode ser sobrescrito
        pelas subclasses para alterar a lógica.
        """
        return True