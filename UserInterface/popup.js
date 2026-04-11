document.addEventListener("DOMContentLoaded", () => {
    const chatWindow = document.getElementById("chat-window");
    const userInput = document.getElementById("user-input");
    const sendBtn = document.getElementById("send-btn");
    const quickButtons = document.querySelectorAll(".quick-btn");

    // Add message to chat window
    function addMessage(text, sender) {
        const bubble = document.createElement("div");
        bubble.textContent = text;

        if (sender === "user") {
            bubble.classList.add("user-message");
        } else {
            bubble.classList.add("bot-message");
        }

        chatWindow.appendChild(bubble);

        // Auto-scroll to bottom
        chatWindow.scrollTop = chatWindow.scrollHeight;
    }

    // Send message to backend
    async function sendMessage() {
        const message = userInput.value.trim();
        if (!message) return;

        addMessage(message, "user");
        userInput.value = "";

        try {
            const response = await fetch("http://127.0.0.1:8000/chat", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ message })
            });

            const data = await response.json();
            addMessage(data.reply, "bot");

        } catch (error) {
            addMessage("Error: Unable to reach PvBuddy backend.", "bot");
        }
    }

    // Send button click
    sendBtn.addEventListener("click", sendMessage);

    // Enter key sends message
    userInput.addEventListener("keypress", (e) => {
        if (e.key === "Enter") {
            sendMessage();
        }
    });

    // Quick action buttons
    quickButtons.forEach(btn => {
        btn.addEventListener("click", () => {
            const msg = btn.getAttribute("data-msg");
            userInput.value = msg;
            sendMessage();
        });
    });
});
