from services.memory_service import MemoryService


def test_memory_save_and_load():
    MemoryService.save("user", "Mike")
    assert MemoryService.load("user") == "Mike"


def test_memory_show():
    MemoryService.save("city", "Johannesburg")
    memory = MemoryService.show()

    assert "city" in memory