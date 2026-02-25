from pydantic import BaseModel, Field, field_validator
import re

# --- Задание 1.4 ---
class User(BaseModel):
    name: str
    id: int

# --- Задание 1.5 ---
class UserAge(BaseModel):
    name: str
    age: int

# Модель для ответа, включающая is_adult
class UserAgeResponse(UserAge):
    is_adult: bool

# --- Задание 2.1 ---
class Feedback(BaseModel):
    name: str
    message: str

# --- Задание 2.2 ---
class Feedback(BaseModel):
    name: str = Field(..., min_length=2, max_length=50, description="Имя пользователя, от 2 до 50 символов")
    message: str = Field(..., min_length=10, max_length=500, description="Сообщение, от 10 до 500 символов")

    @field_validator('message')
    @classmethod
    def check_bad_words(cls, v: str) -> str:
        lower_message = v.lower()
        bad_words = ["кринж", "рофл", "вайб"]

        for word in bad_words:
            # \b - это граница слова
            if re.search(rf'\b{word}\b', lower_message):
                raise ValueError('Использование недопустимых слов')
        return v