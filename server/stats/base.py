from rich.table import Table
from rich.console import Console

class DataObject:
    def __init__(self):
        self._data = {}
        self._console = Console()
        self._stats = {}    
    def __getitem__(self, key):
        return self._data[key]

    def __iter__(self):
        return iter(self._data)
    
    def __len__(self):
        return len(self._data)

    def table_data(self):
        table = Table(show_header=True, header_style="bold magenta")

        for i in self._data:
            table.add_column(i)
    
        l = [[str(s)] for s in self._data.values()]

        for row in zip(*l):
            table.add_row(*row)
        
        self._console.print(table)