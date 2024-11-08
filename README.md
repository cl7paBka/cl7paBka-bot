## cl7paBka-bot is a fun Telegram bot packed with quirky features! Here's what it offers:
- 🤖 **AI Assistant "cl7paBka"** — powered by AI, the bot can answer questions, help with tasks, and chat on any topic!
- 🎶 **Music Recognition** — send a voice or video message with music, and the bot will identify the song for you!
- 🖼️ **Photo Blurring** — send a photo with people, and the bot will return it with blurred faces for privacy!
- 📜 **About the Creator** — get to know me a bit better.


## 🏗️ Project Architecture

### 🗂️ Directory Structure

```Bash
cl7paBka_bot/
├── bot.py                     # Entry point for starting the bot
├── .gitignore                 # Ignore file for Git
├── Dockerfile                 # Docker setup for app environment
├── docker-compose.yml         # Docker Compose configuration for app and database
├── README.md                  # Project documentation
└── app/
    ├── config.py              # Configuration and environment variables
    ├── handlers/              # Directory for Telegram bot handlers
    │   ├── __init__.py        # Initialize handlers
    │   ├── assistant.py       # Handlers for AI Assistant functionality
    │   ├── music_recognition.py # Handlers for music recognition
    │   ├── photo_blurring.py  # Handlers for photo face blurring
    │   └── about_creator.py   # Handler for "About the Creator" info
    ├── services/              # Core services for bot functions
    │   ├── ai_assistant.py    # Core logic for AI Assistant interactions
    │   ├── music_service.py   # Core logic for music recognition
    │   ├── photo_service.py   # Core logic for face blurring on photos
    ├── keyboards/             # Directory for custom keyboards
    │   ├── __init__.py        # Initialize keyboards
    │   ├── main_menu.py       # Main menu keyboard with bot options
    │   └── inline.py          # Inline keyboards for specific interactions
    └── utils/                 # Utility functions and helpers
        ├── __init__.py        # Initialize utilities
        ├── image_processing.py # Utilities for image processing
        ├── audio_processing.py # Utilities for audio processing
        └── api_helpers.py     # Helpers for external API calls
```
## Technology Stack

- **Python 3.10+** - The primary programming language for the project.
- **Aiogram 3.14** - A modern and efficient asynchronous Telegram bot framework.
- **PostgreSQL** - A relational database for managing user data and bot activity logs.
- **SQLAlchemy 2.0** - An ORM (Object-Relational Mapping) library for interacting with the PostgreSQL database using a repository pattern.
- **Docker** - Used for containerizing the bot application and its dependencies, ensuring consistency across different environments.
- **Docker Compose** - Manages multiple containers (bot and database) to simplify setup and deployment.


- **External APIs** - Integrates with various APIs to enable specific functionalities:
    - **AI API** - Provides conversational AI capabilities for the assistant.
    - **Music Recognition API** (e.g., Shazam API or ACRCloud) - Identifies music from audio files submitted by users.
    - **Photo Blurring API** - Blurs faces in user-submitted photos for privacy protection.