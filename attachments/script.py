from motor import motor_asyncio
import config
import pprint
import asyncio
import aioredis

loop = asyncio.get_event_loop()
client = motor_asyncio.AsyncIOMotorClient(config.MONGO_CONNECTION['host'], config.MONGO_CONNECTION['port'])
guidebox_collection = client.ozone.guidebox_program_details


async def get_and_queue_programs():
    redis = await aioredis.create_redis(config.REDIS_CONNECTION, loop=loop)
    cursor = guidebox_collection.find().limit(50)
    async for document in cursor:
        print("{0} -- {1}".format(document['show_type'], document.get('gb_id', 0)))
        await redis.rpush('gb', "{0}-{1}".format(document.get('gb_id', 0), document['show_type']))


loop.run_until_complete(get_and_queue_programs())
