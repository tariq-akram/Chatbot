# Simple OpenAI API Integration with Django

This project demonstrates a simple integration of the OpenAI API into a single-page website using Django. Users can input questions into a form, and the website generates a response using the OpenAI API.

## Features

- **Question Submission**: Users can submit questions through a form on the website.
- **AI Response Generation**: Upon submitting a question, the website sends a request to the OpenAI API to generate a response based on the input question.
- **Display of Question and Response**: The website displays the submitted question along with the generated AI response.
- **Minimalistic Interface**: The user interface is kept simple and minimalistic, focusing on functionality.

## Requirements

- Python 3.11
- Django
- Personal OpenAI API Key

## Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/simple-openai-django.git
    ```

2. Navigate to the project directory:

    ```bash
    cd chatbot
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Obtain an OpenAI API Key:
   
   If you don't have an OpenAI API key, sign up for one at the [OpenAI website](https://openai.com/). Once you have your API key, include it in the appropriate place in your Django project settings.

5. Run the Django development server:

    ```bash
    python manage.py runserver
    ```

6. Access the website in your browser at `http://localhost:8000`.

## Usage

1. Open the website in your browser.
2. Enter your question into the form.
3. Submit the form.
4. View the generated response below the form.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature-name`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add some feature'`).
5. Push to the branch (`git push origin feature/your-feature-name`).
6. Create a new Pull Request.
