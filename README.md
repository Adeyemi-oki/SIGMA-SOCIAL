# Sigma Social (Django)

Production-ready Django starter for a social media platform.

## Structure
- `config/`: project settings and entrypoints
- `apps/`: domain apps (`users`, `profiles`, `posts`, `comments`, `likes`, `notifications`)
- `static/`, `media/`: static and uploaded media

## Local setup
1. Create virtual environment and install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Copy env file and fill values:
   ```bash
   cp .env.example .env
   ```
3. Run migrations and start server:
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

## Render deployment
- Use `render.yaml` (Blueprint deploy) or manually set:
  - Build command: `./build.sh`
  - Start command: `gunicorn config.wsgi:application`
- Provision PostgreSQL and map env vars.


## Render troubleshooting
- If you still see **400 Bad Request**, confirm Render env variables are present and restart deploy.
- This project auto-trusts runtime hostnames from `RENDER_EXTERNAL_HOSTNAME`, `RENDER_HOSTNAME`, and `RENDER_EXTERNAL_URL`.
- You can also explicitly set `DJANGO_ALLOWED_HOSTS` (comma-separated) and `DJANGO_CSRF_TRUSTED_ORIGINS` (comma-separated `https://...` origins).
