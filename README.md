# Ask data

Ask data is a project for asking structured data in a natural language.

## Quickstart

The easiest way to give it a try is to [![open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/achugr/ask-data)

There is a free quota, open the codespace, once loaded do this in the terminal:

```shell
cd ask-data-pf-dag
pip install -r requirements.txt
pf connection create -f openai.yaml --set api_key=YOUR_OPENAI_KEY
pf flow serve --source . --port 8080 --host localhost
```

This will start the simple chat where you could ask the data in a natural language. Please remember that you pay for the
LLM API.

## Data source

The project uses [ClickHouse playground](https://play.clickhouse.com/play?user=play) as a data source, because it's
free, fast and easy to use, plus it has variety of datasets from different areas.

Here are some examples of the queries you may ask:

- What's the top five most expensive apartments in the UK?
- What are the months when COVID is most dangerous?
- What is the average length of the taxi trip?
- Who made the most of the contributions to ClickHouse/ClickHouse in the summer 2021
- ...

## Ask data with [promptflow](https://github.com/microsoft/promptflow)

### [DAG](https://microsoft.github.io/promptflow/concepts/concept-flows.html#dag-flow)

DAG (Directed Acyclic Graph) is a simple and natural way to describe a flow for solving a problem.
Promptflow gives us an easy way to build/debug/run/evaluate the flow.

Follow the installation [instructions](./ask-data-pf-dag/README.md).

The flow definition looks like this.
![dag.png](assets/dag.png)

Ask questions in the chat.
![chat-example.png](assets/chat-example.png)


