import time
import gradio as gr

API_BASE_URL = "http://localhost:8000/qna"

def request_chat_api(user_message: str) -> str:
    url = API_BASE_URL
    resp = requests.post(
        url,
        json={
            "user_message": user_message,
        },
    )
    resp = resp.json()
    return resp["answer"]

def chat_bot(user_message):
    # Display user message
    chat_history.append({"role": "user", "content": user_message})

    # Display assistant response
    assistant_response = request_chat_api(user_message)
    chat_history.append({"role": "assistant", "content": assistant_response})

    return assistant_response

def simulate_typing(response):
    for char in response:
        time.sleep(0.05)
        yield char

def chat_main():
    return gr.Interface(
        fn=chat_bot,
        inputs="text",
        outputs="text",
        live=True,
        examples=[
            ["Hello, how can I help you?"],
            ["What is the main cause of the bug?"],
            ["Could you please suggest some enhancements?"],
        ],
        title="Simple Chat",
        description="Chat with the assistant to get help or ask questions.",
        interpretation="default",
    )

if __name__ == "__main__":
    chat_interface = chat_main()
    chat_interface.launch()
