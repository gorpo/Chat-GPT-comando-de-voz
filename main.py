# 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

import os
import openai
openai.api_key = ("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")

# Set the model and prompt
model_engine = "text-davinci-003"
prompt = input('escreva algo: ')

# Set the maximum number of tokens to generate in the response
max_tokens = 1024

# Generate a response
completion = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=max_tokens,
    temperature=0.5,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)

# Print the response
print(completion.choices[0].text)