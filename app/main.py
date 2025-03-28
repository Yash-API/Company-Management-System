from fastapi import FastAPI
from app.database import engine, Base
from app.routers import auth, employees, clients, chatbot  # Import the chatbot router

# from app.utils.nlp_utils import llm  # Import llm to check its status

app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

# Initialize FastAPI app
app = FastAPI(title="Company Management System API")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Frontend URL
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)


# Create database tables
Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(employees.router, prefix="/employees", tags=["Employees"])
app.include_router(clients.router, prefix="/clients", tags=["Clients"])
app.include_router(chatbot.router, prefix="/api")


# @app.post("/chatbot/")
# async def chatbot_endpoint(query: str):
#     response = chatbot_response(query)
#     return {"response": response}


@app.get("/")
def root():
    return {"message": "Welcome to the Company Management System API!"}
