# build: docker build -t lolcatfigletprint -f app.dockerfile .
# run: docker run -it --rm lolcatfigletprint
FROM python:3.10
WORKDIR /usr/src/app

# Upgrade pip
RUN python -m pip install --upgrade pip

# Install container depencencies
RUN apt-get update && apt-get install -y figlet lolcat gnuplot

# Add games to env
ENV PATH $PATH:/usr/games

# App requirements
COPY requirements.txt .
RUN python -m pip install --no-cache-dir -r requirements.txt

# App
COPY . .

ENTRYPOINT [ "python",  "/usr/src/app/LolcatFigletPrinter.py"]