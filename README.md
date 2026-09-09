# pythonPackages

Esse repositório é um tutorial sobre como publicar pacotes em Python no TestPyPi.

Este arquivo [README](README.md) serve como a documentação "oficial" do pacote - ou seja, como um usuário encontraria a 
documentação caso este pacote fosse de verdade.

Já o arquivo [AULA.md](AULA.md) é um tutorial passo-a-passo de como criar e publicar pacotes Python no TestPyPi.

## Instalação

Caso o pacote estivesse publicado no PyPI, você poderia instalá-lo com o seguinte comando:

```bash
pip install henryzord_pythonPackages
```

Como este pacote está publicado apenas no TestPyPi, você deve instalar com o seguinte comando:

```bash
pip install --index-url https://test.pypi.org/simple/ henryzord_pythonPackages
```

O pacote está hospedado neste link: https://test.pypi.org/project/henryzord-pythonPackages/

## Uso

Uma vez instalado, você pode usar o pacote em seu código Python da seguinte forma:

```python
from rpg_dice import roll

print(roll("d6"))
print(roll("d20"))
print(roll("2d6"))
print(roll("1d20+5"))
print(roll("3d8-2"))
```

### Valores suportados

```text
d6
d20
2d6
1d20+5
3d8-2
```

## Desenvolvimento

Para colaborar com o desenvolvimento do pacote, você deve primeiro fazer um fork deste repositório, e depois abrir 
um pull request com as contribuições.

Para desenvolvimento do pacote, siga as instruções abaixo. 

Instale as dependências:

```bash
pip install -r requirements.txt
```

Construa o pacote:

```bash
python -m build
```

### Publicando

Após fazer modificações no seu código, salve-o em um commit:

```bash
git add .
git commit -m "Mensagem do commit"
```

E depois, publique uma tag:

```bash
git tag v0.1.0  # ou outro número de versão, dependendo de qual você estiver
git push origin v0.1.0
```

O push da tag irá disparar o workflow presente em [publish.yml](.github/workflows/publish.yml).
