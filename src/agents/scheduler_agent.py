class SchedulerAgent:
    def __init__(self, memory, store):
        self.memory = memory
        self.store = store

    def suggest_schedule(self, meal_plan):
        schedule = []

        # Simple schedule suggestion for demo
        for day in meal_plan.keys():
            schedule.append({
                "time": "18:00",
                "note": f"Cook dinner for {day}"
            })
            schedule.append({
                "time": "08:00",
                "note": f"Prepare breakfast for {day}"
            })

        self.store.save("schedule", schedule)
        return schedule
