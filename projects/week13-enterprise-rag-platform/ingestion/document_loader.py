from pathlib import Path


class EnterpriseDocumentLoader:
    def __init__(self, data_directory=None):
        project_root = Path(__file__).resolve().parents[1]

        if data_directory is None:
            self.data_directory = project_root / "data"
        else:
            self.data_directory = Path(data_directory)

    def load_documents(self):
        documents = []

        for file in self.data_directory.glob("*.txt"):
            with open(file, "r", encoding="utf-8") as f:
                documents.append(
                    {
                        "filename": file.name,
                        "content": f.read(),
                    }
                )

        return documents