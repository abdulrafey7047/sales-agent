from db_utils import execute_insert, execute_select


def register_tools(mcp_app):
    """Registers tools to the FastMCP instance."""

    @mcp_app.tool()
    def add_row(table_name: str, row_data: dict) -> str:
        """
        Inserts a row into a specified table.

        :param table_name (str): Name of the table to insert the row into.
        :param row_data (dict): A dictionary where keys are column names and values are the data.
        """
        try:
            execute_insert(table_name, row_data)
            return f"Successfully added record to {table_name}."
        except Exception as e:
            return f"Insert failed: {str(e)}"

    @mcp_app.tool()
    def get_row(table_name: str, identifier_column: str, identifier_value: str) -> str:
        """
        Finds a record by a specific column value.
        
        Retrieves a row from a table based on a specific column value.
        :param table_name (str): Table to query
        :param identifier_column (str): The column to filter by (e.g., 'user_id' or 'product_name')
        :param identifier_value (str): The value to look for
        """
        try:
            result = execute_select(table_name, identifier_column, identifier_value)
            return str(result) if result else "No record found."
        except Exception as e:
            return f"Query failed: {str(e)}"
