FROM python:3.8-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8096

# Run your script when the container launches
CMD ["python", "netflix_ui_automation.py"]
