import logging
import json
from agents.task_manager import TaskManagerAgent
from agents.reminder_agent import ReminderAgent
from agents.meal_planner import MealPlannerAgent
from agents.shopping_agent import ShoppingAgent
from agents.scheduler_agent import SchedulerAgent
from tools.json_store_tool import JSONStoreTool
from memory.memory_bank import MemoryBank
from observability.logging import init_logging


class SupervisorAgent:
    def __init__(self, config=None):
        init_logging()
        self.memory = MemoryBank()
        self.store = JSONStoreTool()

        self.task_agent = TaskManagerAgent(self.memory, self.store)
        self.reminder_agent = ReminderAgent(self.memory, self.store)
        self.meal_agent = MealPlannerAgent(self.memory, self.store)
        self.shopping_agent = ShoppingAgent(self.memory, self.store)
        self.scheduler_agent = SchedulerAgent(self.memory, self.store)

    def handle_user_request(self, text):
        meal_plan = self.meal_agent.create_meal_plan(text)
        shopping = self.shopping_agent.generate_shopping_list(meal_plan)
        schedule = self.scheduler_agent.suggest_schedule(meal_plan)
        tasks = self.task_agent.add_tasks_from_plan(meal_plan)
        reminders = self.reminder_agent.create_reminders_from_schedule(schedule)

        summary = {
            "meal_plan": meal_plan,
            "shopping_list": shopping,
            "schedule": schedule,
            "tasks": tasks,
            "reminders": reminders
        }

        self.memory.save_user_summary(summary)
        return summary


if __name__ == "__main__":
    sup = SupervisorAgent()
    out = sup.handle_user_request("Plan my meals for 7 days")
    print(json.dumps(out, indent=2))
