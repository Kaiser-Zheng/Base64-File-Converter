import argparse
import base64
import os


def encode_file(input_file, output_file):
    with open(input_file, "rb") as file:
        file_content = file.read()
    encoded_content = base64.b64encode(file_content)
    with open(output_file, "wb") as file:
        file.write(encoded_content)


def decode_file(input_file, output_file):
    with open(input_file, "rb") as file:
        encoded_content = file.read()
    decoded_content = base64.b64decode(encoded_content)
    with open(output_file, "wb") as file:
        file.write(decoded_content)


def main():
    parser = argparse.ArgumentParser(description="Encode or decode files using Base64.")
    parser.add_argument("action", choices=["encode", "decode"], help="Action to perform")
    parser.add_argument("input_file", help="Name of the input file")
    parser.add_argument("output_file", help="Name of the output file")

    args = parser.parse_args()

    if not os.path.exists(args.input_file):
        print(f"Input file '{args.input_file}' does not exist in the current directory.")
        return

    try:
        if args.action == "encode":
            encode_file(args.input_file, args.output_file)
            print(f"File encoded successfully. Output saved to {args.output_file}")
        elif args.action == "decode":
            decode_file(args.input_file, args.output_file)
            print(f"File decoded successfully. Output saved to {args.output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
