# API de Atividades da Mergington High School

Uma aplicação FastAPI super simples que permite que estudantes visualizem e se inscrevam em atividades extracurriculares.

## Funcionalidades

- Visualizar todas as atividades extracurriculares disponíveis
- Inscrever-se em atividades

## Primeiros Passos

1. Instale as dependências:

   ```
   pip install -r ../requirements.txt
   ```

2. Execute a aplicação:

   ```
   uvicorn app:app --reload
   ```

3. Abra seu navegador e acesse:
   - Documentação da API: http://localhost:8000/docs
   - Documentação alternativa: http://localhost:8000/redoc

## Endpoints da API

| Método | Endpoint                                                          | Descrição                                                                   |
| ------ | ----------------------------------------------------------------- | --------------------------------------------------------------------------- |
| GET    | `/activities`                                                     | Obtém todas as atividades com seus detalhes e contagem atual de participantes |
| POST   | `/activities/{activity_name}/signup?email=student@mergington.edu` | Inscreve-se em uma atividade                                                |

## Testes de Backend

Os testes ficam no diretório de nível raiz `tests/` e usam `pytest`.

1. Execute todos os testes:

   ```
   python -m pytest -v
   ```

2. Execute novamente para validar isolamento de estado:

   ```
   python -m pytest -v
   ```

3. Execute apenas os testes de inscrição:

   ```
   python -m pytest -v tests/test_signup.py
   ```

### Convenção AAA (Arrange-Act-Assert)

Todos os testes seguem o padrão AAA para manter legibilidade e consistência:

- Arrange: prepara o cenário e os dados de entrada.
- Act: executa a ação a ser testada.
- Assert: valida o resultado esperado.

## Troubleshooting de Ambiente (Debian/Ubuntu)

Se ocorrer erro como `No module named pip`, `No module named pytest` ou falha de criação de venv por ausência de `ensurepip`, instale os pacotes base do Python:

```
sudo apt update
sudo apt install -y python3-pip python3-venv
```

Depois, no diretório raiz do projeto:

```
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
python -m pytest -v
```

## Modelo de Dados

A aplicação usa um modelo de dados simples com identificadores significativos:

1. **Activities** - Usa o nome da atividade como identificador:

   - Descrição
   - Horário
   - Número máximo de participantes permitidos
   - Lista de emails dos estudantes inscritos

2. **Students** - Usa email como identificador:
   - Nome
   - Série/Ano escolar

Todos os dados são armazenados em memória, o que significa que os dados serão resetados quando o servidor reiniciar.
