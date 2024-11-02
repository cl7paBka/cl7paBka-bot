## cl7paBka-bot is a fun Telegram bot packed with quirky features! Here's what it offers:
- 🤖 **AI Assistant "cl7paBka"** — powered by AI, the bot can answer questions, help with tasks, and chat on any topic!
- 🎶 **Music Recognition** — send a voice or video message with music, and the bot will identify the song for you!
- 🖼️ **Photo Blurring** — send a photo with people, and the bot will return it with blurred faces for privacy!
- 📜 **About the Creator** — get to know me a bit better.


## 🏗️ Project Architecture

### 🗂️ Directory Structure

```bash
cl7paBka-bot/
├── app/                    # Main directory with project code
│   ├── __init__.py
│   ├── interaction/           # Presentation layer
│   │   ├── __init__.py
│   │   ├── handlers/          # Handlers for commands and menu
│   │   │   ├── assistant.py
│   │   │   ├── recognize.py
│   │   │   ├── blur.py
│   │   │   ├── about.py
│   │   │   ├── menu.py
│   │   │   └── errors.py      # Exception handler
│   │   └── keyboard.py        # Menu button settings
│   ├── application/           # Business logic layer
│   │   ├── __init__.py
│   │   ├── services/
│   │   │   ├── assistant_service.py
│   │   │   ├── music_service.py
│   │   │   └── photo_blur_service.py
│   ├── infrastructure/        # Supporting components
│   │   ├── __init__.py
│   │   ├── logging.py         # Logging configuration
│   │   ├── api_clients/       # External API integrations
│   │   │   ├── ai_client.py
│   │   │   ├── music_client.py
│   │   │   └── photo_client.py
│   └── data/                  # Data layer
│       ├── __init__.py
│       ├── db.py              # Database connection
│       └── repositories/      # Data repositories
│           └── user_repository.py
├── config.py                  # Configuration file for settings and API keys
├── main.py                    # Main file to run the bot
├── Dockerfile                 # Dockerfile for containerizing the app
├── docker-compose.yml         # Docker Compose file for managing multi-container setup
└── requirements.txt           # Project dependencies
```

### Project Layers and Modules

**app/** - This main directory contains all the source code for the bot. Each subdirectory within app/ is structured according to the Onion Architecture, keeping different layers separate for better maintainability and scalability.

1. **Presentation Layer (interaction/)**

- **Purpose:** Handles user interactions, processing commands, and providing user interface elements like menus and buttons. This layer is responsible for managing communication with users and routing user commands to the business logic layer.

- **Modules:**
    - **handlers/** - Contains handlers for all commands and menu options.
        - **assistant.py** - Handles the /assistant command, initiating interaction with the AI assistant.
        - **recognize.py** - Handles the /recognize command for music recognition.
        - **blur.py** - Handles the /blur command, which initiates the photo blurring process.
        - **about.py** - Handles the /about command, displaying information about the creator.
        - **menu.py** - Handles the /menu command, generating the main menu and associated buttons.
        - **errors.py** - Manages error handling, logging exceptions, and providing feedback to users when issues occur.
    - **keyboard.py** - Defines menu buttons and keyboard layouts, centralizing configuration for the bot's user interface.

2. **Business Logic Layer (application/)**

- **Purpose:** Implements the core functionality of the bot. This layer contains the services responsible for processing data received from the presentation layer, as well as managing and coordinating tasks between other components and the infrastructure layer.

- **Modules:**
    - **services/** - Contains modules dedicated to each primary function of the bot.
        - **assistant_service.py** - Processes requests to the AI assistant, interacting with an external API to retrieve responses.
        - **music_service.py** - Manages audio processing and sends requests to an external API for music recognition.
        - **photo_blur_service.py** - Processes images to blur faces, using an external face-blurring API or service.

- **Infrastructure Layer (infrastructure/)**

- **Purpose:** Manages support components and integrations, such as external APIs, logging, and additional system resources that the application depends on.

- **Modules:**
    - **logging.py** - Sets up logging for the application, capturing key events, errors, and general activity logs to monitor bot performance and troubleshoot issues.
    - **api_clients/** - Contains modules that facilitate interaction with external APIs.
          - **ai_client.py** - Client for connecting with an AI service API that powers the assistant.
          - **music_client.py** - Client for the music recognition API, allowing the bot to identify songs from user-submitted audio.
          - **photo_client.py** - Client for the face-blurring API, processing user-submitted photos to blur faces.

3. **Data Layer (data/)**

- **Purpose:** Handles data storage and retrieval, providing an abstraction over the database through a repository pattern for easy access and manipulation.

- **Modules:**
    - **db.py** - Manages the connection to the PostgreSQL database, handling initial setup and configuration.
    - **repositories/** - Contains repository modules that manage interactions with the database.
        - **user_repository.py** - Defines methods to manage user data in the database, such as adding, updating, or retrieving user records.

4. **Main Project Files**

- **main.py** - The main entry point for the bot. It initializes the bot, registers all handlers, and starts the polling process to listen for user messages.
- **config.py** - Holds configuration settings, including API keys, database URLs, and other environment-specific variables that are used throughout the project.

5. **Deployment and Setup Files**

- **Dockerfile** - Configures a Docker image for the bot, setting up the environment, installing dependencies, and defining the default command to start the bot.
- **docker-compose.yml** - Defines a multi-container setup using Docker Compose, including the bot service and a PostgreSQL database. It manages networking and environment variables between services.
- **requirements.txt** - Lists all Python dependencies for the project, allowing easy installation in different environments.

## Technology Stack

- **Python 3.10+** - The primary programming language for the project.
- **Aiogram 3.13** - A modern and efficient asynchronous Telegram bot framework.
- **PostgreSQL** - A relational database for managing user data and bot activity logs.
- **SQLAlchemy 2.0** - An ORM (Object-Relational Mapping) library for interacting with the PostgreSQL database using a repository pattern.
- **Docker** - Used for containerizing the bot application and its dependencies, ensuring consistency across different environments.
- **Docker Compose** - Manages multiple containers (bot and database) to simplify setup and deployment.


- **External APIs** - Integrates with various APIs to enable specific functionalities:
    - **AI API** - Provides conversational AI capabilities for the assistant.
    - **Music Recognition API** (e.g., Shazam API or ACRCloud) - Identifies music from audio files submitted by users.
    - **Photo Blurring API** - Blurs faces in user-submitted photos for privacy protection.