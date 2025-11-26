import gradio as gr

#Linear Search Explorer

def linear_search(values_list, target):
    """
    Performs linear search and returns either the
    step-by-step process or the final result.
    """
    steps = []
    
    for index, value in enumerate(values_list):
        steps.append(f"Checking index {index}: {value}")
        if value == target:
            steps.append(f"Item found at position {index}")
            return "\n".join(steps)
    
    steps.append("Item not found in the list")
    return "\n".join(steps)


#Function to handle user input

def search_interface(list_input, target_input):
    try:
        #Convert comma-separated input into a list of integers
        values = [int(item.strip()) for item in list_input.split(",")]
        target = int(target_input.strip())
    except ValueError:
        return "Please enter valid integers separated by commas."
    
    #Run linear search and return steps/results
    return linear_search(values, target)

#Gradio Interface

iface = gr.Interface(
    fn=search_interface,
    inputs=[
        gr.Textbox(label="Enter list (comma-separated)"),
        gr.Textbox(label="Enter target value")
    ],
    outputs=gr.Textbox(label="Linear Search Steps / Result"),
    title="Linear Search App",
    description="Enter a list of numbers and a target value. The app will show each step of the search and the final result.",
    theme="default"
)

#Launch the app
iface.launch()

