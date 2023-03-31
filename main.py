import typer
from getinfo import get_user_info, get_time_entries, add_new_entry_time
from rich.console import Console
from rich.table import Table
from rich.progress import track

console = Console()
app = typer.Typer()
    
@app.command()
def list():
    table = Table('#', 'Description', 'Duration')
    user = get_user_info()
    total = 0
    
    for value in track(range(10), description='Loading results...'):
        entry_list = get_time_entries(user.get('activeWorkspace'), user.get('id'))
        total += 1
    
    for index, entry in enumerate(entry_list, start=1):
        description = entry.get('description')
        duration = entry.get('duration')
        table.add_row(str(index), description, duration)
    
    console.print(table)

@app.command()
def create(description: str, date: str):
    table = Table('Description', 'Duration')
    user = get_user_info()
    new_entry = add_new_entry_time(description=description, selected_date=date, current_workspace=user.get('activeWorkspace'), projectId=user.get('project').get('id'))
    
    table.add_row(new_entry.get('description'), new_entry.get('timeInterval').get('duration'))
    console.print(table)

if __name__ == "__main__":
    app()    
