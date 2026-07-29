from pathlib import Path


class DocumentLoader:

    def __init__(self, data_directory):

        self.data_directory = Path(data_directory)

    def load(self):

        documents = []

        for file in self.data_directory.glob("*.txt"):

            with open(file, "r", encoding="utf-8") as f:

                documents.append(
                    {
                        "source": file.name,
                        "text": f.read()
                    }
                )

        return documents