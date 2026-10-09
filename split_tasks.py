import json

with open('missing_images_tasks.json', 'r') as f:
    tasks = json.load(f)

num_agents = 5
chunk_size = (len(tasks) + num_agents - 1) // num_agents

for i in range(num_agents):
    chunk = tasks[i * chunk_size : (i + 1) * chunk_size]
    with open(f'tasks_chunk_{i}.json', 'w') as f:
        json.dump(chunk, f, indent=2)

print(f"Split {len(tasks)} tasks into {num_agents} chunks.")
