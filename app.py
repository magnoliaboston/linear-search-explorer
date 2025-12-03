import gradio as gr

#Linear Search Snack Finder
def linear_search_snack(pantry, snack_target):
    steps = []

    for index, snack in enumerate(pantry):
        steps.append(f" Checking slot **{index}** → `{snack}`")
        #match found and snack bounce 
        if snack.lower().strip() == snack_target.lower().strip():
            steps.append(f"\n MATCH FOUND! `{snack}` is at position **{index}**!\n")
            steps.append(
                "<div class='snack-bounce'>🍫</div>" #snack image 
                "<div class='snack-glow'>Snack Secured!</div>" #displayed to user 
            )
            return "\n".join(steps)
    #if snack is not in the pantry - display to user 
    steps.append("\n Snack not in the pantry! Try again! 🍪")
    return "\n".join(steps)


def run_snack_finder(pantry_input, target_input):
    if pantry_input.strip() == "":
        pantry = []
    else:
        pantry = [item.strip() for item in pantry_input.split(",")]

    if target_input.strip() == "":
        return "⚠️ Please enter a snack you're craving!" #display to user 

    return linear_search_snack(pantry, target_input)


#APP UI
with gr.Blocks() as demo:
    #Visuals for code to make it more appealing and interactive 
    gr.HTML("""
    <style>
    * { font-family: "Comic Sans MS", cursive !important; }
    /* Background: bolder, more vibrant */
    body, .gradio-container {
        background: radial-gradient(circle at top, #3a7fff, #1a3fcc, #081a66);
        background-attachment: fixed;
    }
    /* Title text with navy color and subtle glow */
    .title {
        font-size: 4.1em;
        text-align: center;
        font-weight: bold;
        color: #0a1a3f; /* navy text */
        text-shadow: 0 0 8px #0a1a3f, 0 0 16px #0a1a3f; /* subtle navy glow */
        margin-top: 20px;
        margin-bottom: 10px;
    }
    /* Glowing emojis */
    .snack-emoji {
        display: inline-block;
        font-size: 1em;  /* small enough to fit in one line */
        margin: 0 6px;
        filter: drop-shadow(0 0 4px #ffffff)
                drop-shadow(0 0 8px #ffffff)
                drop-shadow(0 0 12px #ffffff);
        animation: pop 1.5s infinite ease-in-out;
    }
    @keyframes pop {
        0% { transform: scale(1); }
        50% { transform: scale(1.25); }
        100% { transform: scale(1); }
    }
    .subtitle {
        text-align:center;
        font-size: 1.7em;
        margin-bottom: 25px;
        color: #001f4d !important; 
        font-weight: 600;
    }
    /* Black search button */
    .neon-btn {
        background: #000000;  /* black button */
        color: white !important;
        font-size: 1.7em;
        border-radius: 12px;
        box-shadow: 0 0 15px #ffffff; /* subtle white glow */
        transition: 0.2s;
    }
    .neon-btn:hover {
        box-shadow: 0 0 25px #ffffff;
        transform: scale(1.05);
    }
    .snack-glow {
        font-size: 1.8em;
        text-align: center;
        padding-top: 10px;
        color: #5c89ff;
        text-shadow: 0 0 15px #ff7ae6;
    }
    .snack-bounce {
        font-size: 4em;
        animation: bounce 0.8s infinite alternate;
        text-align: center;
        -webkit-text-fill-color: initial !important;
        color: initial !important;
        text-shadow: none !important;
        filter: drop-shadow(0 0 8px #ffffff);
    }
    @keyframes bounce {
        from { transform: translateY(0); }
        to   { transform: translateY(-18px); }
    }
    /* Blue textboxes */
    input[type="text"],
    textarea {
        background: rgba(0, 102, 255, 0.85) !important;
        color: white !important;
        border: 2px solid #003399 !important;
        border-radius: 10px !important;
        padding: 12px !important;
        box-shadow: 0 0 10px rgba(0, 102, 255, 0.8);
    }
    label {
        color: #d6e6ff !important;
        font-weight: bold;
    }
    .gr-textbox {
        width: 100% !important;
        height: 120px !important;
    }
    </style>
    """)

    #title with emojis
    gr.HTML("""
    <div class='title'>
        <span class='snack-emoji'>🍪</span>
        <span class='snack-emoji'>🍫</span>
        <span class='snack-emoji'>🍭</span>
        &nbsp; Snack Searcher &nbsp;
        <span class='snack-emoji'>🍭</span>
        <span class='snack-emoji'>🍫</span>
        <span class='snack-emoji'>🍪</span>
    </div>
    <div class='subtitle'>Search your pantry with Linear Search</div>
    """)

    #Two even textboxes
    with gr.Row(equal_height=True):
        pantry_box = gr.Textbox(
            label="Your Virtual Pantry ...", #left textbox title 
            placeholder="ex. chocolate, chips, cookies, gummies", #example inputs for user 
            lines=3,
        )

        target_box = gr.Textbox(
            label="Snack You're Craving ...", #right textbox title 
            placeholder="Type a snack…", #prompt user 
            lines=3,
        )
    #search button to find users snack 
    search_button = gr.Button("🔍 Search for Snack", elem_classes="neon-btn")
    #explain to user where snack location will appear 
    output_box = gr.Markdown("Results will appear here!", elem_id="results-box")
    #search for snack 
    search_button.click(
        fn=run_snack_finder,
        inputs=[pantry_box, target_box],
        outputs=[output_box]
    )
#launch app 
demo.launch()

