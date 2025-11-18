class ReminderAgent:
    def __init__(self, memory, store):
        self.memory = memory
        self.store = store

    def create_reminders_from_schedule(self, schedule):
        reminders = []
        for item in schedule:
            reminders.append({
                "time": item.get("time"),
                "message": item.get("note")
            })
        self.store.save("reminders", reminders)
        return reminders

    def pause_reminder(self, reminder_id):
        data = self.store.load("reminders") or []
        for r in data:
            if r.get("id") == reminder_id:
                r["paused"] = True
        self.store.save("reminders", data)
        return True

    def resume_reminder(self, reminder_id):
        data = self.store.load("reminders") or []
        for r in data:
            if r.get("id") == reminder_id:
                r["paused"] = False
        self.store.save("reminders", data)
        return True
