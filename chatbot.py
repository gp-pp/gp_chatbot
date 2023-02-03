from fastapi import FastAPI, Request, routing
from mongodb import db_connection
import openai

# Load your API key from an environment variable or secret management service
openai.api_key = "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"


app = FastAPI()

@app.post("/")
async def input(request: Request):

    request = await request.json()
    req_prompt = request.get('prompt')
    userID = request.get('userid')

    user_chatbot = db_connection()

    list_of_users = []

    for x in user_chatbot.find():
        list_of_users.append(x.get('userid'))

    if userID not in list_of_users:
        print(userID)
        req_prompt = request.get('prompt')

        response = openai.Completion.create(
        model="text-davinci-003",
        prompt= req_prompt,
        temperature=0,
        max_tokens=100,
        )

        res = response.get('choices')[0].get('text')

        user_dict = {'userid': userID, 'prompt': "Q) {}, A) {} \n".format(req_prompt, res)}

        user_chatbot.insert_one(user_dict)

        return res

    else:
        x = user_chatbot.find({'userid':userID})
        req_prompt = request.get('prompt')
        prev_prompt = x[0].get('prompt')
        
        new_prompt = prev_prompt + 'Q)' + req_prompt

        response = openai.Completion.create(
        model="text-davinci-003",
        prompt= new_prompt,
        temperature=0,
        max_tokens=100,
        )

        res = response.get('choices')[0].get('text')

        user_dict = {'userid': userID, 'prompt': "{}, A) {} \n".format(new_prompt, res)}
        user_chatbot.delete_one({'userid':userID})
        user_chatbot.insert_one(user_dict) 

        return res




    # print(list_of_users)

    response = openai.Completion.create(
    model="text-davinci-003",
    prompt= req_prompt,
    temperature=0,
    max_tokens=10,
    )
                             
    # print(response.get('choices')[0].get('text'))

    # print(request)
    return {"message": "hello"}