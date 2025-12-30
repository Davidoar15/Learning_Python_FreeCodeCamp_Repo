def verify_card_number(card_number):
    cleaned = ""
    for char in card_number:
        if char.isdigit():
            cleaned += char

    digits = [int(digit) for digit in cleaned]

    total = 0
    for i in range(len(digits) - 1, -1, -1):
        value = digits[i]

        position_from_right = len(digits) - 1 - i

        if position_from_right % 2 == 1:
            value *= 2
            if value > 9:
                value -= 9

        total += value

    if total % 10 == 0: return "VALID!"
    else: return "INVALID!"
