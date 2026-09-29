# Draw.io Diagram Design Rules (`diagram_rules_drawio`)

This file contains the mandatory, explicit preferences for designing draw.io and architecture diagrams in this project. When generating or editing diagrams, you MUST follow these guidelines to ensure they meet the aesthetic and structural standards of the Vibe Coding ecosystem.

## 🟢 What I Want (DOs)

1. **Semantic Shapes**: 
   - Always choose the shape that matches the node's purpose.
   - `shape=actor` for users, clients, or people.
   - `ellipse;shape=cloud` for LLMs, OpenAI, AWS, or external 3rd-party services.
   - `shape=cylinder` for databases, storage, and heavy data processing.
   - `shape=document` or `shape=note` for files (PDFs, CSVs, scripts).
   - `shape=hexagon` or `shape=step` for microservices or discrete processing steps.

2. **Perfect Alignment & Spacing**:
   - Use clean, structured layouts.
   - If a node has many outgoing edges, fan them out (radially or in a staggered cascade) so they do not stack on top of each other.
   - Provide ample horizontal and vertical padding between nodes (e.g., minimum 100px spacing).

3. **No Edge Label Overlaps**:
   - Edge text MUST be perfectly readable. 
   - If multiple arrows point in the same general direction, offset their target nodes so the connection lines separate early, giving each label its own clear space.

4. **Pleasing, Professional Colors & Contrast**:
   - Use soft, modern pastel fills with distinct border strokes.
   - Example Base: `fillColor=#dae8fc;strokeColor=#6c8ebf` (Blue/Tech)
   - Example Data: `fillColor=#d5e8d4;strokeColor=#82b366` (Green/Database)
   - Example External: `fillColor=#ffe6cc;strokeColor=#d79b00` (Orange/API)
   - Example Error/Warning: `fillColor=#f8cecc;strokeColor=#b85450` (Red)
   - **CRITICAL CONTRAST RULE:** You must ALWAYS explicitly set the `fontColor` to ensure readability. If you are using light pastel fill colors, you MUST set `fontColor=#000000` (or another dark contrast color like `#333333`). Never assume the default font color will contrast well, especially in dark mode viewers.

5. **Logical Grouping & Multi-Page Rule (CRITICAL)**:
   - When appropriate, wrap related nodes in a container or boundary box (e.g., a dashed rectangle representing a "Serverless Backend" or "VPC") with a subtle background color.
   - **Multi-Page Rule:** DO NOT cluster or overload Page 1 with too many nodes or complex workflows. If a process requires multiple steps, alternative paths (like error handling or amendments), or deep security gates, you MUST abstract them into separate pages/tabs within the same `.drawio` file. Use Off-Page Connectors (`shape=offPageConnector`) to link between pages. Keep Page 1 as the high-level, clean main flow.

6. **Preserve Manual Styling & Geometry (CRITICAL)**:
   - Before updating an existing `.drawio` file, you MUST read the current XML and extract the style string AND geometry for all existing nodes and edges.
   - **Colors/Fonts**: You must preserve manual color overrides (`fillColor`, `strokeColor`, `fontColor`). 
   - **Layout/Routing**: You must preserve the `<mxGeometry>` exact coordinates (`x`, `y`, `width`, `height`) for existing nodes. For edges, you MUST preserve the manual routing paths (the `<Array as="points">` block with `mxPoint` tags).
   - When adding new nodes or edges, do not regenerate the entire graph layout. Only place the new elements in available whitespace and leave the user's manual aesthetic positioning completely untouched.

---

## 🔴 What I DON'T Want (DON'Ts)

1. **NO Boring Rectangles**:
   - Do not generate entire diagrams using nothing but basic rectangles. A diagram where every node is identical is a failure.

2. **NO Spaghetti Routing or Overlaps**:
   - Do not allow connection lines to pass *through* other nodes.
   - Do not allow connection lines to sit perfectly on top of one another, masking their paths.
   - Do not allow text labels on edges to collide or overlap.

3. **NO Garish or Default Colors**:
   - Avoid plain white nodes with harsh black borders unless specifically doing a wireframe.
   - Never use neon, highly saturated, or conflicting colors that hurt the eyes.

4. **NO Unreadable Text**:
   - Do not let node text overflow outside of the shape boundaries. Use word wrapping (`whiteSpace=wrap`) and ensure the shape is large enough to contain its label.

---

---

## 📘 Documentation Synchronization (Mandatory)

1. **Synchronous Updates**: Whenever you modify, add to, or restructure a `.drawio` file, you MUST synchronously edit the accompanying `.md` file with the **same name** (e.g., `architecture.md` for `architecture.drawio`) located in the same directory. **Never name it `README.md`.**
2. **Textual Source of Truth**: The matching `.md` must explain the "why" and "how" of the architecture. Document all pages under explicit `## Page X` headers within that single file.
3. **Never Drift**: The diagram and its `.md` must never fall out of sync. A change to one requires a change to the other.

---

## 🌑 Dark Mode Color Rules (CRITICAL — User Always Uses Dark Mode)

The user **always views diagrams in dark mode**. Every `.drawio` file MUST be legible in dark mode. Apply these rules to **every mxCell** without exception:

### Vertex boxes (shapes with fills)
- Always set `fontColor=#000000` — black text on light pastel fills is readable in dark mode
- Never omit `fontColor` — draw.io dark mode defaults to white fill-on-white text (invisible)

### Edges (connectors / arrows)
- `fontColor=#ffffff` — edge labels float on the dark canvas, must be white
- `strokeColor=#aaaaaa` — light grey stroke is visible against dark background
- `strokeWidth=2` — thicker lines are visible in dark mode

### Floating text / title labels (`text;` style with `strokeColor=none`)
- `fontColor=#ffffff` — these float on the dark canvas, must be white

### Required style templates
```
Vertex:  rounded=1;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;fontColor=#000000;
Edge:    edgeStyle=orthogonalEdgeStyle;fontColor=#ffffff;strokeColor=#aaaaaa;strokeWidth=2;
Title:   text;html=1;strokeColor=none;fillColor=none;fontColor=#ffffff;fontSize=16;fontStyle=1;
Swimlane: swimlane;startSize=30;fillColor=#fff2cc;strokeColor=#d6b656;fontColor=#000000;
```

**Never leave `fontColor` unset. Never use default edge colors.**

