import argparse

from close_task import close_task
from delete_task import delete_task
from get_task import get_task

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('id', help='The id of the task to get.')

    group = parser.add_mutually_exclusive_group()
    group.add_argument('--delete', '-d', help='The id of the task to delete.', action='store_true')
    group.add_argument('--close', '-c', help='The id of the task to close.', action='store_true')

    arguments = parser.parse_args()

    try:
        if arguments.delete:
            delete_task(task_id=arguments.id)
        elif arguments.close:
            close_task(task_id=arguments.id)
        else:
            print(get_task(task_id=arguments.id))
    except Exception as e:
        print(e)
