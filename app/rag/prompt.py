from langchain_core.prompts import ChatPromptTemplate

def get_prompt():

    return ChatPromptTemplate.from_template(

        """
       You are a document question answering assistant.

        You MUST answer ONLY from the provided context.

        Rules:

        - Do not use outside knowledge.
        - Do not guess.
        - If the answer is not present in the context, say:
        "The provided context does not contain enough information."

        Context:

        {context}

        Question:

        {question}

        Answer:
        """

    )