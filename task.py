import argparse

from get_task import get_task

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('id', help='The id of the task to get.')

    arguments = parser.parse_args()

    try:
        task = get_task(task_id=arguments.id)
        print(task)
    except Exception as e:
        print(e)
