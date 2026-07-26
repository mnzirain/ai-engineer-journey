from services.memory_service import MemoryService


def test_memory_save_and_load():

    MemoryService.clear()

    MemoryService.remember("user_name", "Mike")

    assert MemoryService.recall("user_name") == "Mike"