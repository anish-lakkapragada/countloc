import sys
import os

numLines = 0


def loc(file_path):
    # print(file_path)

    try:
        return len(open(file_path).readlines())
    except UnicodeDecodeError as e:
        try:
            return len(open(file_path, errors='ignore').readlines())
        except Exception as e:
            print(f"cannot read {file_path}")
            return 0


def countLines(cur_dir, AVOID):
    global numLines
    for file in os.listdir(cur_dir):
        if (file.upper() in AVOID):
            continue

        screwed = False
        for avoid in AVOID:
            if len(avoid) > 1 and avoid[:1] == ".": 
                print(file , avoid[1:])
                if file.upper().endswith(avoid[1:]): 
                    screwed = True 
                    break 
            if file.upper().endswith(avoid): 
                screwed = True 
                break 

        if screwed:
            continue

        # if it's a file
        if os.path.isfile(cur_dir + "/" + file):
            numLines += loc(cur_dir + "/" + file)

        # if it's a directory
        else:
            countLines(cur_dir + "/" + file, AVOID)  # recurse even further


def main():
    print([avoid for avoid in sys.argv[1:]])
    countLines(os.getcwd(), [avoid.upper() for avoid in sys.argv[1:]])
    print(f"Counted {numLines} lines")


if __name__ == '__main__':
    main()
