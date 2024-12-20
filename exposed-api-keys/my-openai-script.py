import openai

# Set your OpenAI API key (synthetic example key)
openai.api_key = "sk-1234567890abcdef1234567890abcdef"

# Define a prompt
prompt = "Write a short poem about the stars."

# Make a request to the OpenAI API
response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=prompt,
    max_tokens=50
)

# Print the response
print(response.choices[0].text.strip())
