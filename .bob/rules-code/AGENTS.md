# Code Mode Rules

## Non-Obvious Coding Patterns

### Backend Integration
- Line 18 in app.py is the designated integration point for watsonx Orchestrate
- Do not implement actual file processing yet - maintain the 2-second delay simulation
- Keep the placeholder structure intact for future backend connection

### UI Constraints
- Must use `layout="centered"` in st.set_page_config (not "wide") - intentional UX decision
- File uploader restricted to .zip only - do not add other formats without backend support
- Spinner message is intentionally misleading ("Analyzing...") - will be accurate once backend connects

### Code Organization
- Single-file architecture is intentional - do not split into multiple files/pages
- All Streamlit logic stays in app.py root level (no subdirectories)