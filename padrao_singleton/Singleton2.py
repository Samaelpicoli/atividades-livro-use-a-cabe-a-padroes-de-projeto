class Singleton2:
    """
    Implementação do padrão Singleton com inicialização imediata.

    O padrão Singleton garante que uma classe tenha apenas uma instância
    e proporciona um ponto de acesso global a essa instância. Esta
    versão implementa a inicialização imediata, o que significa que
    a instância é criada na primeira vez que é solicitada, mantendo
    a consistência em todo o sistema.
    """
    
    _unique_instance = None

    def __new__(cls):
        """
        Método para retornar a instância única da classe.

        Este método é responsável por criar a instância da classe
        se ela ainda não existir. Se a instância já foi criada,
        ele simplesmente retorna a instância existente.
        """
        if cls._unique_instance is None:
            cls._unique_instance = super(Singleton2, cls).__new__(cls)
            # Inicialização de outras variáveis de instância, se necessário
        return cls._unique_instance

    @classmethod
    def get_instance(cls):
        """
        Retorna a instância única da classe Singleton2.

        Returns:
            Singleton2: A instância única da classe.

        Este método fornece um ponto de acesso global à instância
        única, garantindo que ela seja criada na primeira chamada,
        se ainda não existir.
        """
        if cls._unique_instance is None:
            cls()  # Chama __new__ para garantir que a instância seja criada
            print('unico')
        return cls._unique_instance

    def __init__(self):
        """
        Inicializa a instância da classe.

        Este método é chamado apenas uma vez, na primeira vez que
        a instância é criada, permitindo a inicialização de variáveis
        de instância sem afetar chamadas subsequentes.
        """
        # Inicialização de variáveis de instância
        pass

    # Outros métodos da classe
    def some_method(self):
        """
        Um exemplo de método na classe Singleton.
        """
        print("Método do Singleton chamado.")

# Exemplo de uso
singleton2 = Singleton2.get_instance()
singleton2.get_instance()