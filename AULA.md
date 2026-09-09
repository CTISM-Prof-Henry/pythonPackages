# Aula

Esse arquivo descreve o passo-a-passo para a criação de um pacote Python, desde a instalação das dependências até a 
publicação do pacote no PyPI.

1. Crie uma conta no site TestPyPi: https://test.pypi.org/account/register/
2. Criar um Token de API (Configurações → Configurações de conta → role para baixo até achar Tokens de API ou acesse o 
   link https://test.pypi.org/manage/account/token/) 
3. Anote o token de API
4. Crie um Secret no repositório do seu fork e coloque o Token de API sob o nome `TEST_PYPI_TOKEN`, que é o mesmo
   nome usado no [workflow](.github/workflows/publish.yml)
   * A página do secrets é `https://github.com/<SEU_USUARIO>/<SEU_REPOSITORIO>/settings/secrets/actions`. Substitua
    `<SEU_USUARIO>` e `<SEU_REPOSITORIO>` pelo seu usuário e repositório do GitHub.
5. Adicione uma tag e envie-a para o GitHub:
   ```bash
   git tag v0.1.0  # ou outro número de versão, dependendo de qual você estiver
   git push origin v0.1.0
   ```
6. O GitHub Actions irá executar o workflow de publicação do pacote no TestPyPi.
7. Acesse o site TestPyPi e verifique se o pacote foi publicado com sucesso.
