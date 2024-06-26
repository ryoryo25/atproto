# 💬 Direct Messages (Chats)

Bluesky Direct Messages were launched on May 22, 2024. It began as a simple chat system for Bluesky users to communicate with one another. Currently, only text messages are supported. 

The Python SDK has supported the Bluesky Direct Messages API since day one. You can use the SDK to send messages to other users, create new conversations, list existing conversations, and perform all other functions available in the mobile app and web client.

The API is not very user-friendly and lacks high-level abstractions. However, thanks to the fully automated process of code generation, it is possible to use Python abstractions for the AT Protocol. Additionally, Bsky proxies requests to the Chat API in an unconventional manner, which adds extra steps to make it work.

## Example

This example demonstrates how to list conversations, create a new conversation, and send a message to it.

```Python
from atproto import Client, IdResolver, models

USERNAME = 'example.com'
PASSWORD = 'hunter2'  # never hardcode your password in a real application


def main() -> None:
    # create resolver instance with in-memory cache
    id_resolver = IdResolver()

    # resolve our DID from a handle
    did = id_resolver.handle.resolve(USERNAME)
    # resolve did document from DID
    did_doc = id_resolver.did.resolve(did)
    # get pds (where our account is hosted) endpoint from DID Document
    pds_url = did_doc.get_pds_endpoint()

    # create client instance with our pds url
    client = Client(base_url=pds_url)
    # login with our username and password
    client.login(USERNAME, PASSWORD)

    convo_list = client.chat.bsky.convo.list_convos()  # use limit and cursor to paginate
    print(f'Your conversations ({len(convo_list.convos)}):')
    for convo in convo_list.convos:
        members = ', '.join(member.display_name for member in convo.members)
        print(f'- ID: {convo.id} ({members})')

    chat_to = id_resolver.handle.resolve('test.marshal.dev')

    # create or get conversation with chat_to
    convo = client.chat.bsky.convo.get_convo_for_members(
        models.ChatBskyConvoGetConvoForMembers.Params(members=[chat_to]),
    )
    print(f'\nConvo ID: {convo.convo.id}')
    print('Convo members:')
    for member in convo.convo.members:
        print(f'- {member.display_name} ({member.did})')

    # send a message to the conversation
    client.chat.bsky.convo.send_message(
        models.ChatBskyConvoSendMessage.Data(
            convo_id=convo.convo.id,
            message=models.ChatBskyConvoDefs.MessageInput(
                text='Hello from Python SDK!',
            ),
        )
    )

    print('\nMessage sent!')


if __name__ == '__main__':
    main()

```
