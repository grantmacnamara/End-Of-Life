# Use the official Python image from Docker Hub
FROM python:3.9

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the requirements file into the container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY app.py .
COPY getApplicationData.py .

# Copy the data folder into the container
COPY data /usr/src/app/data
COPY templates /usr/src/app/templates
COPY static /usr/src/app/static
# Expose the port your app runs on
EXPOSE 5000

# Command to run the application
CMD ["flask", "run", "--host=0.0.0.0"]
