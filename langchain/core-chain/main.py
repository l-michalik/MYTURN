import os
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.schema import StrOutputParser

# 1️⃣ Załaduj klucz API
load_dotenv()

# 2️⃣ Utwórz prompt
prompt = PromptTemplate.from_template("Wyjaśnij pojęcie '{pojecie}' w maksymalnie 3 zdaniach po polsku.")

# 3️⃣ Zdefiniuj model
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

# 4️⃣ Połącz w pipeline (LCEL)
chain = prompt | llm | StrOutputParser()

# 5️⃣ Uruchom chain
pojecie = input("Podaj pojęcie do wyjaśnienia: ")
result = chain.invoke({"pojecie": pojecie})

print("\n📘 Wyjaśnienie:")
print(result)
