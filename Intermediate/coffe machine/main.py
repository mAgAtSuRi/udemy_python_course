from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
coffee_maker = CoffeeMaker()
moneymachine = MoneyMachine()

while True:
	print("")
	coffee_maker.report()
	order = input(f"Choose your drink: {menu.get_items()}\n")
	drink = menu.find_drink(order)
	if drink:
		if coffee_maker.is_resource_sufficient(drink):
			print(f"It will be {drink.cost}{moneymachine.CURRENCY}")
			moneymachine.make_payment(drink.cost)
			coffee_maker.make_coffee(drink)
			moneymachine.report()