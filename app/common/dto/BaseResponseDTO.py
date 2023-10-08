from pydantic import BaseModel, Field

class BaseResponseDTO(BaseModel):
    code: int = Field(..., example= 200)
    status: str = Field(..., example= "OK")
    message: str = Field(..., example= "Success transaction")
    idTransaction: str = Field(..., example= "f51c10e0-6136-43c6-b4b8-52cd34d86e06")
    data: list = Field(..., example= {"ID": 1, "Name":"Lina Leal"})

    def serialize(self):
        return {
            'code': self.code,
            'status' : self.status,
            'message' : self.message,
            'idTransaction': self.idTransaction,
            'data': self.data
        }

    class Config:
        orm_mode = True