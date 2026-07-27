from pathlib import Path


class EnterpriseDocumentLoader:

    def __init__(self, data_directory="data"):
        self.data_directory = Path(data_directory)

    def load_documents(self):
        documents = []

        for file in self.data_directory.glob("*.txt"):

            with open(file, "r", encoding="utf-8") as f:

                documents.append(
                    {
                        "filename": file.name,
                        "content": f.read()
                    }
                )

        return documents