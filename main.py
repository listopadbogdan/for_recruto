from fastapi import FastAPI, Response

from typing import Optional

import uvicorn

app = FastAPI()


@app.get('/')
async def hello_page(name: Optional[str] = '', message: Optional[str] = ''):
    return Response(
        f'Hello, {name}! '
        f'{message}!', media_type='text/html'
    )


if __name__ == '__main__':
    print('Запускаем сервер!')
    uvicorn.run('main:app', reload=True)
    
