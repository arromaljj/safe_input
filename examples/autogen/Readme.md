# Autogen and LLama_Cpp Example 

- For testing out llama_cpp run the llama_cpp_test.py file. llama_cpp is the backend that will be used for running the models on your local machine
- For testing out autogen, run the following command first on a separate terminal and keep it running in the background
    - python -m server --model models/WizardLM-7B-uncensored.Q4_K_M.gguf  --host 127.0.0.1 --n_ctx 2048 --n_batch 128 --n_gpu_layers 35
    - make sure that your model is downloaded into the models directory. Update the path of the model in the config_list inside autogen_test.py file. You can find models on huggingface
    - Run the autogen_test.py file in the terminal to interact with the agent
    - Experiment with different models


