# Study Discord WebApp

## Overview

The Study Discord WebApp is a project built using Python and Django framework to create an online platform for students to collaborate, discuss, and study together in a virtual environment. The application features chat rooms, voice channels, and study group functionalities to facilitate seamless communication and collaboration among users.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/study-discord-webapp.git
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3. Set up the database:

```bash
python manage.py migrate
```

4. Create a superuser account:

```bash
python manage.py createsuperuser
```

5. Run the development server:

```bash
python manage.py runserver
```

## Usage

1. Navigate to the project directory:

```bash
cd study-discord-webapp
```

2. Start the Django development server:

```bash
python manage.py runserver
```

3. Open your web browser and go to `http://localhost:8000` to access the application.

4. Log in with your superuser account to access administrative features.

## Features

- **User Authentication:** Users can create accounts, log in, and log out securely.

- **Chat Rooms:** Real-time chat rooms for text-based communication among users.

- **Voice Channels:** Audio channels for users to join and have voice conversations.

- **Study Groups:** Create and join study groups for collaborative learning.

- **User Roles:** Differentiate between administrators, moderators, and regular users for effective management.

## Technologies Used

- **Python:** The primary programming language for backend development.

- **Django:** A high-level Python web framework for rapid development.

- **Django Channels:** Extends Django to handle WebSockets, enabling real-time functionality.

- **JavaScript and Django REST framework:** Used for frontend interactivity and API development.

- **SQLite:** Lightweight database system for data storage.

## Project Structure

The project follows a standard Django project structure with additional directories for templates, static files, and media files. The frontend is built using HTML, CSS, and JavaScript, and the backend uses Django models, views, and serializers.

## Contributing

Contributions are welcome! If you would like to contribute to this project, please follow our [Contribution Guidelines](CONTRIBUTING.md).

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute the code for your own projects.


## Demonstration :


### Landing Page:
![django Front Page](https://github.com/MOHINI1403/StudyDiscord/assets/96575564/82990dea-4eba-4f6e-9b3d-82443334dbd0)
### StudyDiscord Room Page:
![DiscordRoomPage](https://github.com/MOHINI1403/StudyDiscord/assets/96575564/0b3314cc-14be-43d2-a9ea-df3856d00002)
### StudyDiscord Login And SignUp Page:

![DiscordLoginPAge](https://github.com/MOHINI1403/StudyDiscord/assets/96575564/a8ca5e23-2d34-433e-9ce6-70b84099a8ee)
![DiscordSignUpPage](https://github.com/MOHINI1403/StudyDiscord/assets/96575564/50041665-56e5-4087-bb57-6db12e53de03)
