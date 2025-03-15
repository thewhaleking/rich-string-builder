from src.string_builder import RichStyles


def combinations():
    rs = RichStyles()
    bright_yellow = rs.Styles.bright + rs.Colors.yellow
    expected = "[bright yellow]Hello, World![/bright yellow]"
    actual = bright_yellow("Hello, World!")
    assert actual == expected
