from src.string_builder import RichStyles

COLOR_PALETTE = {
    "GENERAL": {
        "HEADER": "#4196D6",  # Light Blue
        "LINKS": "#8CB9E9",  # Sky Blue
        "HINT": "#A2E5B8",  # Mint Green
        "COLDKEY": "#9EF5E4",  # Aqua
        "HOTKEY": "#ECC39D",  # Light Orange/Peach
        "SUBHEADING_MAIN": "#7ECFEC",  # Light Cyan
        "SUBHEADING": "#AFEFFF",  # Pale Blue
        "SUBHEADING_EXTRA_1": "#96A3C5",  # Grayish Blue
        "SUBHEADING_EXTRA_2": "#6D7BAF",  # Slate Blue
        "CONFIRMATION_Y_N_Q": "#EE8DF8",  # Light Purple/Pink
        "SYMBOL": "#E7CC51",  # Gold
        "BALANCE": "#4F91C6",  # Medium Blue
        "COST": "#53B5A0",  # Teal
        "SUCCESS": "#53B5A0",  # Teal
        "NETUID": "#CBA880",  # Tan
        "NETUID_EXTRA": "#DDD5A9",  # Light Khaki
        "TEMPO": "#67A3A5",  # Grayish Teal
    },
    "STAKE": {
        "STAKE_AMOUNT": "#53B5A0",  # Teal
        "STAKE_ALPHA": "#53B5A0",  # Teal
        "STAKE_SWAP": "#67A3A5",  # Grayish Teal
        "TAO": "#4F91C6",  # Medium Blue
        "SLIPPAGE_TEXT": "#C25E7C",  # Rose
        "SLIPPAGE_PERCENT": "#E7B195",  # Light Coral
        "NOT_REGISTERED": "#EB6A6C",  # Salmon Red
        "EXTRA_1": "#D781BB",  # Pink
    },
    "POOLS": {
        "TAO": "#4F91C6",  # Medium Blue
        "ALPHA_IN": "#D09FE9",  # Light Purple
        "ALPHA_OUT": "#AB7CC8",  # Medium Purple
        "RATE": "#F8D384",  # Light Orange
        "TAO_EQUIV": "#8CB9E9",  # Sky Blue
        "EMISSION": "#F8D384",  # Light Orange
        "EXTRA_1": "#CAA8FB",  # Lavender
        "EXTRA_2": "#806DAF",  # Dark Purple
    },
    "GREY": {
        "GREY_100": "#F8F9FA",  # Almost White
        "GREY_200": "#F1F3F4",  # Very Light Grey
        "GREY_300": "#DBDDE1",  # Light Grey
        "GREY_400": "#BDC1C6",  # Medium Light Grey
        "GREY_500": "#5F6368",  # Medium Grey
        "GREY_600": "#2E3134",  # Medium Dark Grey
        "GREY_700": "#282A2D",  # Dark Grey
        "GREY_800": "#17181B",  # Very Dark Grey
        "GREY_900": "#0E1013",  # Almost Black
        "BLACK": "#000000",  # Pure Black
    },
    "SUDO": {
        "HYPERPARAMETER": "#4F91C6",  # Medium Blue
        "VALUE": "#D09FE9",  # Light Purple
        "NORMALIZED": "#AB7CC8",  # Medium Purple
    },
}


def custom_style_examples():
    rs = RichStyles(COLOR_PALETTE)
    expected = "[bold][#5F6368]Hello, [/#5F6368][#0E1013]World![/#0E1013][/bold]"
    actual = rs.str(
        rs.s.bold(rs.custom.GREY.GREY_500("Hello, "), rs.custom.GREY.GREY_900("World!"))
    )
    assert expected == actual
