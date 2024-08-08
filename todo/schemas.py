from ninja import ModelSchema
from .models import User,Todo
from pydantic import BaseModel


class UserSchema(ModelSchema):
    class Config:
        model = User
        model_fields = ['id', 'username', 'email']


class SignInSchema(BaseModel):
    email: str
    password: str


class TodoSchema(ModelSchema):
    class Config:
        model = Todo
        model_fields = ['id', 'description', 'is_completed']