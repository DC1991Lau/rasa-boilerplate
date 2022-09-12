from bson.objectid import ObjectId
import motor.motor_asyncio

MONGO_DETAILS = "mongodb://mongo1:30001,mongo2:30002,mongo3:30003/?replicaSet=rasa-mongo-replica-set"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.rasa

logs_collection = database.get_collection("conversations")


# helpers


def log_helper(log) -> dict:
    return {
        "logs": log["events"]
    }

 
# Retrieve all events present in the database
async def retrieve_logs():
    temp_logs = []
    keyValList=['user']
    new_logs = []
    logs = []
    async for log in logs_collection.find():
        events = log['events']
        temp_logs = [d for d in events if d['event'] in keyValList]
        for i in temp_logs:
            if i['text'] not in new_logs:
                new_logs.append(i['text'])
                logs.append(i)

    return logs