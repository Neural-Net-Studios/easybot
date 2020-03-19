import vk_api


token = 'токен'

vk=vk_api.VkApi(token=token)
vk._auth_token()


data = {
    'offset':0,
    'count':20,
    'filter':'unanswered'
}


while True:
    messages = vk.method('messages.getConversations', data)
    if messages['count']>=1:
        print(messages)
        id = messages['items'][0]['last_message']['from_id']
        text = messages['items'][0]['last_message']['text']
        if text.lower() == 'привет':
            vk.method('messages.send', {'peer_id':id, 'random_id':0, 'message': 'Здравствуй!'})
        else:
            vk.method('messages.send', {'peer_id':id, 'random_id':0, 'message': 'ERROR'})
