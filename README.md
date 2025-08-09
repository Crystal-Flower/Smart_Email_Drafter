# Smart Email Drafter

An intelligent agent that automatically reads your unread emails, drafts context-aware replies using a local Large Language Model (LLM) via Ollama, and saves them for your review. Take back control of your inbox without compromising your privacy.

-----

## 🌟 Overview

Email overload is a common struggle. Manually replying to every message consumes significant time and mental energy. **AI Email Responder** tackles this by acting as your personal email assistant. It intelligently processes incoming emails and prepares professional, ready-to-send drafts.

The key difference? **It runs entirely on your local machine.** By using [Ollama](https://ollama.com/), your email content is never sent to a third-party cloud service, ensuring your data remains private and secure. You get the power of state-of-the-art AI with complete peace of mind.

## ✨ Features

  * **📧 Automated Reply Drafting:** Processes unread emails and generates high-quality draft replies.
  * **🤖 Powered by Local LLMs:** Leverages Ollama to run powerful models like Llama 3.2 on your own hardware.
  * **🔒 Privacy-First:** Your emails are analyzed locally. No data is shared with external APIs.
  * **🧠 Context-Aware Generation:** Creates relevant and personalized replies by incorporating the sender, subject, and original email body into its prompts.
  * **✅ User in Control:** Generates **drafts** instead of sending emails directly, giving you full control to review, edit, and approve every message.
  * **🔧 Highly Customizable:** Easily change the LLM model or modify the prompt in `main.py` to alter the AI's tone, style, or instructions.

## ⚙️ How It Works

The workflow is simple yet powerful:

1.  **Fetch Unread Mail:** The script securely connects to your email account (e.g., Gmail) using OAuth2 and fetches all unread messages.
2.  **Construct Prompt:** For each email, it creates a detailed, structured prompt containing the email's content and context.
3.  **Generate Reply:** The prompt is sent to your local Ollama instance, which uses an LLM (e.g., `llama3.2`) to generate a coherent and professional reply.
4.  **Create Draft:** The script connects back to your email account and saves the AI-generated text as a draft reply to the original message.
5.  **Review & Send:** You can then open your email client, review the drafts, make any necessary tweaks, and send them with confidence.

## 🛠️ Setup and Installation

Follow these steps to get the AI Email Responder up and running on your system.

### Prerequisites

  * [Python 3.8+](https://www.python.org/downloads/)
  * [Ollama](https://ollama.com/download) installed and running on your machine.
  * An LLM pulled via Ollama. We recommend Llama 3.2:
    ```bash
    ollama pull llama3.2
    ```
  * API access to your email provider. The included `helper.py` is designed for the **Gmail API**. You will need to enable it and download your credentials.

### Installation Guide

**1. Clone the Repository**

```bash
git clone https://github.com/Crystal-Flower/Smart_Email_Drafter.git
cd Smart_Email_Drafter
```

**2. Set Up a Virtual Environment (Recommended)**

```bash
# For macOS/Linux
python3 -m venv venv
source venv/bin/activate

# For Windows
python -m venv venv
.\venv\Scripts\activate
```

**3. Install Dependencies**
The project relies on a few Python libraries. A `requirements.txt` would look like this:

```
# requirements.txt
ollama
google-api-python-client
google-auth-oauthlib
google-auth-httplib2
```

Install them using pip:

```bash
pip install -r requirements.txt
```

**4. Configure Gmail API Credentials**
This is the most critical step for allowing the script to access your email.

  * Go to the [Google Cloud Console](https://console.cloud.google.com/).
  * Create a new project.
  * Enable the **Gmail API** for your project.
  * Create credentials for an **OAuth client ID**. Select "Desktop app" as the application type.
  * Download the JSON file. **Rename it to `credentials.json`** and place it in the root directory of this project.

The first time you run the script, you will be prompted to authorize access to your Gmail account through your web browser. This will create a `token.json` file in the project directory, which stores your credentials for future runs.

**5. Configure Helper File**
Open the `helper.py` file and update the `name` variable inside the `get_unread_messages()` function to the name you want to sign off your emails with.

## 🚀 Usage

Once the setup is complete, running the agent is straightforward.

**1. Start Ollama**
Ensure the Ollama application is running or start the server in a separate terminal:

```bash
ollama serve
```

**2. Run the Main Script**
Execute the main Python script from the project's root directory:

```bash
python main.py
```

The script will begin fetching unread emails and generating drafts. You will see output in your terminal for each email processed:

```
completed mail from sender@example.com
----------------------------------------
completed mail from another.sender@work.com
----------------------------------------
```

Now, check your email account's "Drafts" folder. You'll find the AI-generated replies waiting for your review\!

## 🔧 Customization

You can easily tailor the AI's behavior by editing `main.py`.

### Changing the LLM Model

To use a different model you have downloaded in Ollama (e.g., `mistral` or `gemma`), simply change the model name in this line:

```python
# In main.py
response = ollama.generate("llama3.2", prompt).response
# Change "llama3.2" to "mistral" or any other Ollama model
```

### Modifying the System Prompt

The core logic of the AI is driven by the prompt. You can change its personality, instructions, and constraints by editing the `prompt` f-string in `main.py`. Experiment with different instructions to get the perfect results for your needs.

## 🤝 Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

Please open an issue first to discuss any major changes you would like to make.

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

-----
