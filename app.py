import streamlit as st
from core.registry import discover_tools

st.set_page_config(page_title="Swiss Army Knife", page_icon=":material/info_i:")

tools = discover_tools()
categories = sorted({t.category for t in tools})

with st.sidebar:
    category = st.selectbox("Category", categories)
    options = [t for t in tools if t.category == category]
    tool = st.pills(
        "Tool",
        options,
        format_func=lambda t: f"{t.icon} {t.name}",
        selection_mode="single",
        default=options[0],
    )

st.title(f"{tool.icon} {tool.name}")
tool.render()
