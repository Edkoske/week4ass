# file_challenge.py

def read_and_write_file(input_file, output_file):
    try:
        # Read from input file
        with open(input_file, "r") as infile:
            content = infile.read()

        # Modify content (example: convert to uppercase)
        modified_content = content.upper()

        # Write modified content to a new file
        with open(output_file, "w") as outfile:
            outfile.write(modified_content)

        print(f"✅ File '{input_file}' read successfully!")
        print(f"✅ Modified content written to '{output_file}'")

    except FileNotFoundError:
        print(f"⚠️ Error: The file '{input_file}' was not found.")
    except PermissionError:
        print(f"🚫 Error: You don't have permission to read '{input_file}'.")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")


def main():
    # Ask user for input file
    input_file = input("Enter the filename to read: ").strip()
    output_file = "modified_" + input_file

    # Process file
    read_and_write_file(input_file, output_file)


if __name__ == "__main__":
    main()
