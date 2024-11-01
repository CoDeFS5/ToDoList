import streamlit as st

# Set up an empty task list if it doesn't already exist
if "tasks" not in st.session_state:
    st.session_state.tasks = []

st.title("To-Do List App")

# Add a new task if input is provided and button is pressed
new_task = st.text_input("Add a new task")
if st.button("Add Task"):
    if new_task:
        st.session_state.tasks.append(new_task)
        st.text_input("Add a new task", value="", key="reset")  # Reset input field

# Display and manage tasks
for i, task in enumerate(st.session_state.tasks):
    col1, col2 = st.columns([0.8, 0.2])
    with col1:
        st.write(task)
    with col2:
        if st.button("Delete", key=f"delete_{i}"):
            del st.session_state.tasks[i]  #
