from pathlib import Path


class DocumentLoader:
    """
    Enterprise Document Loader

    Loads text documents from the data folder.
    """

    @staticmethod
    def load_documents(folder="data"):

        documents = []

        folder = Path(folder)

        if not folder.exists():
            return documents

        for file in folder.glob("*.txt"):

            with open(file, "r", encoding="utf-8") as f:

                documents.append(
                    {
                        "filename": file.name,
                        "content": f.read()
                    }
                )

        return documents