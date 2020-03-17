# best_songs

Cliente API simples que busca em Genius (repositório com informações osbre musicas e artistas) as 10 musicas mais populares do artista. Pesquisa feita pelo ID do artista no site Genius.

Tecnologias utililadas:
- Python
- Django
- Django RFW

Utilização
 *PREPARAÇÃO
 1 - instalar docker e docker-compose
 2 - clonar o repositório 
 3 - na raiz da pasta, rodar o comando docker-compose up --build
 
 *PESQUISANDO A MUSICA
 1 - identificar o ID do artista no Genius
 2 - mandar uma chamda GET para a URL http://localhost:8000/topten/id (substituir id pelo id do artista escolido. EX: 16775)
 
 API Genius documentation:
 https://docs.genius.com/#/getting-started-h1
