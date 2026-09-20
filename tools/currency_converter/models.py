from dataclasses import dataclass


@dataclass(frozen=True)
class ConversionResult:
    amount: float
    from_currency: str
    to_currency: str
    rate: float
    converted_amount: float
    date: str
