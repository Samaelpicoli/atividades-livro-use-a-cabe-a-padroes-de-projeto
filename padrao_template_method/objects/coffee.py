from templates.caffeine_beverage import CaffeineBeverage


class Coffee(CaffeineBeverage):
    """
    Classe que representa a preparação de café.

    Esta classe estende a classe abstrata CaffeineBeverage e implementa
    os métodos necessários para preparar o café. O método brew define
    como o café é feito, enquanto o método add_condiments adiciona os
    condimentos desejados. 

    O padrão Template Method é utilizado para definir o fluxo de preparo,
    permitindo que subclasses (como CoffeeWithHook) personalizem a lógica
    de adição de condimentos sem alterar o fluxo principal da preparação.
    """

    def brew(self):
        """Prepara o café, filtrando o líquido."""
        print('Dripping Coffee through filter')

    def add_condiments(self):
        """Adiciona açúcar e leite ao café."""
        print('Adding Sugar and Milk')