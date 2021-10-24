import csv
import json
import requests

URL_STRING = "https://a.4cdn.org/"

def save_boards():
    print('Saving boards...')
    boards = get_boards()

    file = open('boards.csv', 'w', newline='')

    csv_writer = csv.writer(file)

    for board in boards['boards']:
        print('Working on ' + board.get('board') + ' currently.')
        csv_writer.writerow(board.values())

    file.close()

def save_threads():
    print('Saving threads...')
    with open('boards.csv', 'r') as boards_file:
        csv_reader = csv.reader(boards_file)

        for row in csv_reader:
            boards = get_threads(row[0])

            file = open('threads.csv', 'w', newline='')
            csv_writer = csv.writer(file)

            for board in boards:
                for thread in board.get('threads'):
                    print('Working on thread ' + str(thread.get('no')) + ' currently.')
                    csv_writer.writerow(thread.values())

        file.close()

    boards_file.close()

def get_boards() -> dict:
    url = URL_STRING + 'boards.json'
    response = requests.get(url)
    response = response.json()
    return response

def get_threads(board: str):
    url = URL_STRING + board + '/' + 'threads.json'
    response = requests.get(url)
    response = response.json()
    return response

def handler():
    save_boards()
    save_threads()

    # for board_info in boards.get('boards'):
    #     board = get_board(board_info.get('board'))
    #     for thread_info in board:
    #         for thread in thread_info.get('threads'):
    #             if thread.get('replies') == 300:
    #                 print(thread)

if __name__ == '__main__':
    handler()