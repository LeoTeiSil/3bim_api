from fastapi import FastAPI

app = FastAPI()

@app.get('/clients')
def ola_mundo():
    return {'mensagem': "Minha rota clients!"}

@app.get('/sobre')
def sobre():
    return {'mensagem': "Minha rota sobre!"}