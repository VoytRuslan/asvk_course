import argparse
import cowsay


def main():
    parser = argparse.ArgumentParser(description='Two cows say something')
    parser.add_argument('-f', '--first', default='default', help='Specify the first cow')
    parser.add_argument('-E', '--eyes', default='oo', help='Specify the eyes')
    parser.add_argument('-F', '--second', default='  ', help='Specify the second cow')
    parser.add_argument('message1', help='The first message')
    parser.add_argument('message2', help='The second message')
    args = parser.parse_args()

    first_cow = cowsay.cowsay(args.message1, cow=args.first)
    second_cow = cowsay.cowsay(args.message2, cow=args.second, eyes=args.eyes)

    # print the cows on the same lines

    # split the cows into lines
    first_cow_lines = first_cow.split('\n')
    second_cow_lines = second_cow.split('\n')

    # find the maximum number of lines
    max_lines = max(len(first_cow_lines), len(second_cow_lines))
    max_first_length = len(max(first_cow_lines, key=len))
    max_second_length = len(max(second_cow_lines, key=len))

    if len(first_cow_lines) < len(second_cow_lines):
        for i in range(len(second_cow_lines) - len(first_cow_lines)):
            print(' ' * max_first_length + second_cow_lines[i])

        second_cow_lines = second_cow_lines[len(second_cow_lines) - len(first_cow_lines):]
    else:
        for i in range(len(first_cow_lines) - len(second_cow_lines)):
            print(first_cow_lines[i])

        first_cow_lines = first_cow_lines[len(first_cow_lines) - len(second_cow_lines):]

    # print the cows line by line
    for i in range(max_lines):
        line = ''
        if i < len(first_cow_lines):
            line += first_cow_lines[i]
        else:
            line += ' ' * max_first_length
        line += (max_first_length - len(line)) * ' '
        if i < len(second_cow_lines):
            line += second_cow_lines[i]
        print(line)


if __name__ == '__main__':
    main()
