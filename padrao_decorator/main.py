from beverage.beverage import Beverage
from coffees.coffee import DarkRoast, Espresso, HouseBlend
from condiments.condiments import Mocha, Soy, Whip


def round_value(value):
    return round(value, 2)

def main():
    print("TALL SIZE")
    
    beverage = Espresso()
    beverage.set_size(Beverage.Size.TALL)
    print(f"{beverage.get_description()} ${round_value(beverage.cost())}")

    beverage2 = DarkRoast()
    beverage2.set_size(Beverage.Size.TALL)
    beverage2 = Mocha(beverage2)
    beverage2 = Mocha(beverage2)
    beverage2 = Whip(beverage2)
    print(f"{beverage2.get_description()} ${round_value(beverage2.cost())}")

    beverage3 = HouseBlend()
    beverage3.set_size(Beverage.Size.TALL)
    beverage3 = Soy(beverage3)
    beverage3 = Mocha(beverage3)
    beverage3 = Whip(beverage3)
    print(f"{beverage3.get_description()} ${round_value(beverage3.cost())}")

    print("\nGRANDE SIZE")
    
    beverage = Espresso()
    beverage.set_size(Beverage.Size.GRANDE)
    print(f"{beverage.get_description()} ${round_value(beverage.cost())}")

    beverage2 = DarkRoast()
    beverage2.set_size(Beverage.Size.GRANDE)
    beverage2 = Mocha(beverage2)
    beverage2 = Mocha(beverage2)
    beverage2 = Whip(beverage2)
    print(f"{beverage2.get_description()} ${round_value(beverage2.cost())}")

    beverage3 = HouseBlend()
    beverage3.set_size(Beverage.Size.GRANDE)
    beverage3 = Soy(beverage3)
    beverage3 = Mocha(beverage3)
    beverage3 = Whip(beverage3)
    print(f"{beverage3.get_description()} ${round_value(beverage3.cost())}")

    print("\nVENTI SIZE")
    
    beverage = Espresso()
    beverage.set_size(Beverage.Size.VENTI)
    print(f"{beverage.get_description()} ${round_value(beverage.cost())}")

    beverage2 = DarkRoast()
    beverage2.set_size(Beverage.Size.VENTI)
    beverage2 = Mocha(beverage2)
    beverage2 = Mocha(beverage2)
    beverage2 = Whip(beverage2)
    print(f"{beverage2.get_description()} ${round_value(beverage2.cost())}")

    beverage3 = HouseBlend()
    beverage3.set_size(Beverage.Size.VENTI)
    beverage3 = Soy(beverage3)
    beverage3 = Mocha(beverage3)
    beverage3 = Whip(beverage3)
    print(f"{beverage3.get_description()} ${round_value(beverage3.cost())}")

if __name__ == "__main__":
    main()