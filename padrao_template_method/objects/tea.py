from templates.caffeine_beverage import CaffeineBeverage


class Tea(CaffeineBeverage):
    """
    Classe que representa a preparação de chá.

    Esta classe estende a classe abstrata CaffeineBeverage e implementa os
    métodos necessários para preparar o chá. O método brew define como o chá
    é preparado, enquanto o método add_condiments adiciona os condimentos
    desejados. O padrão Template Method é utilizado para definir o fluxo de
    preparo, permitindo que subclasses personalizem a lógica de adição de
    condimentos sem alterar o fluxo principal da preparação.
    """

    def brew(self):
        """Prepara o chá, infundindo as folhas."""
        print('Steeping the tea')


    def add_condiments(self):
        """Adiciona limão ao chá."""
        print('Adding Lemon')