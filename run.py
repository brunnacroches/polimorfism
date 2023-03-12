from models.inserter import Inserter
from models.repository import Repository

class RepositoryFaker(Repository):
    def __init__(self):
        super().__init__()
    
    def select(self, name: int) -> None:
        return None

repo = RepositoryFaker()
inserter = Inserter(repo)

data = inserter.insert_data('brunna', 28)
print(data)