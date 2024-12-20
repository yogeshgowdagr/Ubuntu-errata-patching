# Flask Project

## Overview
This is a Flask web application designed to manage and display server information, execute SSH commands, and log actions taken within the application. It utilizes SQLAlchemy for database interactions and includes utility functions for SSH operations and USN information retrieval.

## Project Structure
```
flask-project
├── app
│   ├── __init__.py
│   ├── routes.py
│   ├── models.py
│   ├── ssh_utils.py
│   ├── usn_utils.py
│   ├── templates
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── server_list.html
│   │   └── logs.html
│   └── static
│       ├── css
│       ├── js
│       └── images
├── server_list.txt
├── config.py
├── requirements.txt
├── run.py
└── README.md
```

## Setup Instructions
1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd flask-project
   ```

2. **Create a virtual environment:**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

4. **Configure the application:**
   Update `config.py` with your database URI and any other necessary settings.

5. **Run the application:**
   ```
   python run.py
   ```

## Usage
- Access the application in your web browser at `http://127.0.0.1:5000`.
- Use the interface to view server information, execute commands, and check logs.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.