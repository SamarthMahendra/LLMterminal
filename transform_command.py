from openai import OpenAI
import os


def transform_command(user_input, api_key=None):
    if api_key:
        os.environ['OPENAI_API_KEY'] = api_key
        # print("OPENAI_API_KEY has been set successfully.")
    else:
        # Check if the API key is already set in the environment
        existing_key = os.getenv('OPENAI_API_KEY')
        if existing_key:
            print("Using existing OPENAI_API_KEY from environment.")
        else:
            raise ValueError("API key not provided and OPENAI_API_KEY is not set in the environment.")

    client = OpenAI()
    # Define the prompt for the LLM
    prompt = f"""You are an assistant that translates high-level instructions into exact shell commands.

Instruction: {user_input}

Output:
       ```bash
pip install scikit-learn
``` 
dont write anything else
Shell Command:"""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": prompt}
        ]
    )
    transformed_command = assistant_response = response.choices[0].message.content
    """
     ```bash
pip install scikit-learn
``` """
    import re
    # Remove the code block markdown
    transformed_command = re.sub(r'```bash\n', '', transformed_command)
    transformed_command = re.sub(r'\n```', '', transformed_command)

    return transformed_command
