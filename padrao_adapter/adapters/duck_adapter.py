import random

from abstracts.duck import Duck
from abstracts.turkey import Turkey


class DuckAdapter(Turkey):

    """
    Adapter que permite que um objeto Duck se comporte como um Turkey.

    O padrão Adapter é usado aqui para fazer com que um objeto Duck
    possa ser tratado como um Turkey, adaptando sua interface para
    corresponder à do Turkey. Isso possibilita a reutilização de
    classes existentes em um novo contexto, sem a necessidade de
    modificar suas implementações originais.
    """

    def __init__(self, duck: Duck):
        """Inicializa o adaptador com um objeto Duck.

        Args:
            duck (Duck): O objeto Duck a ser adaptado.
        """
        self.duck = duck
        self.rand = random.Random()


    def gobble(self):
        """Adapta o método quack do Duck para o método gobble do Turkey."""
        self.duck.quack()


    def fly(self):
        """
        Adapta o método de voo do Duck, com uma chance de 20% de
        realmente voar, simulando o comportamento de um Turkey.
        """
        if self.rand.randint(0, 4) == 0:  
            self.duck.fly()