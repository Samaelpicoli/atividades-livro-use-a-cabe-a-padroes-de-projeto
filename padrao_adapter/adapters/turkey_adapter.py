from abstracts.duck import Duck
from abstracts.turkey import Turkey


class TurkeyAdapter(Duck):
    
    """
    Adapter que permite que um objeto Turkey se comporte como um Duck.

    O padrão Adapter é utilizado para permitir que um objeto Turkey
    seja utilizado onde um Duck é esperado, adaptando a interface 
    do Turkey para a do Duck. Isso facilita a integração de classes
    com interfaces incompatíveis, permitindo que trabalhem juntas
    sem a necessidade de modificar suas implementações originais.
    """

    def __init__(self, turkey: Turkey):
        """Inicializa o adaptador com um objeto Turkey.

        Args:
            turkey (Turkey): O objeto Turkey a ser adaptado.
        """
        self.turkey = turkey


    def quack(self):
        """Adapta o método quack para chamar o método gobble do Turkey."""
        self.turkey.gobble()


    def fly(self):
        """
        Adapta o método fly para chamar o método fly do Turkey cinco vezes.
        """
        for i in range(5):
            self.turkey.fly()