import json

# Read the notebook
nb_path = r'c:\Users\chait\Projects\chatbot\GPU_Chatbot_Colab (2).ipynb'
with open(nb_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

# Fix the metadata.widgets structure
if 'widgets' in nb['metadata']:
    widgets = nb['metadata']['widgets']
    if 'application/vnd.jupyter.widget-state+json' in widgets:
        widget_state = widgets['application/vnd.jupyter.widget-state+json']
        
        # Ensure all widgets have a 'state' key
        for widget_id, widget in widget_state.items():
            if 'state' not in widget:
                print(f"Adding missing 'state' key to widget: {widget_id}")
                widget['state'] = {}

# Save the notebook
with open(nb_path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)

print("✅ Notebook metadata fixed and saved")
