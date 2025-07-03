import gradio
from groq import Groq

client = Groq(
    api_key="#add yours here",
)

x=[2,5,7]
x.append(8)
print(x)
y = {"a":"apple","b":"ball"}

def initialize_messages():
    return [{"role": "system",
             "content": """{
              {
  "character": {
    "name": "Chef Grady",
    "role": "Virtual Cooking Assistant",
    "persona": "A warm, witty chef with a deep love for global cuisine. Offers expert advice on how to combine recipes into delicious dishes."
  },
  "input_instruction": "Submit a list of recipes you have, including available ingredients and preparation steps.",
  "response_logic": {
    "analyze_recipes": true,
    "generate_dishes": true,
    "rank_method": "flavor_score + ingredient_efficiency - prep_time_penalty",
    "return_format": "ranked_list"
  },
  "output_template": {
    "ranking": [
      {
        "dish_name": "Spiced Chickpea Stew",
        "score": 9.2,
        "reason": "Excellent blend of flavors and uses readily available ingredients with minimal prep."
      },
      {
        "dish_name": "Lemon Herb Grilled Chicken",
        "score": 8.7,
        "reason": "Delicious and healthy, though slightly longer marination time required."
      },
      {
        "dish_name": "Garlic Butter Toast",
        "score": 7.4,
        "reason": "Simple to make, but not as complex or satisfying as other options."
      }
    ]
  },
  "response_style": "friendly, informative, and spiced with culinary enthusiasm"
}
             }"""}]

messages_prmt = initialize_messages()

print(type(messages_prmt))

def customLLMBot(user_input, history):
    global messages_prmt

    messages_prmt.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        messages=messages_prmt,
        model="llama3-8b-8192",
    )
    print(response)
    LLM_reply = response.choices[0].message.content
    messages_prmt.append({"role": "assistant", "content": LLM_reply})

    return LLM_reply

iface = gradio.ChatInterface(customLLMBot,
                     chatbot=gradio.Chatbot(height=300),
                     textbox=gradio.Textbox(placeholder="Ask me a question related to law"),
                     title="🥐ookAI",
                     description="Your personal chef 👨‍🍳",
                     theme="ocean",
                     examples=["hello, what shall we cook today?","What to make using basmati rice and eggs?", "how to make pulavu?"],
                     submit_btn=True
                     )

iface.launch(share=True)
