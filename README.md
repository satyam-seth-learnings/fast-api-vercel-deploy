# How to run

- Create virtual enticement

  ```bash
  python3 -m venv .venv
  ```

- Activate virtual enticement

  ```bash
  source .venv/bin/activate
  ```

- Install requirements

  ```bash
  pip install -r requirements.txt
  ```

- Create a `.env` file and add the variables listed in the `.env.example` file.

- Run fast api server in dev mode

  ```bash
  fastapi dev main.py
  ```

- Open API docs link in browser `http://127.0.0.1:8000/docs`

# How to deploy

- Install vercel cli

  ```sh
  npm i -g vercel
  ```

- Vercel Login

  ```sh
  vercel login
  ```

- Deploy project

  ```sh
  vercel .
  ```

- Deploy as production

  ```sh
  vercel --prod .
  ```
