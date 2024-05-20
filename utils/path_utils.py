import os

def get_first_pdf_file_paths(directory_path):

    # List to store the folder names and first PDF file paths as tuples
    folder_pdf_tuples = []
    if not os.path.isdir(directory_path):
        return folder_pdf_tuples

    # Iterate through the items in the directory
    for item in os.listdir(directory_path):
        item_path = os.path.join(directory_path, item)

        # Check if the item is a folder
        if os.path.isdir(item_path):
            first_pdf_path = None

            # Iterate through the items in the folder
            for sub_item in os.listdir(item_path):
                sub_item_path = os.path.join(item_path, sub_item)

                # Check if the sub-item is a PDF file
                if os.path.isfile(sub_item_path) and sub_item.lower().endswith('.pdf'):
                    first_pdf_path = sub_item_path
                    break  # Exit loop after finding the first PDF

            folder_pdf_tuples.append((item, first_pdf_path))

    # Return the list of tuples
    return folder_pdf_tuples

