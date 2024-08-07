FROM python:3.12

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the working directory
COPY problem1 problem1

WORKDIR /app/problem1

# Specify the command to run the application
CMD [ "python", "main.py" ]