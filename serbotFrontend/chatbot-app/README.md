# Ollama Chatbot UI
![alt text](/images/chat_ui.png)

This project provides a simple React-based chatbot interface designed to interact with a backend API powered by **FastAPI** and **ServerAPI SDK**.

## Features
- Interactive chat interface for querying server data.
- Real-time responses from the backend.
- Auto-scrolling chat view.
- Keyboard shortcuts for sending messages.

## Prerequisites
- **Node.js** installed.
- Backend API running (FastAPI).

## Installation
1. Install dependencies:
   ```bash
   npm install
   ```
2. Start the development server:
   ```bash
   npm start
   ```
   The app will be available at `http://localhost:3000`.

## Usage
1. Ensure the FastAPI backend is running (`http://localhost:8000` by default).
2. Type your query in the chat input field and press **Enter** to send.

## Customization
- **Backend URL**: Update in `Chat.js`:
  ```javascript
  const backendUrl = 'http://localhost:8000/chat';
  ```
- **Styling**: Modify `Chat.css` for custom styles.

## Example Queries
- "What is the current CPU usage?"
- "List all websites running on the server."
- "Show me the health status of Server B."

## License
Licensed under the MIT License.

---

