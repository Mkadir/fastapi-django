import logging
from typing import List

from fastapi import APIRouter
from .schemes import DemoUserBase, DemoUserDisplay
from .models import DemoUsers
from starlette.responses import JSONResponse
app = APIRouter(prefix='/users', tags=['demo'])


@app.post(path='/add-user')
def add_user_func(request: DemoUserBase):
    try:
        user = DemoUsers(
            username=request.username,
            age=request.age
        )
        user.save()
        return user
    except Exception as e:
        print(e)


@app.get('/get-users', response_model=List[DemoUserDisplay])
def get_user_func():
    try:
        users = DemoUsers.objects.all()
        return [{
            'username': user.username,
            'age': user.age
        } for user in users]
    except Exception as e:
        return JSONResponse(
            status_code=404,
            content={
                'error': 'Something went wrong'
            }
        )
