from llama_index.llms.ollama import Ollama
from llama_index.core.agent import ReActAgent

llm = Ollama(model="phi3", request_timeout=100)

agent = ReActAgent.from_llm(llm=llm)

response = agent.chat("Olá voce entende portugues?")

print(response)



