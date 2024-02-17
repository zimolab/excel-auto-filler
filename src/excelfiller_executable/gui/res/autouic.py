import os
import sys

OUTPUT_DIR = "../generated_code"

OUTPUT_FILE_PREFIX = ""

CMD = "pyside2-uic"


def make_output_filename(path: str, prefix: str = OUTPUT_FILE_PREFIX, suffix: str = ".py") -> str:
    basename = os.path.basename(path)
    filename, _ = os.path.splitext(basename)
    return f"{prefix}{filename}{suffix}"


def main():
    args = sys.argv[1:]
    if len(args) > 0:
        output_dir = args[0]
    else:
        output_dir = OUTPUT_DIR

    for filename in os.listdir("./"):
        if not filename.endswith(".ui"):
            continue
        try:
            output_filename = make_output_filename(filename, prefix=OUTPUT_FILE_PREFIX, suffix=".py")
            output_path = os.path.join(output_dir, output_filename)
            os.system(f"{CMD} {filename} -o {output_path} ")
        except BaseException as e:
            print(e)


if __name__ == '__main__':
    main()
