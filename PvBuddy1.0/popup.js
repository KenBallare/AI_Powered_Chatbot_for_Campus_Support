
document.addEventListener('DOMContentLoaded', () => {
    const userInput = document.getElementById('user-input');
    const sendBtn = document.getElementById('send-btn');
    const chatWindow = document.getElementById('chat-window');
    const Model_Name = "gemini-2.5-flash";
    const apiKey = 'AI_KEY';
    const API_Endpoint = `https://generativelanguage.googleapis.com/v1beta/models/${Model_Name}:generateContent`;
    const headers = {'Content-Type': 'application/json',
        'x-goog-api-key': apiKey
    };


    sendBtn.addEventListener('click', sendMessage);
    userInput.addEventListener('keypress', (e) =>{
        if (e.key === 'Enter') {
            sendMessage();
        }
    });

    function sendMessage() {
        const userMessage = userInput.value.trim();
        if (!userMessage) return;

        appendMessage('You', userMessage);
        userInput.value = '';

        fetch('https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent', {
            method: 'POST',
            headers: headers,
            body: JSON.stringify({
                contents: [{
                    role: 'you',
                    parts: [{ text: userMessage}]
                }],
        
            })
        })
        .then(response => {
            if (!response.ok) {
                return response.json().then(err => {
                    console.error('API Error Response:', err);
                    throw new Error(err.error.message || 'API request failed');
                });
            }
            return response.json();
        })
        .then(data => {
            const aiResponse = data.candidates[0].content.parts[0].text;
            appendMessage('PvBuddy', aiResponse);
        })
        .catch(error => {
            console.error('Fetch Error:', error);
            appendMessage('PvBuddy', 'Sorry, there was an error processing your request.');
        });
    }
    function appendMessage(sender, text) {
        const messageDiv = document.createElement('div');

        
        messageDiv.textContent = `${sender}: ${text}`;

        messageDiv.classList.add('message', sender.toLowerCase());

        chatWindow.appendChild(messageDiv);
        chatWindow.scrollTop = chatWindow.scrollHeight;
    }
});
