FROM python:3.8

# streamlit-specific commands
RUN mkdir -p ~/.streamlit
RUN bash -c 'echo -e "\
[general]\n\
email = \"\"\n\
" > ~/.streamlit/credentials.toml'
RUN bash -c 'echo -e "\
[server]\n\
enableCORS = false\n\
" > ~/.streamlit/config.toml'

RUN pip install poetry==1.1.0

WORKDIR /app

COPY poetry.lock pyproject.toml /app/

RUN poetry config virtualenvs.create false && poetry install --no-dev

EXPOSE 8501

COPY . /app

CMD ["poetry","run","streamlit", "run","app.py"]



