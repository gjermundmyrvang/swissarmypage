import streamlit as st

from core.base_tool import BaseTool
from core.errors import ToolError

from .client import convert, get_currencies


class CurrencyConverterTool(BaseTool):
    name = "Currency Converter"
    icon = ":material/currency_exchange:"
    category = "Finance"

    def render(self) -> None:
        col1, col2, col3 = st.columns(3)

        currencies = get_currencies()

        with col1:
            amount = st.number_input("Amount", min_value=0.0, value=100.0)
        with col2:
            from_currency = st.selectbox("From", currencies, index=0)
        with col3:
            to_currency = st.selectbox("To", currencies, index=1)

        try:
            result = convert(amount, from_currency, to_currency)
        except ToolError as e:
            st.error(str(e))
            return

        st.metric(
            f"{result.amount:,.2f} {result.from_currency} =",
            f"{result.converted_amount:,.2f} {result.to_currency}",
        )
        st.caption(
            f"1 {result.from_currency} = {result.rate:.4f} {result.to_currency} (as of {result.date})"
        )
