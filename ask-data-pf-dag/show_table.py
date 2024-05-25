from promptflow import tool
from ch_playground import query

@tool
def show_table(table_name: str) -> str:
    return query(f"show create table {table_name}")
