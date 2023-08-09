from fastapi import FastAPI
from scripts.core.member import userRouter
from scripts.core.projects import projectRouter
from scripts.core.tasks import taskRouter
app = FastAPI()

app.include_router(userRouter)
app.include_router(projectRouter)
app.include_router(taskRouter)