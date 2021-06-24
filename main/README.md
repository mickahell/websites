## Build
- Main page : docker build . --file main/Dockerfile --tag page_main:latest
## Launch
- Main page : docker run -d --name page_main -p 8502:8501 -e LANG=C.UTF-8 page_main:latest
