# Text Sentiment Analysis with Flask

This repository contains a simple web application for performing sentiment analysis on text using Flask. The application allows users to input text, and it returns the sentiment (positive, negative, or neutral) associated with the given text.

## Features

- Text sentiment analysis using a pre-trained model.
- Simple and user-friendly web interface.
- Easy integration with Docker for containerization.
- Jenkins pipeline for continuous integration and deployment.

## Getting Started

### Prerequisites

Before you start, ensure you have the following installed:

- Python 3.6 or higher
- Docker (optional, for containerization)
- Jenkins (optional, for CI/CD)

### Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/alishbalaeeq/Sentiment-Analysis-from-text.git
   cd Sentiment-Analysis-from-text

2. Create a virtual environment and activate it (recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate

3. Install the required Python packages:

   ```bash
   pip install -r requirements.txt

### Usage
1. Run the Flask application:

   ```bash
   python flask_app.py
   
2. Open a web browser and navigate to http://localhost:5000 to access the sentiment analysis tool.
3. Enter text in the provided input field, and the application will analyze its sentiment and display the result.

### Docker Support

This repository includes a Dockerfile that allows you to containerize the Flask application. To build and run the Docker container, use the following commands:

   ```bash
   docker build -t your-image-name .
   docker run -p 8080:5000 your-image-name

The application will be accessible at http://localhost:8080.

### Jenkins Integration

The repository includes Jenkins support for continuous integration and deployment. The Jenkinsfile in the jenkins directory defines the CI/CD pipeline. You can set up Jenkins to automatically build and deploy the application when changes are pushed to the repository.

