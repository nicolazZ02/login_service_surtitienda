from pydantic import BaseModel, Field

class MessagesResponseDTO(BaseModel):
        
        title: str = Field(..., example="success!")
        message: str = Field(..., example="Success transaction")
        status: str = Field(..., example="success")
            
        def serialize(self):
            return {
                'title': self.title,
                'message': self.message,
                'status': self.status
            }
        
        class Config:
            orm_mode = True