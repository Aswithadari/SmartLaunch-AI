# Plan Mode Rules

## Non-Obvious Architecture Constraints

### Current Architecture
- Single-file Streamlit application (app.py) - intentionally simple for MVP stage
- No database, no state management, no multi-page structure
- Backend integration point exists (line 18) but not yet implemented

### Planned Architecture
- watsonx Orchestrate will handle repository analysis backend
- File processing pipeline not yet designed - currently simulated with 2-second delay
- Setup guide generation logic is placeholder only

### Design Constraints
- Must maintain centered layout (not wide) - UX requirement
- File upload restricted to .zip format only - backend dependency
- Single-file structure must be preserved until backend integration complete

### Future Considerations
- Backend connection will replace time.sleep(2) simulation
- Actual file processing logic needs to be designed for .zip extraction
- Output formatting for setup guides not yet specified