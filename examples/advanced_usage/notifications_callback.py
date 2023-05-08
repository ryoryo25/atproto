import asyncio
from datetime import datetime, timezone

from atproto import AsyncClient

# how often we should check for new notifications
FETCH_NOTIFICATIONS_DELAY_SEC = 3.0


async def main():
    async_client = AsyncClient()
    await async_client.login('my-handle', 'my-password')

    async def on_notification_callback(notification):
        print(f'Got new notification! Type: {notification.reason}; from: {notification.author.did}')
        # example: "Got new notification! Type: like; from: did:plc:hlorqa2iqfooopmyzvb4byaz"

    async def listen_for_notifications(on_notification):
        print('Start listening for notifications...')
        while True:
            # save the time in UTC when we fetch notifications
            last_seen_at = datetime.now(timezone.utc).isoformat()

            # fetch new notifications
            response = await async_client.bsky.notification.list_notifications()

            # create task list to run callbacks concurrently
            on_notification_tasks = []
            for notification in response.notifications:
                if not notification.isRead:
                    on_notification_tasks.append(on_notification(notification))

            # run callback on each notification
            await asyncio.gather(*on_notification_tasks)

            # mark notifications as processed (isRead=True)
            await async_client.bsky.notification.update_seen({'seenAt': last_seen_at})
            print('Successfully process notification. Last seen at:', last_seen_at)

            await asyncio.sleep(FETCH_NOTIFICATIONS_DELAY_SEC)

    # run our notification listener and register the callback on notification
    await asyncio.ensure_future(listen_for_notifications(on_notification_callback))


if __name__ == '__main__':
    # use run() for higher Python version
    asyncio.get_event_loop().run_until_complete(main())