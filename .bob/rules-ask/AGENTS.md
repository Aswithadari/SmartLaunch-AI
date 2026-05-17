# Ask Mode Rules

## Non-Obvious Documentation Context

### Project Structure
- Despite "SmartLaunch AI" name suggesting a complex system, this is a single-file Streamlit app
- No multi-page structure exists yet - all functionality in app.py
- Backend integration is planned but not implemented (see line 18 comment)

### UI Design Decisions
- Centered layout is intentional UX choice (not wide/full-width)
- File uploader only accepts .zip files - this is a deliberate constraint for future backend
- Spinner message is placeholder text - will be accurate once backend connects

### Development Status
- Currently in prototype/MVP stage with simulated processing (2-second delay)
- watsonx Orchestrate integration is the planned backend (not yet connected)
- Setup guide generation is stubbed out - shows placeholder message only