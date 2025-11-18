class MealPlannerAgent:
    def __init__(self, memory, store):
        self.memory = memory
        self.store = store

    def create_meal_plan(self, text):
        # Simple 7-day rotating meal plan
        base_meals = [
            {"breakfast": "oatmeal", "lunch": "salad", "dinner": "veg curry"},
            {"breakfast": "eggs", "lunch": "rice bowl", "dinner": "pasta"},
            {"breakfast": "smoothie", "lunch": "wrap", "dinner": "stir fry"}
        ]

        plan = {}
        for i in range(1, 8):
            plan[f"day{i}"] = base_meals[(i - 1) % len(base_meals)]

        self.store.save("meal_plan", plan)
        return plan
