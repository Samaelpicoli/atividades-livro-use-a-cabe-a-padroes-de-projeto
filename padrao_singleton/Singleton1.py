class Singleton1:
    """
    Implementação do padrão Singleton.

    O padrão Singleton garante que uma classe tenha apenas uma
    instância e fornece um ponto de acesso global a essa instância.
    Isso é útil quando exatamente um objeto é necessário para
    coordenar ações em todo o sistema, como gerenciar recursos
    ou configurações globais.
    """

    _unique_instance = None

    def __new__(cls):
        """
        Método para criar uma nova instância da classe, garantindo que seja única.

        Este método é chamado para criar uma nova instância da classe.
        Ele verifica se a instância única já foi criada e, se não,
        cria uma nova instância. Caso contrário, retorna a instância existente.
        """
        if cls._unique_instance is None:
            cls._unique_instance = super(Singleton1, cls).__new__(cls)
            # Inicialização de outras variáveis de instância, se necessário
        return cls._unique_instance

    @classmethod
    def get_instance(cls):
        """
        Retorna a instância única da classe Singleton1.
        
        Returns:
            Singleton1: A instância única da classe.
        """
        if cls._unique_instance is None:
            cls()  # Chama __new__ para garantir que a instância seja criada
            print('sou unico')
        return cls._unique_instance

    def __init__(self):
        """
        Inicializa a instância da classe.
        
        Este método é chamado apenas uma vez, na primeira vez que
        a instância é criada. É importante que a inicialização
        não modifique a instância em chamadas subsequentes.
        """
        pass

    # Outros métodos da classe
    def some_method(self):
        """
        Um exemplo de método na classe Singleton.
        """
        print("Método do Singleton chamado.")


# Exemplo de uso
singleton1 = Singleton1.get_instance()
singleton2 = Singleton1.get_instance()
singleton3 = Singleton1.get_instance()