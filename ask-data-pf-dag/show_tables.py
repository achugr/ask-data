
from promptflow import tool
from ch_playground import query

@tool
def show_tables() -> str:
    return query("show tables")

