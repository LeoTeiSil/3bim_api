python -m venv venv    
.\venv\scripts\activate   
pip install fastapi uvicorn sqlalchemy pymysql
pip freeze > requirements.txt

uvicorn main:app --reload    




git config --global user.email "leoteixeira3010@gmail.com"
git config --global user.name "LeoTeiSil"
