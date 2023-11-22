from langchain.llms import CTransformers

llm = CTransformers(
    model="llama-2-7b-chat.ggmlv3.q2_K.bin",
    model_type="llama"
)

# 첫 번째 문장에 따라서 글을 작성해준다.
first_sentence = 'Let me introduce myself to you.'
result = llm.predict(first_sentence)

print(result)