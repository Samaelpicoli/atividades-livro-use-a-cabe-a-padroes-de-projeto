from abc import ABC, abstractmethod

class CaffeineBeverage(ABC):
    """
    Classe abstrata que define o método template para preparar bebidas
    de cafeína.

    O padrão Template Method permite que subclasses definam o esqueleto
    de um algoritmo,
    enquanto algumas etapas do algoritmo são deixadas para serem
    implementadas pelas subclasses.

    Este método template `prepare_recipe` define o fluxo de preparação
    da bebida, incluindo a fervura da água, a preparação da bebida
    (método abstrato), o despejo na xícara e a adição de condimentos
    (também um método abstrato).

    Subclasses como `Tea` e `Coffee` devem fornecer implementações 
    específicas para os métodos `brew` e `add_condiments`, permitindo que
    cada bebida customize seu próprio processo de preparação, enquanto mantém
    a estrutura geral definida aqui.
    """

    def prepare_recipe(self):
        """Prepara a bebida de cafeína usando o método template."""
        self.boil_water()
        self.brew()
        self.pour_in_cup()
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