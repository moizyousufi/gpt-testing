import os
import openai
import wikipedia

### pass the API key
openai.api_key = os.environ.get('OPENAI_API_KEY')

### get user input
ourTitle = input('Title of the Wikipedia Page: ')

### get the wikipedia content
page = wikipedia.page(title = ourTitle, auto_suggest = False)

### define the prompt
prompt = 'Summarize the following passage: ' + page.content[:10000]
ourMessages = []
ourMessages.append({'role' : 'user', 'content' : prompt})

try:
    ### make an api call
    response = openai.ChatCompletion.create(
        model = 'gpt-3.5-turbo-0301',
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

