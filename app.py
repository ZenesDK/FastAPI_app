from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
from models import User, UserAge, UserAgeResponse, Feedback

app = FastAPI()

# --- Задание 1.3 ---
# Модель для запроса /calculate
class CalculateRequest(BaseModel):
    num1: float
    num2: float

# --- Задание 1.4: Создаем экземпляр пользователя ---
user_data = User(name="Даниил Кайзер", id=1)

# --- Задание 2.1 ---
feedbacks_db = []

# --- Задание 1.1 ---
@app.get("/")
async def read_root():
    return {"message": "Авторелоад действительно работает"}

# --- Задание 1.2 ---
@app.get("/html", response_class=FileResponse)
async def get_html_page():
    return "index.html"

# --- Задание 1.3 ---
@app.post("/calculate")
async def calculate_sum(data: CalculateRequest):
    result = data.num1 + data.num2
    return {"result": result}

# --- Задание 1.4 ---
@app.get("/users", response_model=User)
async def get_user():
    return user_data

# --- Задание 1.5 ---
@app.post("/user", response_model=UserAgeResponse)
async def check_user_adult(user: UserAge):
    user_response = user.dict()
    user_response["is_adult"] = user.age >= 18
    return user_response

# --- Задание 2.1 ---
@app.post("/feedback")
async def create_feedback(feedback: Feedback):
    feedbacks_db.append(feedback)
    return {"message": f"Feedback received. Thank you, {feedback.name}."}

# --- Задание 2.2 --- 
@app.post("/feedback2")
async def create_feedback_v2(feedback: Feedback):
    feedbacks_db.append(feedback)
    return {"message": f"Спасибо, {feedback.name}! Ваш отзыв сохранён."}