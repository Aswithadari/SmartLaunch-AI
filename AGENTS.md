# AGENTS.md

This file provides guidance to agents when working with code in this repository.

## Project Overview
SmartLaunch AI - Streamlit-based web app for automated repository analysis and setup guide generation.

## Running the Application
```bash
streamlit run app.py
```

## Non-Obvious Project Details

### Backend Integration Point
- Line 18 in app.py has placeholder comment for watsonx Orchestrate integration
- Backend connection not yet implemented - currently uses simulated 2-second delay
- File upload accepts .zip only, but processing logic is stubbed out

### Application Structure
- Single-file Streamlit app (no multi-page structure despite the name suggesting a larger system)
- Uses centered layout (not wide/full-width) - intentional UX choice
- Spinner message says "Analyzing repository structure..." but no actual analysis occurs yet