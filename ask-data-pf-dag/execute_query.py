from promptflow import tool
import chdb
import re


@tool
def execute_query(query: str, table_name: str) -> str:
    table_name_pattern = rf"([\"'`]?)(default\.)?{table_name}\1"
    remote_table_name = f"remoteSecure('play.clickhouse.com', default, {table_name}, 'play', 'play')"
    remote_table_query = re.sub(table_name_pattern, remote_table_name, query) 
    print(f"Remote table query {remote_table_query}")
    # no special reason for using chdb here now
    ret = chdb.query(remote_table_query, "CSVWithNames")
    return str(ret)