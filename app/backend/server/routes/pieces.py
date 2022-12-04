from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from ..database.database import (
    add_piece,
    delete_piece,
    retrieve_pieces,
    retrieve_piece,
    update_piece,
)
from ..database.models.pieces import (
    ErrorResponseModel,
    ResponseModel,
    PieceSchema,
    PieceUpdateModel,
)

router = APIRouter()


@router.post("/", response_description="Piece added into the database")
async def add_piece_data(piece: PieceSchema = Body(...)):
    piece = jsonable_encoder(piece)
    new_piece = await add_piece(piece)
    return ResponseModel(new_piece, "Piece added successfully.")


@router.get("/", response_description="Pieces retrieved")
async def get_pieces():
    pieces = await retrieve_pieces()
    if pieces:
        return ResponseModel(pieces, "Pieces data retrieved successfully")
    return ResponseModel(pieces, "Empty list returned")


@router.get("/{id}", response_description="Piece data retrieved")
async def get_piece(id):
    piece = await retrieve_piece(id)
    if piece:
        return ResponseModel(piece, "Piece data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "Piece doesn't exist.")


@router.put("/{id}")
async def update_patient_data(id: str, req: PieceUpdateModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_piece = await update_piece(id, req)
    if updated_piece:
        return ResponseModel(
            "Piece with ID: {} name update is successful".format(id),
            "Piece name updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the piece data.",
    )


@router.delete("/{id}", response_description="Piece data deleted from the database")
async def delete_piece_data(id: str):
    deleted_piece = await delete_piece(id)
    if deleted_piece:
        return ResponseModel(
            "Piece with ID: {} removed".format(id), "Piece deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "Piece with id {0} doesn't exist".format(id)
    )
