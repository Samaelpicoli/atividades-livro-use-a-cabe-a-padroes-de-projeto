from templates.caffeine_beverage_with_hook import CaffeineBeverageWithHook


class TeaWithHook(CaffeineBeverageWithHook):
    """
    Classe que representa a preparação de chá utilizando o padrão
    Template Method.

    Esta classe estende a classe abstrata CaffeineBeverageWithHook e
    implementa os métodos necessários para preparar o chá. O
    método prepare_recipe segue o fluxo definido na classe base, enquanto os
    métodos brew e add_condiments são implementados para fornecer a lógica
    específica do chá.

    Além disso, o método customer_wants_condiments permite que o usuário
    escolha se deseja adicionar condimentos, personalizando
    a experiência de preparo do chá.
    """

    def brew(self):
        """Prepara o chá, infundindo as folhas."""
        print('Steeping the tea')


    def add_condiments(self):
        """Adiciona limão ao chá."""
        print('Adding Lemon')


    def customer_wants_condiments(self):
        """Pergunta ao usuário se ele deseja adicionar condimentos."""
        answer = self.get_user_input()
        return answer.lower().startswith("y")


    def get_user_input(self):
        """Obtém a resposta do usuário."""
        answer = input("Would you like lemon with your tea (y/n)? ")
        if answer is None:
            return "no"
        return answer