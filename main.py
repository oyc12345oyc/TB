from fastapi import FastAPI
from skin import skin


# uvicorn main:app --reload

app=FastAPI()

# @app.get("/")
# def home():
#     return 'This is Home'

# @app.get("/test")
# def home():
#     return 'This is Test'
    
@app.get("/skin/{url}")
def get_skin(url: str):
    print(url)          #[http,naver,com]
    url=url.replace("[", '')
    url=url.replace("]", '')
    url=url.replace("\"", '')
    url=url.replace(",", '/')
    url=url.replace("!", '?')
    url=url.replace(" ", '')
    print(url)          #http://naver.com
    result=skin(url)
    print(f'<br>result<br>{result}<br>')
    return result

if __name__=='__main__':
    home()


