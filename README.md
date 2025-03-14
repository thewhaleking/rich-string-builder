# rich-string-builder
Text preprocessor for building strings for the rich console


## Background
This came about because I was annoyed at the way we needed to insert text into rich to make it reflect our intended
stylistic choices. Take the following example:

```python
console.print(
    f"Subnet: [{COLOR_PALETTE['GENERAL']['SUBHEADING']}]{netuid_}[/{COLOR_PALETTE['GENERAL']['SUBHEADING']}] "
    f"Stake:\n"
    f"  [blue]{current_stake}[/blue] "
    f":arrow_right: "[{COLOR_PALETTE['STAKE']['STAKE_AMOUNT']}]{new_stake}\n"
)
```

With this library, it's a bit more readable as:
```python
console.print(
    rs.str(
        "Subnet: ", rs.GENERAL.SUBHEADING(netuid_),
        " Stake:\n  ",
        rs.c.blue(current_stake),
        " :arrow_right: ", rs.STAKE.STAKE_AMOUNT(new_stake, "\n")
    )
)
```

The ideas are largely derived from Tailwind and other utility-style frameworks/libraries.

## Current State
Currently this is just proof of concept. I will likely add to this over time.


# Examples
See `examples` directory for examples of using this.
