# Use an official Python runtime as the base image
FROM python:3.9

# Label the image to link back to the repository
LABEL org.opencontainers.image.source="https://github.com/babajaguska/ppg_modelling"

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the code to the container
COPY . .

# Set the command to run when the container starts
CMD [ "python", "app.py" ]
