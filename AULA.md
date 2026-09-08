# Aula

Esse arquivo descreve o passo-a-passo para a criação de um pacote Python, desde a instalação das dependências até a 
publicação do pacote no PyPI.

1. Crie uma conta no site TestPyPi.
2. Criar um Token de API.
3. Coloque o Token de API no GitHub Secrets do repositório do seu fork.
4. Crie uma tag e envie-a para o GitHub (push).
5. O GitHub Actions irá executar o workflow de publicação do pacote no TestPyPi.
6. Acesse o site TestPyPi e verifique se o pacote foi publicado com sucesso.
