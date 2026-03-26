import gradio as gr
from backend import run_travel_planner

# ==============================
# Chat Function
# ==============================
def chat(user_message, history):
    if history is None:
        history = []

    if not user_message.strip():
        return history, history

    response = run_travel_planner(user_message)

    # ✅ New format 
    history.append({"role": "user", "content": user_message})
    history.append({"role": "assistant", "content": response})

    return history, history


# ==============================
# UI Design 
# ==============================
with gr.Blocks() as demo:

    gr.Markdown("## ✈️ AI Travel Planner")
    gr.Markdown("Plan routes, cost & itinerary in seconds 🚀")

    chatbot = gr.Chatbot(height=450)

    with gr.Row():
        txt = gr.Textbox(
            placeholder="Example: 2 day trip Chennai to Bangalore under 5000",
            scale=4
        )
        btn = gr.Button("Send 🚀")

    clear = gr.Button("Clear Chat ❌")

    # Actions
    btn.click(chat, inputs=[txt, chatbot], outputs=[chatbot, chatbot])
    txt.submit(chat, inputs=[txt, chatbot], outputs=[chatbot, chatbot])
    clear.click(lambda: [], None, chatbot)


# ==============================
# Launch
# ==============================
if __name__ == "__main__":
    demo.launch(
        theme=gr.themes.Soft(),
        css="""
        body {background-color: #0f172a;}
        """
    ) 