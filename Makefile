.PHONY: install build package-install clean

install:
	uv sync

VD-games:
	uv run VD-games

build:
	uv build

package-install:
	uv tool install dist/*.whl

clean:
	rm -rf dist/
	rm -rf build/
	rm -rf *.egg-info

help:
	@echo "Доступные команды:"
	@echo "  make install       - Установить зависимости"
	@echo "  make VD-games      - Запустить игру"
	@echo "  make build         - Собрать пакет"
	@echo "  make package-install - Установить пакет в систему"
	@echo "  make clean         - Очистить временные файлы"
lint:
	uv run ruff check games_project_loginova/

lint-fix:
	uv run ruff check --fix games_project_loginova/
