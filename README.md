Playground to test the webpage for NWO Physics 2024.

Put the data in `static/data/.` as gifs, later we may want to convert to videos to add interaction.

`template/index.html` dictates the composition and look of the page.

`python app.py` will start the local server so you can look at the result.


### Docker
Alternatively I am experimenting with docker containers to facilitate hosting the page on other machines in the future.

Once `Dockerfile` and `requirements.txt` are as you like, you can use `docker build -t NS-demo .` to build the Docker image.

Then using `docker run -p 5000:5000 NS-demo` will run the Docker container on any machine.

## Generative-AI Disclaimer

Parts of the code have been generated and/or refined using GitHub Copilot. All AI-output has been verified for correctness, accuracy and completeness, revised where needed, and approved by the author(s).

