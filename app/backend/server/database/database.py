import motor.motor_asyncio
from bson.objectid import ObjectId


MONGO_DETAILS = "mongodb://localhost:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.music

pieces_collection = database.get_collection("pieces")


async def retrieve_pieces():
    pieces = []
    async for piece in pieces_collection.find():
        pieces.append(pieces_helper(piece))
    return pieces


async def add_piece(piece_data: dict) -> dict:
    piece = await pieces_collection.insert_one(piece_data)
    new_piece = await pieces_collection.find_one({"_id": piece.inserted_id})

    return pieces_helper(new_piece)


async def retrieve_piece(id: str) -> dict:
    piece = await pieces_collection.find_one({"_id": ObjectId(id)})
    if piece:
        return pieces_helper(piece)


async def update_piece(id: str, data: dict):
    if len(data) < 1:
        return False
    piece = await pieces_collection.find_one({"_id": ObjectId(id)})
    if piece:
        updated_piece = await pieces_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )

        if updated_piece:
            return True
        return False


async def delete_piece(id: str):
    piece = await pieces_collection.find_one({"_id": ObjectId(id)})
    if piece:
        piece.delete_one({"_id": ObjectId(id)})
        return True


def pieces_helper(piece) -> dict:
    return {
        "id": str(piece["_id"]),
        "title": piece["title"],
        "composer": piece["composer"],
        "genre": piece["genre"],
    }
