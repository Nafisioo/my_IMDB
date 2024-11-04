# my_IMDB

**my_IMDB** is a web application that allows users to browse, search, and review movies. This project showcases my skills in web development, API integration, and database management.

## Features

- **Movie Search**: Allows users to search for movies by title.
- **Movie Details**: Displays detailed information about movies, including ratings, reviews, and cast.
- **User Reviews**: Users can submit and read reviews for movies.
- **Responsive Design**: Ensures the app looks good on all devices.
- **API Integration**: Fetches movie data from a third-party API.

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/Nafisioo/my_IMDB.git
    cd my_IMDB
    ```

2. Create a virtual environment:

    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the dependencies:

    ```sh
    pip install -r requirements.txt
    ```

4. Set up environment variables for the third-party API key and database credentials.

5. Initialize the database:

    ```sh
    flask db init
    flask db migrate
    flask db upgrade
    ```

6. Run the application:

    ```sh
    flask run
    ```

## Usage

After running the application, navigate to `http://127.0.0.1:5000/` in your web browser. You can search for movies, view details, and submit reviews.

## Contributing

Contributions are welcome! Follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact

If you have any questions or suggestions, feel free to contact me at nafisebahoosh3@gmail.com .
