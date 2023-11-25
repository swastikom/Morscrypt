from enum import Enum
from fastapi import APIRouter
from pydantic import BaseModel
from functions.final import morse_encryption_func

router = APIRouter()

class Tags(Enum):
    message_encrypt_route = "Encryption Route"

class message_to_encrypt(BaseModel):
    message: str

@router.post("/morsecryption",tags=[Tags.message_encrypt_route])
async def morsecrypt(request_data: message_to_encrypt):
    morse_encrypted_message = morse_encryption_func(request_data.message)
    return {"message": morse_encrypted_message}