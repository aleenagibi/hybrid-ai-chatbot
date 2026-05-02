function formatText(text) {
    return text
        .replace(/\n/g, "<br>")
        .replace(/\*\*(.*?)\*\*/g, "<b>$1</b>");
}

function getTime() {
    const now = new Date();
    return now.toLocaleTimeString([], {hour: '2-digit', minute:'2-digit'});
}

function addMessage(text, type, source = "") {
    const chatbox = document.getElementById("chatbox");

    const msg = document.createElement("div");
    msg.className = `message ${type}`;

    const avatar = `<img class="avatar" src="${type === 'user' ? 'https://i.pravatar.cc/40' : 'https://cdn-icons-png.flaticon.com/512/4712/4712027.png'}">`;

    msg.innerHTML = `
        ${avatar}
        <div>
            <div class="bubble">${formatText(text)}</div>
            <div class="time">${getTime()}</div>
            ${source ? `<div class="badge">${source}</div>` : ""}
        </div>
    `;

    chatbox.appendChild(msg);
    chatbox.scrollTop = chatbox.scrollHeight;

    saveChat();

    return msg;
}

async function sendMessage() {
    const input = document.getElementById("input");
    const question = input.value.trim();

    if (!question) return;

    addMessage(question, "user");

    input.value = "";

    const loading = addMessage("Typing...", "bot");

    try {
        const res = await fetch("http://127.0.0.1:8000/chat", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({ question })
        });

        const data = await res.json();

        loading.remove();

        if (data.error) {
            addMessage(data.error, "bot");
        } else {
            addMessage(data.response, "bot", data.source);
        }

    } catch {
        loading.remove();
        addMessage("Network error", "bot");
    }
}

/* Enter key */
document.getElementById("input").addEventListener("keypress", function(e) {
    if (e.key === "Enter") sendMessage();
});

/* Theme toggle */
function toggleTheme() {
    document.body.classList.toggle("light");
}

/* Save chat */
function saveChat() {
    localStorage.setItem("chat", document.getElementById("chatbox").innerHTML);
}

/* Load chat */
window.onload = function() {
    const saved = localStorage.getItem("chat");
    if (saved) {
        document.getElementById("chatbox").innerHTML = saved;
    }
};