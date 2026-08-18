class MeansEndAnalysis:
    def __init__(self, operators):
        self.operators = operators

    def solve(self, current, goal):
        print(f"Current State: {current} | Goal State: {goal}")

        # Goal achieved
        if all(current.get(key) == value for key, value in goal.items()):
            return []

        # Find difference
        diff = self.find_difference(current, goal)

        if not diff:
            return []

        # Find operator
        op = self.select_operator(diff)

        if not op:
            print(f"No operator found to resolve difference: {diff}")
            return None

        # Check preconditions
        for key, value in op['precond'].items():
            if current.get(key) != value:
                precondition_op = self.select_operator((key, value))

                if not precondition_op:
                    print(f"Cannot satisfy precondition: {key} = {value}")
                    return None

                result = self.solve(current, op['precond'])

                if result is None:
                    return None

                # Apply precondition operator
                current = current.copy()
                current.update(precondition_op['effect'])

        # Apply selected operator
        new_state = current.copy()
        new_state.update(op['effect'])

        # Solve remaining goal
        remaining_path = self.solve(new_state, goal)

        if remaining_path is None:
            return None

        return [op['name']] + remaining_path

    def find_difference(self, current, goal):
        for key in goal:
            if current.get(key) != goal[key]:
                return (key, goal[key])

        return None

    def select_operator(self, diff):
        key, value = diff

        for op in self.operators:
            if op['effect'].get(key) == value:
                return op

        return None


# Example Usage
if __name__ == "__main__":

    operators = [
        {
            'name': 'Drive_Car',
            'precond': {
                'has_car': True,
                'at_home': True
            },
            'effect': {
                'at_work': True,
                'at_home': False
            }
        },

        {
            'name': 'Buy_Car',
            'precond': {
                'has_money': True,
                'has_car': False
            },
            'effect': {
                'has_car': True
            }
        }
    ]

    current_state = {
        'has_money': True,
        'has_car': False,
        'at_home': True,
        'at_work': False
    }

    goal_state = {
        'at_work': True
    }

    mea = MeansEndAnalysis(operators)

    plan = mea.solve(current_state, goal_state)

    print("\nExecution Plan:", plan)