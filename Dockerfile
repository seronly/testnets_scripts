FROM python:3.10

WORKDIR /code

RUN apt update && apt upgrade -y && apt install -y --no-install-recommends locales; rm -rf /var/lib/apt/lists/*; sed -i '/^#.* ru_RU.UTF-8 /s/^#//' /etc/locale.gen; locale-gen

# Копируем requirements.txt в контейнер
COPY requirements.txt .
# Устанавливаем зависимости Python
RUN pip3 install --upgrade setuptools
RUN pip3 install -r requirements.txt

RUN chmod 755 .
COPY /app ./app
COPY wallets.db .

# Открываем порт для приложения (если необходимо)
# EXPOSE 8000

# Команда для запуска приложения
# RUN chmod +x ./webdrivers/chromedriver_linux
# CMD ["python", "-m", "app"]