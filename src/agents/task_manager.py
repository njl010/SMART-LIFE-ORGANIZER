class TaskManagerAgent:
    def __init__(self, memory, store):
        self.memory = memory
        self.store = store

    def add_tasks_from_plan(self, meal_plan):
        tasks = []
        for day, meals in meal_plan.items():
            dinner = meals.get("dinner")
            tasks.append({
                "day": day,
                "task": f"Prepare {dinner}",
                "priority": "medium"
            })
        self.store.save("tasks", tasks)
        return tasks

    def list_tasks(self):
        return self.store.load("tasks") or []
