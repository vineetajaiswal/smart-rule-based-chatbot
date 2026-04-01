import streamlit as st

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(page_title="Smart AI Chatbot", page_icon="🤖", layout="centered")

# -----------------------------
# CUSTOM CSS
# -----------------------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #020617, #0f172a, #020617);
    color: white;
}

.block-container {
    padding-top: 1.5rem;
    padding-bottom: 2rem;
    max-width: 900px;
}

.main-title {
    text-align: center;
    font-size: 50px;
    font-weight: 800;
    color: #38bdf8;
    margin-bottom: 8px;
}

.subtitle {
    text-align: center;
    color: #94a3b8;
    font-size: 18px;
    margin-bottom: 25px;
}

.chat-wrapper {
    margin-top: 25px;
    margin-bottom: 25px;
}

.user-msg {
    background: linear-gradient(90deg, #2563eb, #3b82f6);
    color: white;
    padding: 14px 18px;
    border-radius: 18px 18px 4px 18px;
    margin: 12px 0;
    max-width: 75%;
    margin-left: auto;
    text-align: left;
    box-shadow: 0 8px 20px rgba(37,99,235,0.28);
    font-size: 16px;
}

.bot-msg {
    background: rgba(255,255,255,0.07);
    color: white;
    padding: 14px 18px;
    border-radius: 18px 18px 18px 4px;
    margin: 12px 0;
    max-width: 78%;
    text-align: left;
    box-shadow: 0 8px 20px rgba(0,0,0,0.18);
    font-size: 16px;
    line-height: 1.6;
}

.tip-box {
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 16px;
    padding: 18px;
    margin-bottom: 22px;
    color: #cbd5e1;
    font-size: 15px;
}

div.stButton > button {
    width: 100%;
    height: 52px;
    font-size: 18px;
    font-weight: 700;
    border-radius: 14px;
    border: none;
    background: linear-gradient(90deg, #0ea5e9, #2563eb);
    color: white;
    transition: 0.3s ease-in-out;
}

div.stButton > button:hover {
    transform: scale(1.02);
    box-shadow: 0 8px 20px rgba(37,99,235,0.35);
}

.footer {
    text-align: center;
    color: #94a3b8;
    font-size: 14px;
    margin-top: 30px;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# CHATBOT LOGIC
# -----------------------------
def chatbot_response(user_input):
    user_input = user_input.lower().strip()

    # Greetings
    if any(word in user_input for word in ["hi", "hello", "hey", "hii", "hy"]):
        return "Hello! 👋 How can I help you today?"

    # Identity
    elif "your name" in user_input or "who are you" in user_input:
        return "I am a Smart Rule-Based AI Chatbot 🤖"

    elif "who made you" in user_input or "who created you" in user_input:
        return "I was created using Python and Streamlit as part of an AI internship project."

    # Help
    elif "help" in user_input or "what can you do" in user_input:
        return """I can answer questions about:
- Python
- AI
- Machine Learning
- Data Science
- Streamlit
- GitHub
- Internships

Try asking:
- What is Python?
- What is AI?
- What is Machine Learning?
- What is Streamlit?
"""

    # Tech / AI topics
    elif "what is python" in user_input:
        return "Python is a high-level programming language known for its simplicity and wide use in web development, automation, data science, and AI."

    elif "what is ai" in user_input or "what is artificial intelligence" in user_input:
        return "Artificial Intelligence (AI) is the simulation of human intelligence in machines so they can learn, reason, and make decisions."

    elif "what is machine learning" in user_input:
        return "Machine Learning is a branch of AI where systems learn patterns from data and make predictions without being explicitly programmed for every task."

    elif "what is data science" in user_input:
        return "Data Science is the field of extracting useful insights from data using statistics, programming, and machine learning."

    elif "what is streamlit" in user_input:
        return "Streamlit is a Python framework used to build interactive web apps for data science, machine learning, and AI projects quickly."

    elif "what is github" in user_input:
        return "GitHub is a cloud-based platform used to store, manage, and share code using Git version control."

    elif "what is internship" in user_input:
        return "An internship is a short-term practical work experience program where students or beginners learn industry skills by working on real tasks or projects."

    # Fun / polite
    elif "how are you" in user_input:
        return "I'm doing great 😄 Thanks for asking!"

    elif "joke" in user_input:
        return "Why do programmers prefer dark mode? 😄 Because light attracts bugs!"

    elif "thank you" in user_input or "thanks" in user_input:
        return "You're welcome 😊"

    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! 👋 Have a great day."

    # Default fallback
    else:
        return """Sorry, I don't have an answer for that yet. 😅

Try asking things like:
- What is Python?
- What is AI?
- What is Machine Learning?
- What is Streamlit?
- What is GitHub?
"""

# -----------------------------
# SESSION STATE
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# -----------------------------
# HEADER
# -----------------------------
st.markdown('<div class="main-title">🤖 Smart AI Chatbot</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">An interactive rule-based chatbot built using Python & Streamlit</div>', unsafe_allow_html=True)

# -----------------------------
# TIP BOX
# -----------------------------
st.markdown("""
<div class="tip-box">
<b>💡 Try asking:</b><br>
What is Python? • What is AI? • What is Machine Learning? • What is Streamlit? • Tell me a joke
</div>
""", unsafe_allow_html=True)

# -----------------------------
# DISPLAY CHAT
# -----------------------------
st.markdown('<div class="chat-wrapper">', unsafe_allow_html=True)

for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f'<div class="user-msg">{msg["content"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="bot-msg">{msg["content"]}</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# -----------------------------
# INPUT SECTION
# -----------------------------
user_input = st.text_input("Type your message...", placeholder="Ask something like: What is Python?")

if st.button("Send"):
    if user_input.strip():
        st.session_state.messages.append({"role": "user", "content": user_input})
        response = chatbot_response(user_input)
        st.session_state.messages.append({"role": "bot", "content": response})
        st.rerun()

# -----------------------------
# FOOTER
# -----------------------------
st.markdown('<div class="footer">Built with Python & Streamlit</div>', unsafe_allow_html=True)