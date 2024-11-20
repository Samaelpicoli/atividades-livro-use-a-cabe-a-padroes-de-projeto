from objects.coffee import Coffee
from objects.coffee_with_hook import CoffeeWithHook
from objects.tea import Tea
from objects.tea_with_hook import TeaWithHook


my_tea = Tea()
my_coffee = Coffee()

print('Making Tea...')
my_tea.prepare_recipe()
print('')

print('Making Coffee...')
my_coffee.prepare_recipe()
print('')

my_tea_hook = TeaWithHook()
my_coffee_hook = CoffeeWithHook()

print('Making Tea...')
my_tea_hook.prepare_recipe()
print('')

print('Making Coffee...')
my_coffee_hook.prepare_recipe()
print('')
