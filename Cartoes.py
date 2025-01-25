#Visa = inicio 4
#Mastercard = inicio 51 e 55 ou entre 2221 e 2720
#American Express = inicio 34 ou 37
#elo = inicio 4011, 4312 ou 4389
#hipercard = inicio 6062
#discover = 6011 ou 65 ou 644 a 649
def get_card_brand(card_number):
    card_number = str(card_number)
    if card_number.startswith('4'):
        return 'Visa'
    elif card_number.startswith(('51', '52', '53', '54', '55')) or 2221 <= int(card_number[:4]) <= 2720:
        return 'Mastercard'
    elif card_number.startswith(('34', '37')):
        return 'American Express'
    elif card_number.startswith(('4011', '4312', '4389')):
        return 'Elo'
    elif card_number.startswith('6062'):
        return 'Hipercard'
    elif card_number.startswith('6011') or card_number.startswith('65') or 644 <= int(card_number[:3]) <= 649:
        return 'Discover'
    else:
        return 'Unknown'

# Example usage
card_number = int(input("Digite Aqui o numero do seu cartão: "))
print(get_card_brand(card_number))  # Output: Elo