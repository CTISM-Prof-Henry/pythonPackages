import random
import re


def roll(dice: str) -> int:
    """
    Rola dados no formato NdX+M.

    Exemplos:
        d6
        2d6
        1d20+5
        3d8-2
    """

    pattern = r"^(\d*)d(\d+)([+-]\d+)?$"

    match = re.fullmatch(pattern, dice.lower())

    if not match:
        raise ValueError(
            "Formato inválido. Use, por exemplo: d6, 2d6, 1d20+3."
        )

    number_of_dice = int(match.group(1) or 1)
    sides = int(match.group(2))
    modifier = int(match.group(3) or 0)

    if number_of_dice < 1:
        raise ValueError("A quantidade de dados deve ser maior que zero.")

    if sides < 2:
        raise ValueError("Um dado deve possuir pelo menos 2 lados.")

    results = [
        random.randint(1, sides)
        for _ in range(number_of_dice)
    ]

    return sum(results) + modifier