# backend

## Environment
- Python 3.10.12 (他のバージョンでもそんなに離れてなければたぶん動くと思います…)

## Installation

```
git clone git@github.com:season2-spajam/backend.git
```

`manage.py` と同じ階層に `.env` を置いてください。

`.env`
```
SECRET_KEY='(Django の secret key)'
NGROK_URL='(NGROK で発行した URL)'
```

```
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py runserver
```

## API endpoints
127.0.0.1:8000/api/(なんか) に直接アクセスして確認できます。
- 127.0.0.1:8000/api/
  - posts/
    - (GET) すべての投稿を取得
    - (POST) 新しい投稿を追加
  - posts/\<post_id\>
    - (PATCH) goodCount など、情報を変更
  - posts\/\?filter\=today
    - (GET) その日の投稿を取得