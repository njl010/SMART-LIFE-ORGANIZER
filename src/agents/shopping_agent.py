class ShoppingAgent:
    def __init__(self, memory, store):
        self.memory = memory
        self.store = store

    def generate_shopping_list(self, meal_plan):
        items = set(["oil", "spices", "vegetables"])

        for meals in meal_plan.values():
            dinner = meals.get("dinner", "")
            if "pasta" in dinner:
                items.add("pasta")
            if "rice" in dinner:
                items.add("rice")

        items = sorted(list(items))
        self.store.save("shopping_list", items)
        return items
