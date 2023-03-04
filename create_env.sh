#
# postgres envs
#
cat <<EOF > .env
  # postgres envs
  POSTGRES_DB=postgres
  POSTGRES_USER=postgres
  POSTGRES_PASSWORD=postgres
EOF

#
# fastapi envs
#
SECRET_KEY=`openssl rand -hex 32`

cat <<EOF > ./backend.env
  # authentication
  SECRET_KEY = "${SECRET_KEY}"
  ALGORITHM = "HS256"
  ACCESS_TOKEN_EXPIRE_MINUTES = 30

  # fastapi db connection
  DB_URL="postgresql://postgres:postgres@db:5432/postgres"
  TEST_DB_URL="sqlite:///:memory:"
EOF
