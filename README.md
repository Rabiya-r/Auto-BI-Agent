┌──────────────────────────────┐
│ User (Microsoft Teams)       │
│ Query: "sales by region"     │
└──────────────┬───────────────┘
               ↓
┌──────────────────────────────┐
│ Copilot / Form               │
│ (Query → JSON Conversion)    │
│ {metric, dimension, time}    │
└──────────────┬───────────────┘
               ↓
┌──────────────────────────────┐
│ Power Automate               │
│ (Trigger + Orchestration)    │
└──────────────┬───────────────┘
               ↓
┌──────────────────────────────────────────────┐
│ Backend API (Python - FastAPI)               │
│----------------------------------------------│
│ 1. Semantic Mapping                          │
│    sales → total_sales                       │
│    region → region_name                      │
│                                              │
│ 2. SQL Generation                            │
│    Dynamic query build                       │
│                                              │
│ 3. DB Execution                              │
│    Azure SQL / MySQL / Excel                │
│                                              │
│ 4. Result JSON                               │
│    [{region, total_sales}]                   │
│                                              │
│ 5. Visualization Agent                       │
│    - Detect data pattern                     │
│    - Choose chart (bar/line/table)           │
│    - Choose axis (x, y)                      │
└──────────────┬───────────────────────────────┘
               ↓
┌──────────────────────────────┐
│ API Response                 │
│ {data, visual, axis info}    │
└──────────────┬───────────────┘
               ↓
┌──────────────────────────────┐
│ Power Automate               │
│ (Condition Logic)            │
│                              │
│ - Set parameter (dimension)  │
│ - Trigger bookmark           │
└──────────────┬───────────────┘
               ↓
┌──────────────────────────────────────────────┐
│ Power BI                                     │
│----------------------------------------------│
│ 1. Dataset (API / DB)                        │
│ 2. DAX Measures (prebuilt)                   │
│    - Total Sales                             │
│    - Profit %                                │
│                                              │
│ 3. Field Parameters                          │
│    - Region / Product switch                 │
│                                              │
│ 4. Visual Layer                              │
│    - Bar chart                               │
│    - Line chart                              │
│    - Table                                   │
│                                              │
│ 5. Bookmarks                                 │
│    - Show/hide visuals                       │
└──────────────┬───────────────────────────────┘
               ↓
┌──────────────────────────────┐
│ Microsoft Teams              │
│ (Embedded Dashboard View)    │
└──────────────────────────────┘
