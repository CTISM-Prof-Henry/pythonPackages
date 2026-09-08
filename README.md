# pythonPackages

Tutorial sobre como publicar pacotes em Python no TestPyPi.

## Instalação

```bash
pip install rpg-dice
```

## Uso

```python
from rpg_dice import roll

print(roll("d6"))
print(roll("d20"))
print(roll("2d6"))
print(roll("1d20+5"))
print(roll("3d8-2"))
```

## Valores suportados

```
d6
d20
2d6
1d20+5
3d8-2
```

## Desenvolvimento

Instale as dependências:

```bash
pip install -r requirements.txt
```

Construa o pacote:

```bash
python -m build
```


## Publicando

Depois de fazer modificações no seu código, salve-o em um commit:

```bash
git add .
git commit -m "Mensagem do commit"
```

E depois, publique uma tag:

```bash
git tag v0.1.0
git push origin v0.1.0
```

O push da tag irá disparar o workflow presente em [publish.yml](.github/workflows/publish.yml).

## Usando

Você pode baixar o pacote diretamente do TestPyPi com o seguinte comando:

```bash
pip install --index-url https://test.pypi.org/simple/ rpg-dice
```