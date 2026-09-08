def calculate_discount(price: int = 100, discount: int = 0) -> float:
    final_price = price * (1 - discount / 100)
    return final_price


def is_even(number: int = 2) -> bool:
    result = number % 2 == 0
    return result


def get_full_name(first_name: str = "", last_name :str = "") -> str:
    full_name =f"{first_name.capitalize()} {last_name.capitalize()}"
    return full_name
