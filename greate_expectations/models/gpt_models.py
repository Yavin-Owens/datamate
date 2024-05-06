from dotenv import load_dotenv, find_dotenv
import openai
import os
load_dotenv(find_dotenv())
openai.api_key  = os.environ.get("OPENAI_API_KEY")


def naturallanguagetoexpectation(sentence):
    """
    Convert Natural Language Query to GE expectation rules with finetuned GPT3 llm
    """
    ftmodel = "gpt-4" #update with your model
    prompt = f"{sentence}\n\n###\n\n"
    response = openai.Completion.create(
    model=ftmodel,
    prompt=prompt,
    temperature=0.3,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
    stop= [" STOP"]
    )
    return response['choices'][0]['text']