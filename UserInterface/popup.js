document.addEventListener("DOMContentLoaded", () => {
    const chatWindow = document.getElementById("chat-window");
    const userInput = document.getElementById("user-input");
    const sendBtn = document.getElementById("send-btn");
    const quickButtons = document.querySelectorAll(".quick-btn");

    // 🔥 Convert URLs into BUTTONS instead of plain links
    function makeLinksClickable(text) {
        return text.replace(
            /(https?:\/\/[^\s]+)/g,
            (url) => {
                let label = "Open Link";

                // 👇 Smart labels based on link
                if (url.includes("mypassword")) {
                    label = "Reset Password";
                } else if (url.includes("registrar")) {
                    label = "Registrar Page";
                } else if (url.includes("financial")) {
                    label = "Financial Aid";
                } else if (url.includes("library")) {
                    label = "Library Info";
                } else if (url.includes("pvamu.edu")) {
                    label = "Visit Website";
                }

                return `
                    <a href="${url}" target="_blank" class="link-btn">
                        ${label}
                    </a>
                `;
            }
        );
    }

    // Add message to chat window
    function addMessage(text, sender) {
        const bubble = document.createElement("div");

        // 👇 Convert links to buttons
        bubble.innerHTML = makeLinksClickable(text);

        if (sender === "user") {
            bubble.classList.add("user-message");
        } else {
            bubble.classList.add("bot-message");
        }

        chatWindow.appendChild(bubble);

        // Auto-scroll
        chatWindow.scrollTop = chatWindow.scrollHeight;
    }

    // Send message to backend
    async function sendMessage() {
        const message = userInput.value.trim();
        if (!message) return;

        addMessage(message, "user");
        userInput.value = "";

        try {
            const response = await fetch("http://127.0.0.1:8001/chat", {
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

    // Enter key
    userInput.addEventListener("keypress", (e) => {
        if (e.key === "Enter") {
            sendMessage();
        }
    });

    // Quick buttons
    quickButtons.forEach(btn => {
        btn.addEventListener("click", () => {
            const msg = btn.getAttribute("data-msg");
            userInput.value = msg;
            sendMessage();
        });
    });
});