# CSVLoader Tool

The **CSVLoader** tool is a Python application built using the Tkinter library that allows users to load and display CSV (Comma-Separated Values) files. It provides a simple graphical user interface for selecting a CSV file, loading its data into a Pandas DataFrame, and displaying the data in a table format using the PandasTable library.

## Prerequisites

- Python 3.x installed on your system.
- Required libraries: tkinter, pandas, pandastable

You can install the required libraries using the following command:

pip install pandas pandastable

## Usage

1. Run the script by executing the following command in your terminal:

**python CSVPANDAS.py**

2. The tool's graphical user interface will open.

3. Click the "Load File" button to open a file dialog.

4. Select a CSV file from your system using the file dialog.

5. The tool will attempt to load the selected CSV file into a Pandas DataFrame.

6. If the file is successfully loaded, the data will be displayed in a table format within the GUI.

## Features

- **Load File Button**: Clicking this button opens a file dialog that allows you to select a CSV file for loading.

- **Data Display**: Once a CSV file is loaded, the tool displays the data from the CSV file in a table format using PandasTable.

- **Error Handling**: The tool provides basic error handling for cases such as an empty CSV file or other exceptions that might occur during file loading.

## Customization

You can further customize this tool by modifying the code to include additional features or improve the user interface. The provided code serves as a starting point for a simple CSV file loader, and you can build upon it to suit your specific needs.

## Note

- The provided code may need adjustments based on your Python environment and requirements.

- This tool is intended for educational and basic data loading purposes. For more complex applications or additional functionalities, you might need to consider more advanced libraries and approaches.

## License

This tool is provided under an open-source license. Please refer to the license terms within the source code for more details.

---

**Disclaimer**: This tool is provided as-is, and the developers and contributors are not responsible for any potential issues or data loss arising from its usage. It's recommended to test the tool thoroughly before using it with important data.
