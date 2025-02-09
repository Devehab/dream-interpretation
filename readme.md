# ✨ Dream Interpretation

## 📖 Description
Dream Interpretation is an AI-powered project that analyzes and interprets dreams based on user inputs. The project aims to provide instant and comprehensive interpretations, helping users gain a deeper understanding of their dreams.

## 🚀 Features
- ⚡ **Instant Analysis:** Provides immediate dream interpretations.
- 🤖 **AI-Powered:** Uses machine learning models for accurate dream analysis.
- 🎨 **User-Friendly Interface:** Easy-to-use design for dream input and interpretation.

## 🛠️ Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Devehab/dream-interpretation.git
   cd dream-interpretation
   ```
2. **Obtain a Google API Key:**
   - Visit [Google AI Studio](https://aistudio.google.com/).
   - Sign in with your Google account.
   - Navigate to the API section and generate a new API key.
   - Copy the generated API key.

3. **Create a `.env` file and store the API key:**
   - Open a terminal inside the project directory.
   - Run the following command to create the `.env` file:
     ```bash
     touch .env
     ```
   - Open the `.env` file with a text editor and add the following line:
     ```
     GOOGLE_API_KEY=your-api-key-here
     ```
   - Save and close the file.

4. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

5. **Install dependencies:**
   ```bash
   pip3 install -r requirements.txt
   ```

6. **Run the application:**
   ```bash
   python3 app.py
   ```

## 🎯 Usage
Once the application is running, open a web browser and go to `http://localhost:3000`. Enter your dream description and click the "Interpret" button to receive an analysis.

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

