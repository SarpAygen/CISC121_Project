import random
import gradio as gr

def choose_size_by_difficulty(difficulty: str) -> int:
    """Return a random array size based on difficulty."""
    if difficulty == "Easy":
        return random.randint(5, 10)
    elif difficulty == "Medium":
        return random.randint(10, 15)
    else: 
        return random.randint(15, 20) #For hard diffucilty


def start_new_game(difficulty="Easy"):
    """
    Initialize a new game and return full initial state.
    """
    size = choose_size_by_difficulty(difficulty)

    # Make sure size is at least 2
    size = max(size, 2)

    array = sorted(random.sample(range(1, 200), size)) #Numbers in array is between 1-200
    target = random.choice(array)

    low = 0
    high = len(array) - 1
    steps = 0
    mistakes = 0
    game_over = False

    message = (
        f"New game started (Difficulty: **{difficulty}**)\n\n"
        f"- Array size: **{size}** indices (0 to {size - 1})\n"
        f"- Your job: act as the **binary search algorithm**.\n\n"
        f"Target to find: **{target}**\n"
        f"Current search range: low = {low}, high = {high}\n\n"
        f"Each turn:\n"
        f"1. Choose the correct mid index based on low and high.\n"
        f"2. Decide if the target is in the left half, right half, or found at mid."
    )

    visualization = render_array(array, low, high, None, target)

    return (array, target,low,high,steps,mistakes,game_over,difficulty,message,visualization)


def render_array(array, low, high, mid, target):
    """Visual display of list, indices, highlight mid and active range."""
    index_line = "Index: "
    value_line = "Value: "

    for i, val in enumerate(array): #Loop through each element
        idx_str = f"{i:2d}"
        val_str = f"{val:2d}"

        if low <= i <= high:  #checks if index is in the current search range and wraps it in brackets if it is for ease of understanding
            idx_str = f"[{idx_str}]" 
            val_str = f"[{val_str}]"

        if mid is not None and i == mid: #checks if the mid is valid and if it is the one you checked If this entry is the mid, wrap it in markdown bold.
            idx_str = f"**{idx_str}**"
            val_str = f"**{val_str}**"

        index_line += f"{idx_str}  " #appends the formatted index text to a display line.
        value_line += f"{val_str}  "

    return (
        f"### Current Array\n"
        f"{index_line}\n\n"
        f"{value_line}\n\n"
        f"Target: **{target}**\n"
        f"Range: low = {low}, high = {high}\n"
    )


def take_step(chosen_mid,direction,array,target,low,high,steps,mistakes,game_over,difficulty,):

    # If game is already over
    if game_over:
        msg = " Game is over. Click **New Game** to start a new round."
        Visual = render_array(array, low, high, None, target)
        return (array, target, low, high, steps, mistakes, game_over,difficulty, msg, Visual)

    # Validate inputs
    if chosen_mid is None or direction is None: #make sure the user inputs a number and a direction
        msg = "Please choose a mid index and a direction."
        Visual = render_array(array, low, high, None, target)
        return (array, target, low, high, steps, mistakes, game_over,difficulty, msg, Visual)

    try:
        chosen_mid = int(chosen_mid)
    except ValueError: #Error Handling
        msg = "Mid index must be an integer."
        Visual = render_array(array, low, high, None, target)
        return (array, target, low, high, steps, mistakes, game_over,difficulty, msg, Visual)

    if chosen_mid < 0 or chosen_mid >= len(array): #Makes sure the number you chose is actually in the range of the list and not below 0
        mistakes += 1
        msg = f"Mid index out of bounds. Valid indices are 0 to {len(array) - 1}."
        Visual = render_array(array, low, high, None, target)
        return (array, target, low, high, steps, mistakes, game_over,difficulty, msg, Visual)

    feedback = []

    # If the range is already invalid
    if low > high:
        game_over = True
        msg = "Search range is empty (low > high). Treasure is lost. Game over."
        Visual = render_array(array, low, high, None, target)
        return (array, target, low, high, steps, mistakes, game_over, difficulty, msg, Visual)

    # True binary search mid
    correct_mid = (low + high) // 2

    # Check mid correctness
    if chosen_mid != correct_mid:
        mistakes += 1
        feedback.append(
            f" Incorrect mid. You chose {chosen_mid}, "
            f"but the correct mid for low={low}, high={high} is **{correct_mid}**."
        )
        feedback.append("Remember: `mid = (low + high) // 2`.")
        msg = "\n".join(feedback)
        Visual = render_array(array, low, high, None, target)
        return (array, target, low, high, steps, mistakes, game_over,difficulty, msg, Visual)

    # If mid is correct apply binary search logic
    mid = correct_mid
    mid_value = array[mid]
    feedback.append(f"Correct mid: mid = {mid}, value = {mid_value}")

    # Determine correct direction from mid value
    if mid_value == target:
        correct_dir = "Found at mid"
    elif mid_value < target:
        correct_dir = "Right half"
        # target is in larger values (indices > mid)
    else:
        correct_dir = "Left half"
        # target is in smaller values (indices < mid)

    # Check direction correctness
    if direction != correct_dir:
        mistakes += 1
        feedback.append(f"Wrong direction. Correct answer is **{correct_dir}**.")
        msg = "\n".join(feedback)
        Visual = render_array(array, low, high, mid, target)
        return (array, target, low, high, steps, mistakes, game_over,difficulty, msg, Visual)

    # If the direction is correct complete a step
    steps += 1
    feedback.append(f"Step #{steps} successful!")

    if correct_dir == "Found at mid": #found the correct mid
        game_over = True
        feedback.append(
            f"🎉 You found **{target}** in {steps} steps with {mistakes} mistake(s)!"
        )
        msg = "\n".join(feedback)
        Visual = render_array(array, low, high, mid, target)
        return (array, target, low, high, steps, mistakes, game_over,difficulty, msg, Visual)

    # Update search range
    if correct_dir == "Right half":
        low = mid + 1
    else:  # Left half
        high = mid - 1

    feedback.append(f"New range: low = {low}, high = {high}")
    msg = "\n".join(feedback)
    Visual = render_array(array, low, high, None, target)

    # If range collapses after this step
    if low > high:
        game_over = True
        feedback.append("\nThe search range is now empty (low > high). Something went wrong. Game over.")
        msg = "\n".join(feedback)

    return (array, target, low, high, steps, mistakes, game_over,difficulty, msg, Visual)

def build_interface(): #UI building
    with gr.Blocks() as game:
        gr.Markdown("Binary Search Treasure Hunt")
        gr.Markdown(
            "Use **binary search logic** to find the target.\n\n"
            "- **Difficulty changes the array size**:\n"
            "  - Easy: 5–10 elements\n"
            "  - Medium: 10–15 elements\n"
            "  - Hard: 15–20 elements\n"
            "- Every time you click **New Game**, a new random-sized array is generated."
        )

        # Difficulty selector
        difficulty_select = gr.Radio(
            ["Easy", "Medium", "Hard"],
            value="Easy",
            label="Select difficulty"
        )

        # Persistent state
        state_array = gr.State()
        state_target = gr.State()
        state_low = gr.State()
        state_high = gr.State()
        state_steps = gr.State()
        state_mistakes = gr.State()
        state_game_over = gr.State()
        state_difficulty = gr.State()

        with gr.Row():
            visualization = gr.Markdown()
            with gr.Column():
                chosen_mid = gr.Number(label="Your chosen mid index", precision=0)
                direction = gr.Radio(
                    ["Left half", "Right half", "Found at mid"],
                    label="Where is the target?"
                )
                take_step_btn = gr.Button("Take Step")
                new_game_btn = gr.Button("New Game")
                message_box = gr.Markdown()


        def _new_game(diff): #Make sure the new game has the correct difficulty
            return start_new_game(difficulty=diff)

        new_game_btn.click(_new_game,inputs=[difficulty_select],outputs=[state_array,state_target,state_low,state_high,state_steps,state_mistakes,state_game_over,state_difficulty,message_box,visualization,])

        def _take_step(chosen_mid_val, direction_val, array, target, low, high, steps, mistakes, game_over, diff):
            return take_step(chosen_mid_val,direction_val,array,target,low,high,steps,mistakes,game_over,diff)

        take_step_btn.click(_take_step,inputs=[chosen_mid,direction,state_array,state_target,state_low,state_high,state_steps,state_mistakes,state_game_over,state_difficulty],outputs=[state_array,state_target,state_low,state_high,state_steps,state_mistakes,state_game_over,state_difficulty,message_box,visualization])

        # Start with an initial game on load
        game.load(_new_game,inputs=[difficulty_select],outputs=[state_array,state_target,state_low,state_high,state_steps,state_mistakes,state_game_over,state_difficulty,message_box,visualization])

    return game


if __name__ == "__main__":
    game = build_interface()
    game.launch()
