import streamlit as st
import openai
import time

openai.api_key = "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"

# CASE 1:
# `Is this code solving the task description`? And if not, how close is this code to the task description?
def assess_closeness(task_description, code_solution):
    prompt = f"How Well and How Close Code Ninja: {task_description}\n\nCode Solution:\n{code_solution}\n\nDoes this code perfectly solve the task? If not, provide details. Additionally, what percentage of the code's closeness to the task description would you give? If the percentage is less than 100%, please provide feedback or suggestions on how to improve it."
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=500,
        n=1,
        stop=None,
        temperature=0.7,
    )
    response = response.choices[0].text.strip() if response.choices else None
    return response if response else "Error: Unable to retrieve a valid response from the API, prompt is so long, please pass the code in parts."


# CASE 2:
# Is this code `modularized`?
def assess_modularity(code_solution):
    prompt = f"Code Modularity Masterpiece:\n{code_solution}\n\nHow well is this code modularized? Provide insights into the modularity of the code."
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7,
    )
    response = response.choices[0].text.strip() if response.choices else None
    return response if response else "Error: Unable to retrieve a valid response from the API, prompt is so long, please pass the code in parts."

# CASE 3:
# How efficient is this code from the `performance`, `clean code`, and `readability` perspective?
def assess_efficiency(code_solution):
    prompt = f"Code Efficient Analysis:\n{code_solution}\n\nAssess the code in terms of performance, clean code, and readability. For performance: consider efficiency and speed. For clean code: focus on simplicity, clarity, and adherence to coding standards. For readability: think about how easily someone else could understand and maintain this code ninja."
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=500,
        n=1,
        stop=None,
        temperature=0.7,
    )
    response = response.choices[0].text.strip() if response.choices else None
    return response if response else "Error: Unable to retrieve a valid response from the API, prompt is so long, please pass the code in parts."

# CASE 4:
# -I need make sure that the code contains the main concepts like `Preprocessing`, `splitting the data`, `training the model`, `testing the model`, and any other section you see suitable.
def validate_main_concepts(code_solution):
    prompt = f"code_solution:\n{code_solution}\n\nEnsure that the provided code encompasses the main concepts required, including 'Preprocessing, splitting the data, training the model and testing the model'. Provide feedback if any of these concepts are absent, and suggest appropriate techniques to enhance the robustness of this code."
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1200,
        n=1,
        stop=None,
        temperature=0.7,
    )
    response = response.choices[0].text.strip() if response.choices else None
    return response if response else "Error: Unable to retrieve a valid response from the API, prompt is so long, please pass the code in parts."

# CASE 5:
# -`Ensure that the code is AI-generated`
def ensure_ai_generated(code_solution):
    prompt = f"Code Origin Verification:\n{code_solution}\n\nVerify if the provided code is AI-generated if yes Confirm its authenticity and acknowledge. If code appears manually written, provide appropriate feedback on any suspicious elements or reasons for the manual appearance.."
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=300,
        n=1,
        stop=None,
        temperature=0.7,
    )
    response = response.choices[0].text.strip() if response.choices else None
    return response if response else "Error: Unable to retrieve a valid response from the API, prompt is so long, please pass the code in parts."

# Streamlit GUI
def main():
    st.title("Code Evaluator")
    task_description = st.text_area("Task Description:")
    code_solution = st.text_area("Code Solution:")

    if st.button("Evaluate Code"):
        closeness_result = assess_closeness(task_description, code_solution)
        time.sleep(10) # To handel api key, not to run more than 3 times in 20 seconds.
        modularity_result = assess_modularity(code_solution)
        time.sleep(10)
        quality_result = assess_efficiency(code_solution)
        time.sleep(10)
        validation_result = validate_main_concepts(code_solution)
        time.sleep(10)
        generation_ai_result = ensure_ai_generated(code_solution)
        
        st.write(f"**Closeness Assessment:**\n\n{closeness_result}")
        st.write(f"**Modularity Assessment:**\n\n{modularity_result}")
        st.write(f"**Code Quality Assessment:**\n\n{quality_result}")
        st.write(f"**Main Concepts Validation:**\n\n{validation_result}")
        st.write(f"**Generation AI Check:**\n\n{generation_ai_result}")

if __name__ == "__main__":
    main()
