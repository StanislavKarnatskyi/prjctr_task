secret_formula = '''	1.	Bun: Sesame seed bun or a plain bun.
	2.	Patty: Beef, veggie, or a special “secret” blend patty.
	3.	Lettuce: Crisp iceberg or romaine.
	4.	Tomato: Sliced fresh tomatoes.
	5.	Cheese: American, cheddar, or a special cheese blend.
	6.	Pickles: Sliced dill pickles.
	7.	Onions: Sliced onions or caramelized onions.
	8.	Ketchup: A classic burger condiment.
	9.	Mustard: Yellow or Dijon mustard.
	10.	Secret Sauce: A special blend of mayonnaise, relish, and spices.
	11.	Special Seasonings: A proprietary blend of spices and herbs.
	12.	Seaweed: For a nautical twist, inspired by the underwater setting.'''


def is_admin(func):
    def wrapper(**kwargs):
        func(**kwargs)
        if kwargs['user_type'] == 'user':
            raise ValueError('Permission denied')
        elif kwargs['user_type'] == 'admin':
            print('Access is allowed')
            print(secret_formula)
        else:
            raise ValueError('Unknown value')
    return wrapper

@is_admin
def show_customer_receipt(user_type: str):
    print('Checking access...')

show_customer_receipt(user_type='user')
show_customer_receipt(user_type='admin')