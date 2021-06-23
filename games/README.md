## Build
- QPokemon-fight : docker build . --file games/qpokemon-fight/Dockerfile --tag qpokemon_game:latest
- Page game : docker build . --file games/streamlit/Dockerfile --tag page_game:latest
## Launch
- QPokemon-fight : docker run -d --name qpokemon_game -p 7681:7681 -e LANG=C.UTF-8 qpokemon_game:latest
- Page game      : docker run -d --name page_game -p 8401:8501 -e LANG=C.UTF-8 page_game:latest
