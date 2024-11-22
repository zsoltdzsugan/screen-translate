FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variable for OpenAI API key
ENV OPENAI_API_KEY=your_openai_api_key_here

# Command to run the application
CMD ["python", "main.py"]

