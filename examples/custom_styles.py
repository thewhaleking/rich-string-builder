from rich_string_builder.string_builder import RichStyles

COLOR_PALETTE = {
    "GENERAL": {
        "HEADER": "#4196D6",  # Light Blue
        "LINKS": "#8CB9E9",  # Sky Blue
        "HINT": "#A2E5B8",  # Mint Green
        "COLDKEY": "#9EF5E4",  # Aqua
        "HOTKEY": "#ECC39D",  # Light Orange/Peach
    },
    "alert": "blink yellow",
}


def custom_style_examples():
    # You can create a RichStyles object with custom definitions like so
    rs = RichStyles(COLOR_PALETTE)
    expected = ">>[bold][#4196D6]Hello, [/#4196D6][#A2E5B8]World![/#A2E5B8][/bold]"
    actual = rs.str(
        ">>",
        rs.s.bold(
            rs.custom.GENERAL.HEADER("Hello, "), rs.custom.GENERAL.HINT("World!")
        ),
    )
    assert expected == actual
    expected = "[blink yellow]ALERT![/blink yellow]"
    actual = rs.custom.alert("ALERT!")
    assert expected == actual


if __name__ == "__main__":
    custom_style_examples()
