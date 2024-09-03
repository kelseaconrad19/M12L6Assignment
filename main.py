def schedule_tasks(task_hierarchy):
    def traverse(task):

        scheduled_tasks = [task]

        for subtask in task.get('subtasks', []):
            scheduled_tasks.extend(traverse(subtask))

        return scheduled_tasks

    all_tasks = traverse(task_hierarchy)

    sorted_tasks = sorted(all_tasks, key=lambda x: x.get('priority', 0), reverse=True)

    return sorted_tasks

task_hierarchy_1 = {
    'id': 1,
    'name': 'Main Task',
    'priority': 2,
    'subtasks': [
        {
            'id': 2,
            'name': 'Subtask 1',
            'priority': 3,
            'subtasks': []
        },
        {
            'id': 3,
            'name': 'Subtask 2',
            'priority': 1,
            'subtasks': []
        }
    ]
}

task_hierarchy_2 = {
    'id': 1,
    'name': 'Project',
    'priority': 1,
    'subtasks': [
        {
            'id': 2,
            'name': 'Phase 1',
            'priority': 2,
            'subtasks': [
                {
                    'id': 3,
                    'name': 'Task 1',
                    'priority': 4,
                    'subtasks': []
                },
                {
                    'id': 4,
                    'name': 'Task 2',
                    'priority': 3,
                    'subtasks': []
                }
            ]
        },
        {
            'id': 5,
            'name': 'Phase 2',
            'priority': 1,
            'subtasks': []
        }
    ]
}

# Running the tests
print(schedule_tasks(task_hierarchy_1))
print(schedule_tasks(task_hierarchy_2))

# Time Complexity: O(n log n)
# Space Complexity: O(n)