import os
import openai

### pass the API key
openai.api_key = os.environ.get('OPENAI_API_KEY')


### define the prompt
ourMessages = []
ourMessages.append({'role' : 'system', 'content' : 'you are a therapist, dont just offer solutions, but also sympathize with the user'})
ourMessages.append({'role' : 'user', 'content' : 'why is life so difficult sometimes?'})

try:
    ### make an api call
    response = openai.ChatCompletion.create(
        model = 'gpt-3.5-turbo-16k',
        messages = ourMessages,
        temperature = 1.2
    )

    ### print the response
    # the following would print out all possible responses and all the data associated with the response
    # print(response)

    print(response.choices[0].message.content)
except openai.error.AuthenticationError as e:
    print('No valid token / Authentication Error')
    print(e)
except openai.error.InvalidRequestError as e:
    print('Sorry, but this request is invalid')
    print(e)





'''
This stuff was just initial practicing

def askGPT(txt):
    openai.api_key = "INSERT KEY HERE"

    # the following works for chatgpt
    openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Who won the world series in 2020?"},
            {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
            {"role": "user", "content": "Where was it played?"}
        ]
    )


    # the following would work for text model, not chatgpt
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
'''