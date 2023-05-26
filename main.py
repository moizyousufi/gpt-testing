import os
import openai

def askGPT(txt):
    openai.api_key = "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"

    ''' the following works for chatgpt
    openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Who won the world series in 2020?"},
            {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
            {"role": "user", "content": "Where was it played?"}
        ]
    ) '''


    ''' the following would work for text model, not chatgpt '''
    response = openai.Completion.create(
        engine = 'text-curie-001',
        prompt = txt,
        temperature = 0.6,
        max_tokens = 150,
    ) 

     
    return print(response.choices[0].text.strip())
 
 
def main():
    while True:
        print('GPT: Ask me a question\n')
        myQn = input()

        if myQn == 'STOP':
            break

        askGPT(myQn)

main()
