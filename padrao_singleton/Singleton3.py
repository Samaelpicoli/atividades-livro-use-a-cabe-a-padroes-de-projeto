import threading

class Singleton3:
    """
    Implementação do padrão Singleton com segurança para threads.
    """

    _unique_instance = None
    _lock = threading.Lock()

    def __new__(cls):
        """
        Retorna a instância única da classe Singleton3.
        """
        if cls._unique_instance is None:
            with cls._lock:  # Garante que apenas uma thread possa entrar aqui
                if cls._unique_instance is None:
                    cls._unique_instance = super(Singleton3, cls).__new__(cls)
                    # Inicialização de outras variáveis de instância, se necessário
        return cls._unique_instance

    @classmethod
    def get_instance(cls):
        """
        Retorna a instância única da classe Singleton3.

        Returns:
            Singleton3: A instância única da classe.
        """
        return cls()

    def __init__(self):
        """
        Inicializa a instância da classe.
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
singleton3 = Singleton3.get_instance()
singleton3.some_method()