# ✨ Dream Interpretation

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Flask](https://img.shields.io/badge/Flask-2.0+-blue)
![AI](https://img.shields.io/badge/AI-Machine%20Learning-orange)
![Gemini](https://img.shields.io/badge/Gemini-Google%20AI-red)

## 🌐 Live Demo

You can try the application here: [Dream Interpretation on Render](https://dream-saas.onrender.com)

⚠ **Note:** This application is hosted on a free server, which may enter sleep mode when not in use. The first request might take a few seconds to wake up the server.

## 📖 Description

Dream Interpretation is an AI-powered project that analyzes and interprets dreams based on user inputs. The project aims to provide instant and comprehensive interpretations, helping users gain a deeper understanding of their dreams.

## 🚀 Features

- ⚡ **Instant Analysis:** Provides immediate dream interpretations.
- 🤖 **AI-Powered:** Uses machine learning models for accurate dream analysis.
- 🎨 **User-Friendly Interface:** Easy-to-use design for dream input and interpretation.

## 🛠️ Installation

### 📌 Prerequisites

Before installing, ensure you have the required dependencies:

1. **Check if Python is installed:**

   ```bash
   python3 --version
   ```

   If Python is not installed, you can install it using the terminal:

   **For Ubuntu/Debian:**

   ```bash
   sudo apt update && sudo apt install python3
   ```

   **For macOS (using Homebrew):**

   If Homebrew is not installed, install it using:

   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

   ```bash
   brew install python3
   ```

   **For Windows:**
   Download and install it from [Python's official site](https://www.python.org/downloads/), then ensure `python3` is added to your system PATH.

2. **Check if pip is installed:**

   ```bash
   pip3 --version
   ```

   If pip is missing, install it using:

   ```bash
   python3 -m ensurepip --default-pip
   ```

3. **Ensure Git is installed:**

   ```bash
   git --version
   ```

   If Git is not installed, follow the instructions on [Git's official website](https://git-scm.com/downloads).

4. **Clone the repository:**

   ```bash
   git clone https://github.com/Devehab/dream-interpretation.git
   cd dream-interpretation
   ```

5. **Obtain a Google API Key:**

   - Visit [Google AI Studio](https://aistudio.google.com/).
   - Sign in with your Google account.
   - Navigate to the API section and generate a new API key.
   - Copy the generated API key.

6. **Create a ************************`.env`************************ file and store the API key:**

   - Open a terminal inside the project directory.
   - In the terminal, navigate to your project directory and run the following command to create the `.env` file:
     ```bash
     touch .env
     ```
   - Open the `.env` file with a text editor and add the following line:
     ```
     GOOGLE_API_KEY=your-api-key-here
     ```
   - Save and close the file.

7. **Create and activate a virtual environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

8. **Install dependencies:**

   ```bash
   pip3 install -r requirements.txt
   ```

9. **Run the application locally:**

   ```bash
   python3 app.py
   ```

## 🚀 Deploying to a Live Server (Render)

You can deploy this application on a live server like **Render** by following these steps:

1. **Create a Render account:**

   - Go to [Render](https://render.com/) and sign up.

2. **Create a new web service:**

   - Click on "New" -> "Web Service".
   - Connect your GitHub repository and select `dream-interpretation`.
   - Choose the `Python` runtime and configure the environment.

3. **Set up environment variables:**

   - In the Render dashboard, go to the "Environment" section.
   - Add `GOOGLE_API_KEY` with your API key.

4. **Define the start command:**

   ```bash
   gunicorn -w 4 -b 0.0.0.0:3000 app:app
   ```

5. **Deploy and monitor:**

   - Click "Deploy" and wait for the build to complete.
   - Your application will be live at the provided Render URL.

## 🎯 Usage

Once the application is running, open a web browser and go to `http://127.0.0.1:3000` or the deployed Render URL. Enter your dream description and click the "Interpret" button to receive an analysis.

## 🤝 Contributing

We welcome contributions! To contribute:

1. **Fork the repository** by clicking on the "Fork" button at the top right.
2. **Create a new branch:**
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Make your changes and commit them.**
4. **Push the changes:**
   ```bash
   git push origin feature/your-feature-name
   ```
5. **Create a Pull Request** on the original repository.

## 📜 License

This project is licensed under the MIT License. For more details, see the [LICENSE](LICENSE) file.

---

🚀 *Feel free to open issues or discussions for suggestions and improvements!*

