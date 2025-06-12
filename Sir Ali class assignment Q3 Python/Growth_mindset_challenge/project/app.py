import streamlit as st

# Initialize session state for tasks
if "tasks" not in st.session_state:
    st.session_state.tasks = []

# Initialize session state for editing
if "editing_index" not in st.session_state:
    st.session_state.editing_index = None

if "edited_text" not in st.session_state:
    st.session_state.edited_text = ""

# Title with Emoji
st.title("📝 TO-DO List App")

# Sidebar Heading
st.sidebar.header("📌 Manage Your Tasks")

# Task Input
new_task = st.sidebar.text_input("➕ Add a new task:", placeholder="Enter your task here...")

if st.sidebar.button("✅ Add Task"):
    if new_task.strip():
        st.session_state.tasks.append({"task": new_task, "completed": False})
        st.success("🎉 Task added successfully!")
    else:
        st.warning("⚠️ Task cannot be empty!")

# Display Tasks
st.subheader("🗂️ Your TO-DO List")
if not st.session_state.tasks:
    st.info("📭 No task added yet! Start by adding a task from the sidebar.")
else:
    for index, task in enumerate(st.session_state.tasks):
        col1, col2, col3 = st.columns([0.6, 0.2, 0.2])

        # Check if task is completed
        completed = col1.checkbox(f"✅ {task['task']}", task["completed"], key=f"check_{index}")
        if completed != task["completed"]:
            st.session_state.tasks[index]["completed"] = completed

        # Edit Task Button
        if col2.button("✏️ Edit", key=f"edit_{index}"):
            st.session_state.editing_index = index
            st.session_state.edited_text = task["task"]

        # Delete Task Button
        if col3.button("🗑️ Delete", key=f"delete_{index}"):
            del st.session_state.tasks[index]
            st.rerun()

    # Show Edit Input Field
    if st.session_state.editing_index is not None:
        st.subheader("✏️ Edit Task")
        edited_task = st.text_input("Update your task:", st.session_state.edited_text)

        col1, col2 = st.columns(2)
        if col1.button("💾 Save Changes"):
            st.session_state.tasks[st.session_state.editing_index]["task"] = edited_task
            st.session_state.editing_index = None
            st.session_state.edited_text = ""
            st.rerun()

        if col2.button("❌ Cancel"):
            st.session_state.editing_index = None
            st.session_state.edited_text = ""
            st.rerun()

# Clear All Tasks
if st.button("🧹 Clear All Tasks"):
    st.session_state.tasks = []
    st.success("🗑️ All tasks deleted successfully!")

# Footer with Icon
st.markdown("---")
st.caption("🚀 Stay organized & productive with this simple TO-DO List App.")
