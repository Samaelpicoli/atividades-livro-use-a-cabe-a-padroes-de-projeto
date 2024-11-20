from adapters.turkey_adapter import TurkeyAdapter
from objects.mallard_duck import MallardDuck
from objects.wild_turkey import WildTurkey


mallard_duck = MallardDuck()

wild_turkey = WildTurkey()
turkey_adapter = TurkeyAdapter(wild_turkey)

print('')
print('The Turkey says...')
wild_turkey.gobble()
wild_turkey.fly()


print('')
print('The Duck says...')
mallard_duck.quack()
mallard_duck.fly()

print('')
print('The TurkeyAdapter says...')
turkey_adapter.quack()
turkey_adapter.fly()