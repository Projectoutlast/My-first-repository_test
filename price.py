
def discounted(price, discount, max_discount = 20):
    price = abs(price)
    discount = abs(discount)
    max_discount = abs(max_discount)
    if max_discount >= 100:
        raise ValueError('Слишком большая скидка')
    if discount >= max_discount:
        return price
    else:
        return price - (price * discount / 100)


def get_summ(one, two, delimiter = '&'):
    one = str(one)
    two = str(two)
    result = f'{one} {delimiter} {two}'
    return result.upper()

def format_price(price):
    price = int(price)
    return f'Цена: {price} руб.'
