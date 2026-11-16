FitDeficit: Engineering Calorie Architecture

'FitDeficit: Engineering Calorie Architecture' is a calorie deficit tracker. The user types in their details and clicks Calculate, and the app shows a daily and weekly calorie limit.

1. Events.
Three things can happen in the app: clicking Calculate, clicking Reset, and pressing Enter. The buttons are connected with command= and the Enter key is connected with bind().

2. Callbacks.
Each event runs a function. Calculate runs calculate_deficit(), Reset runs reset_application(), and Enter runs press_enter(), which just calls calculate_deficit(). We write the function names without parentheses so they run when the event happens, not when the program starts.

3. Widget interaction.
calculate_deficit() reads the entry boxes with get(), then changes other widgets. It uses config() to update the result labels and the feedback label, and insert() to add a line to the history box. The history box is locked so users can't type in it, so we unlock it before inserting and lock it again after. Reset uses delete(0, tk.END) to empty the entries.

4. Input Validation.
Before doing any math, the app cleans the input with strip() and upper(). Then it checks that no field is empty, that age, weight, and height are numbers (using try/except), that the numbers are inside a logical range, and that Sex and Activity have allowed values. If a check fails, the feedback label shows what's wrong in red and the function stops with return. A successful calculation shows a green message.
