## Installation

Install requirements

```shell
pip install -r requirements.txt
```

Add openai key

```shell
pf connection create -f openai.yaml --set api_key=YOUR_OPENAI_KEY
```

Install promptflow VS Code [extension](https://marketplace.visualstudio.com/items?itemName=prompt-flow.prompt-flow).

Start the chat 

```shell
pf flow serve --source . --port 8080 --host localhost
```