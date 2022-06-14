# build: docker build -t lolcatfigletgnuplotprint -f lolcatfigletgnuplotprint.dockerfile .
# run: docker run -it --rm lolcatfigletgnuplotprint
FROM python:3.10
WORKDIR /usr/src/app

# Upgrade pip
RUN python -m pip install --upgrade pip

# Install container depencencies
RUN apt-get update && apt-get install -y lolcat figlet gnuplot

# Add games to env
ENV PATH $PATH:/usr/games

# App install
COPY . .
RUN python -m pip install --no-cache-dir -r requirements.txt

ENTRYPOINT [ "python",  "-m", "printers"]