from transformers import pipeline as transformers_pipeline


def perform_qa(question, context):
    nlp_pipeline = transformers_pipeline("question-answering")
    result = nlp_pipeline(question=question, context=context)
    return result["answer"]
