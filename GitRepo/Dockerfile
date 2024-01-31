FROM python:3.8

# Install Chrome web driver
RUN apt-get update && apt-get install -yqq unzip
RUN wget https://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
RUN unzip chromedriver_linux64.zip chromedriver -d /usr/local/bin/

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . /usr/src/app

# Copy the requirements file into the container
COPY requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the contents of the current directory into the container
COPY . .

# Set the entrypoint to run the tests
ENTRYPOINT ["pytest"]