from pypdf import PdfWriter

def merge_files(input_file_paths, output_file_path):
    writer = PdfWriter()

    try:
        for file_path in input_file_paths:
            writer.append(file_path)

        writer.write(output_file_path)
        writer.close()

        print(f"Output File Path: {output_file_path}")

    except Exception as e:
        print(f"Error: {str(e)}")

    finally:
        pass

if __name__ == "__main__":
    file_paths = [
        "./Signed.pdf",
        "./Signed.pdf"
    ]
    output_file = "./Combined.pdf"

    merge_files(file_paths, output_file)
