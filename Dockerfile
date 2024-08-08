FROM python:3.10-slim as base

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .
COPY spec.json .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt


FROM base AS problem1

# Copy the rest of the application code to the working directory
COPY problem1 problem1

WORKDIR /app/problem1

# Specify the command to run the application
CMD [ "python", "main.py" ]

FROM base AS problem2

# Copy the rest of the application code to the working directory
COPY problem2 problem2

WORKDIR /app/problem2

# Specify the command to run the application
CMD [ "python", "main.py" ]