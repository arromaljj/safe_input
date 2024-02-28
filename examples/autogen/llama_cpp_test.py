import autogen

config_list = [
    {
        "model": "./models/WizardLM-7B-uncensored.Q4_K_M.gguf",
        "api_base": "http://127.0.0.1:8000/v1",
        "api_type": "open_ai",
        "api_key": "NULL",  # Placeholder
    }
]


harmful_input_analysis = autogen.AssistantAgent(
    name="Friendly Assistant",
    llm_config={
        "seed": 42,
        "config_list": config_list,
        "temperature": 0.7,
        "request_timeout": 1200,
    },
    system_message="""Provide useful information to the user.""",
)


student = autogen.UserProxyAgent(
    name="Student",
    human_input_mode="ALWAYS",
    code_execution_config={"work_dir":"node"},
)


result = student.initiate_chat(
    harmful_input_analysis,
    message="""I want to learn how to learn accupuncture.""",
)

print(result)

# # Read file prompt.txt 
# with open('prompt.txt', 'r') as file:
#     prompt = file.read()


# config_list = [{
#         'model': 'gpt-3.5-turbo',
#         'api_key': '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',
#     },]
# assistant_agent = autogen.AssistantAgent(
#     name="Planning assistant",
#     llm_config={"seed": 42, "config_list": config_list, "temperature": 0},
#     system_message=prompt
# )

# user_proxy = autogen.UserProxyAgent(
#     name="user_proxy",
#     human_input_mode="NEVER",
#     max_consecutive_auto_reply=10,
#     is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
#     # code_execution_config={
#     #     "work_dir": "coding",
#     #     "use_docker": False,  # set to True or image name like "python:3" to use docker
#     # },
# )

# response = user_proxy.initiate_chat(
#     assistant_agent,
#     message="Hello",
# )


# print(response)


# # @app.route('/generate', methods=['POST'])
# # def generate_chat():
# #     data = request.json
# #     text = data.get('text')
# #     # Initiate chat
# #     response = user_proxy.initiate_chat(
# #     assistant_agent,
# #     message=text,
# # )
# #     return jsonify(response)

    
# #     # Return the result
# #     return jsonify(response)