# build: docker build -t lsipii/lolcatfigletgnuplotprint -f lolcatfigletgnuplotprint.dockerfile .
# run: docker run -it --rm lsipii/lolcatfigletgnuplotprint
FROM python:3.10
WORKDIR /usr/src/lolcatfigletgnuplotprint

# Upgrade pip
RUN python -m pip install --upgrade pip

# Install container depencencies
RUN apt-get update && apt-get install -y lolcat figlet gnuplot

# Add games to env
ENV PATH $PATH:/usr/games

# App install
COPY . .
RUN python -m pip install -e .

ENTRYPOINT [ "python",  "-m", "src.printers"]