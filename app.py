import streamlit as st


# Page config and title (Notion-style)
st.set_page_config(page_title="📝 My Daily Todo Tasker", layout="wide")
st.markdown("<h1 style='text-align:center;margin-bottom:0.2rem'>📝 My Daily Todo Tasker</h1>", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align:center;color:#6b6b6b;margin-top:0.1rem;font-size:14px'>Track your daily routines, master your studies, and design your perfect day. ☀️</p>",
    unsafe_allow_html=True,
)

# Scoped CSS to remove white gap on buttons inside todo cards
st.markdown(
    """
    <style>
    /* Target only buttons inside the todo list wrapper to blend with card background */
    #todo-list-root .stButton>button {
        background: transparent !important;
        border: none !important;
        box-shadow: none !important;
        padding: 6px 12px !important;
        color: inherit !important;
    }
    #todo-list-root .stButton {
        background: transparent !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# Initialize session state
if "todo_list" not in st.session_state:
    st.session_state["todo_list"] = []


# Sidebar: inputs
st.sidebar.header("My Daily Plan")
content = st.sidebar.text_input(
    "What is on your todo list today?",
    key="new_content",
    placeholder="e.g., Buy groceries, Read a book",
)
category = st.sidebar.selectbox(
    "Category",
    ["Study", "Daily", "Workout"],
    key="new_category",
)
priority = st.sidebar.selectbox(
    "Priority",
    ["High", "Medium", "Low"],
    key="new_priority",
)


# Safe callback for adding todos
def add_todo_callback():
    content_val = st.session_state.get("new_content", "")
    if not content_val or not content_val.strip():
        st.sidebar.warning("Please enter a todo item.")
        return

    if "todo_list" not in st.session_state:
        st.session_state["todo_list"] = []

    st.session_state["todo_list"].append(
        {
            "content": content_val.strip(),
            "category": st.session_state.get("new_category", "Daily"),
            "priority": st.session_state.get("new_priority", "Medium"),
        }
    )

    # Clear the input safely inside the callback
    st.session_state["new_content"] = ""
    st.sidebar.success("Task added to your list!")


# Add button with on_click callback
st.sidebar.button("Add to List", on_click=add_todo_callback, key="add_to_list")


# Mappings for UI
CATEGORY_EMOJI = {"Study": "📚", "Daily": "☕", "Workout": "🏋️‍♀️"}
PRIORITY_LABEL = {"High": "🔴 High", "Medium": "🟡 Medium", "Low": "🟢 Low"}

# Sidebar / card background color (unified)
SIDEBAR_BG = "#ffffff"


# Main area: Today's Todo List (Notion-like layout)
st.subheader("Today's Todo List")

todos = st.session_state.get("todo_list", [])
if not todos:
    st.info("Your daily todo list is clear! Add some tasks in the sidebar to get started. ☕")
else:
    # Open wrapper div to scope CSS so buttons inside will blend with card background
    st.markdown("<div id='todo-list-root' style='width:100%'>", unsafe_allow_html=True)
    for idx, item in enumerate(todos):
        emoji = CATEGORY_EMOJI.get(item.get("category", ""), "")
        pr_label = PRIORITY_LABEL.get(item.get("priority", ""), item.get("priority", ""))

        # Use per-column divs and nest the button inside a right-side div so the background spans fully
        with st.container():
            left_col, right_col = st.columns([4, 1], gap="small")

            # Left column: background div containing the text; extend margin-right to cover gutter
            with left_col:
                st.markdown(
                    f"<div style='background-color:{SIDEBAR_BG};border-top-left-radius:10px;border-bottom-left-radius:10px;padding:12px;margin:0;margin-right:-6px;box-sizing:border-box;'>"
                    f"<div style='font-size:15px;margin-bottom:6px'>{emoji} <strong>[{item.get('category','')}]</strong> {item.get('content','')}</div>"
                    f"<div style='color:#6b6b6b;font-size:13px'>{pr_label}</div>"
                    f"</div>",
                    unsafe_allow_html=True,
                )

            # Right column: open a div, render the Streamlit button (so it's nested), then close div
            with right_col:
                st.markdown(
                    f"<div style='background-color:{SIDEBAR_BG};border-top-right-radius:10px;border-bottom-right-radius:10px;padding:8px;margin:0;margin-left:-6px;display:flex;align-items:center;justify-content:center;box-sizing:border-box;'>",
                    unsafe_allow_html=True,
                )

                if st.button("✔ Complete", key=f"complete_{idx}"):
                    st.session_state["todo_list"].pop(idx)
                    st.rerun()

                st.markdown("</div>", unsafe_allow_html=True)
    # Close wrapper
    st.markdown("</div>", unsafe_allow_html=True)


# Behind the scenes: data structure (JSON)
st.divider()
st.subheader("Behind the Scenes: Data Structure (JSON)")
st.json(st.session_state.get("todo_list", []))

st.markdown("---")
st.caption("Tasks persist in `st.session_state` so they survive reruns while the session is active.")
