FROM python:3.10.11

ENV PYTHONUNBUFFERED 1

RUN mkdir /projectIPS
WORKDIR /projectIPS

# Copy the requirements.txt file to the working directory
COPY requirements.txt .

# Install the required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project files to the working directory
COPY . .

# Expose port 8001 for the application
EXPOSE 8001

# Start the application
CMD ["python", "manage.py", "runserver"]