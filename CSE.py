import streamlit as st 
from google import genai
from dotenv import load_dotenv



client = genai.Client()


system_prompt = """You are 'Brew', the friendly assistance at CSE Canteen.
Talk in a warm, casual Hinglish tone. Keep answers short (2-4 lines).

Menu:
- Smooth      Rs.20
- Diet Coke   Rs.70
- Espresso    Rs.180
- Cappuccino  Rs.220
- Latte       Rs.240
- Cold Brew   Rs.260

- Add-ons: Croissant Rs.120, Brownie Rs.150, Bagel Rs.130

Rules:
- Suggest drinks based on the customer's mood, weather or taste.
- Only recommend items from the menu.
- If asked something unrelated, politely say i am a assistant."""

WELCOME = "Welcome to The CSE Canteen! Please tell me how can I help you today?."


#print(interaction.output_text)
st.set_page_config(page_title="CSE Canteen",page_icon="🍽️")

#st.title("👋 Welcome of Online asistance of CSE Canteen ")
#st.caption("Most preffred Canteen of our YCCE ",text_alignment="right")
#import streamlit as st
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Nunito:wght@700;800;900&display=swap');

    .bounce-wrap {
        background: linear-gradient(160deg, #fffbeb 0%, #fff7ed 50%, #ffedd5 100%);
        border: 2px solid #fed7aa;
        border-radius: 20px;
        padding: 32px 40px 24px;
        text-align: center;
        position: relative;
        overflow: hidden;
        box-shadow: 0 8px 24px rgba(234, 88, 12, 0.08);
        margin-bottom: 24px;
    }

    /* Floating food emojis in corners */
    .bounce-wrap::before {
        content: '🍔';
        position: absolute;
        top: 12px;
        left: 18px;
        font-size: 1.6rem;
        opacity: 0.5;
        transform: rotate(-15deg);
    }
    .bounce-wrap::after {
        content: '🍕';
        position: absolute;
        top: 12px;
        right: 18px;
        font-size: 1.6rem;
        opacity: 0.5;
        transform: rotate(12deg);
    }

    /* Steam wisps above title */
    .steam {
        display: flex;
        justify-content: center;
        gap: 6px;
        margin-bottom: 6px;
        height: 24px;
    }
    .steam span {
        width: 3px;
        height: 18px;
        background: #fdba74;
        border-radius: 3px;
        animation: steam-rise 2s ease-in-out infinite;
    }
    .steam span:nth-child(1) { animation-delay: 0s; }
    .steam span:nth-child(2) { animation-delay: 0.3s; height: 22px; }
    .steam span:nth-child(3) { animation-delay: 0.6s; }
    @keyframes steam-rise {
        0%, 100% { opacity: 0.3; transform: translateY(0) scaleY(1); }
        50% { opacity: 0.8; transform: translateY(-4px) scaleY(1.2); }
    }

    .bounce-wrap h1 {
        font-family: 'Nunito', sans-serif;
        font-size: 2.8rem;
        font-weight: 900;
        color: #7c2d12;
        margin: 0;
        letter-spacing: -1px;
    }
    .bounce-wrap h1 .letter {
        display: inline-block;
        animation: bounce 2.5s ease-in-out infinite;
    }
    .bounce-wrap h1 .letter:nth-child(odd) { animation-delay: 0.15s; }
    .bounce-wrap h1 .letter:nth-child(3n) { animation-delay: 0.3s; }
    @keyframes bounce {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-5px); }
    }

    /* Wavy underline */
    .wavy {
        width: 160px;
        height: 14px;
        margin: 12px auto 0;
        background: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='160' height='14'%3E%3Cpath d='M0 7 Q20 0 40 7 T80 7 T120 7 T160 7' stroke='%23ea580c' stroke-width='3' fill='none' stroke-linecap='round'/%3E%3C/svg%3E") no-repeat center;
    }

    /* Subtitle with dot separators */
    .sub-row {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 8px;
        margin-top: 10px;
    }
    .sub-row .dot {
        width: 5px;
        height: 5px;
        background: #f97316;
        border-radius: 50%;
    }
    .sub-row p {
        font-family: 'Nunito', sans-serif;
        font-size: 0.9rem;
        color: #c2410c;
        font-weight: 700;
        letter-spacing: 1.5px;
        margin: 0;
    }

    /* Bottom emoji strip */
    .emoji-strip {
        margin-top: 14px;
        font-size: 1.1rem;
        letter-spacing: 8px;
        opacity: 0.7;
    }
</style>

<div class="bounce-wrap">
    <div class="steam"><span></span><span></span><span></span></div>
    <h1>
        <span class="letter">C</span><span class="letter">S</span><span class="letter">E</span>
        <span class="letter">&nbsp;</span>
        <span class="letter">C</span><span class="letter">a</span><span class="letter">n</span><span class="letter">t</span><span class="letter">e</span><span class="letter">e</span><span class="letter">n</span>
    </h1>
    <div class="wavy"></div>
    <div class="sub-row">
        <span class="dot"></span>
        <p>YCCE Food Buddy</p>
        <span class="dot"></span>
    </div>
    <div class="emoji-strip">🍛 🥤 🍩 ☕ 🌮</div>
</div>
""", unsafe_allow_html=True)   







if "message" not in st.session_state:
    st.session_state.message=[]
    st.session_state.message.append({"role":"assistant","content":WELCOME})
#st.sidebar.header("📝 __MENU__")
with st.sidebar:
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Nunito:wght@700;800;900&display=swap');

        .menu-wrap {
            background: linear-gradient(160deg, #fffbeb 0%, #fff7ed 50%, #ffedd5 100%);
            border: 2px solid #fed7aa;
            border-radius: 16px;
            padding: 20px 20px 16px;
            text-align: center;
            position: relative;
            overflow: hidden;
            box-shadow: 0 4px 12px rgba(234, 88, 12, 0.08);
            margin-bottom: 16px;
        }

        /* Corner food emojis */
        .menu-wrap::before {
            content: '🍕';
            position: absolute;
            top: 8px;
            left: 10px;
            font-size: 1.1rem;
            opacity: 0.45;
            transform: rotate(-12deg);
        }
        .menu-wrap::after {
            content: '🍔';
            position: absolute;
            top: 8px;
            right: 10px;
            font-size: 1.1rem;
            opacity: 0.45;
            transform: rotate(10deg);
        }

        /* Mini steam */
        .menu-steam {
            display: flex;
            justify-content: center;
            gap: 4px;
            margin-bottom: 4px;
            height: 16px;
        }
        .menu-steam span {
            width: 2.5px;
            height: 12px;
            background: #fdba74;
            border-radius: 2px;
            animation: m-steam 2s ease-in-out infinite;
        }
        .menu-steam span:nth-child(1) { animation-delay: 0s; }
        .menu-steam span:nth-child(2) { animation-delay: 0.25s; height: 15px; }
        .menu-steam span:nth-child(3) { animation-delay: 0.5s; }
        @keyframes m-steam {
            0%, 100% { opacity: 0.3; transform: translateY(0) scaleY(1); }
            50% { opacity: 0.8; transform: translateY(-3px) scaleY(1.15); }
        }

        .menu-wrap h3 {
            font-family: 'Nunito', sans-serif;
            font-size: 1.5rem;
            font-weight: 900;
            color: #7c2d12;
            margin: 0;
            letter-spacing: -0.5px;
        }
        .menu-wrap h3 .letter {
            display: inline-block;
            animation: m-bounce 2.5s ease-in-out infinite;
        }
        .menu-wrap h3 .letter:nth-child(odd) { animation-delay: 0.12s; }
        .menu-wrap h3 .letter:nth-child(3n) { animation-delay: 0.24s; }
        @keyframes m-bounce {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-4px); }
        }

        /* Mini wavy line */
        .menu-wavy {
            width: 80px;
            height: 10px;
            margin: 8px auto 0;
            background: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='80' height='10'%3E%3Cpath d='M0 5 Q10 0 20 5 T40 5 T60 5 T80 5' stroke='%23ea580c' stroke-width='2.5' fill='none' stroke-linecap='round'/%3E%3C/svg%3E") no-repeat center;
        }

        /* Subtitle */
        .menu-sub {
            font-family: 'Nunito', sans-serif;
            font-size: 0.75rem;
            color: #c2410c;
            font-weight: 700;
            letter-spacing: 1.5px;
            margin-top: 6px;
        }

        /* Emoji strip */
        .menu-strip {
            margin-top: 10px;
            font-size: 0.9rem;
            letter-spacing: 6px;
            opacity: 0.6;
        }
    </style>

    <div class="menu-wrap">
        <div class="menu-steam"><span></span><span></span><span></span></div>
        <h3>
            <span class="letter">M</span><span class="letter">e</span><span class="letter">n</span><span class="letter">u</span>
        </h3>
        <div class="menu-wavy"></div>
        <p class="menu-sub">Pick your craving</p>
        <div class="menu-strip">🍛 🥤 🍩 ☕</div>
    </div>
    """, unsafe_allow_html=True)

    
 
st.write()
st.write()
st.sidebar.write("1. Diet Coke - 70")
st.sidebar.write("2. Smooth - 20")
st.sidebar.write("3. Espresso - 180")
st.sidebar.write("4. Cappuccino - 220")
st.sidebar.write("5. Latte - 240")
st.sidebar.write("6. Cold Brew - 260")
st.divider()
for msg in st.session_state.message:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])


prompt=st.chat_input("Chat here...")

if prompt:
    with st.chat_message("user"):
        st.write(prompt)
    st.session_state.message.append({"role":"user","content":prompt})

    conversation=""
    for msg in st.session_state.message:
        conversation = conversation + msg["role"] + msg["content"] + "\n\n"
      
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response= client.interactions.create(
                model="gemini-3.5-flash-lite",
                system_instruction=system_prompt,
                input=conversation
                )
            st.write(response.output_text)
            st.session_state.message.append({"role":"assistant","content":response.output_text})