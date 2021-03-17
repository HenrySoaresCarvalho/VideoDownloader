# Simples API de download de video.

## Api com o intuito de fazer download de videos no youtube.

### Bibliotecas usadas:

Pytube (Biblioteca responsavel pela captura de informação e download de video)

Flask (Micro-FrameWork responsavel pelo controle de requisições e retorno de respostas)

### Instalação:

#### Requisitos:
Necessario Python

Caso não tenha as bibliotecas instaladas o programa irá instalar.

Ao programa instalar as dependencias você deve renicia-lo.

Se não tiver as duas dependencias o programa devera ser reniciado duas vezes.

#### Startando o Projeto:
python app.py

## Uso da Api

### Rotas:

### /video/info -> POST
Rota para pegar as informações do video.

#### Ex:

{
    "link": _Link do video_
}

se tudo der certo deve retornar:

{
    "author": _nome do autor_,
    "video_name": _nome do video_,
    "video_views": _quantidade de views_
}

### /video/download -> POST
Rota para baixar o video.

#### Ex:

{
    "link":_Link do video_
}

Se tudo der certo deve retornar:

{
    "status": "Downloaded",
    "video_id": _id do video_
}

### /video/get/<id> -> GET
Rota para fazer o download do video.

### /video/delete/<id> -> DELETE
Rota para deletar o video.
  
