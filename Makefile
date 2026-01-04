# VEX V5 Robot Project Makefile
# ==============================
# Usage: make <target>
# Run 'make help' to see all available commands

.PHONY: help setup install clean lint typecheck format venv activate info test test-cov test-watch docs

# Default Python
PYTHON := python3
VENV := venv
VENV_BIN := $(VENV)/bin
VENV_PYTHON := $(VENV_BIN)/python
VENV_PIP := $(VENV_BIN)/pip

# Colors for output
CYAN := \033[36m
GREEN := \033[32m
YELLOW := \033[33m
RESET := \033[0m

# =============================================================================
# HELP
# =============================================================================

help: ## Show this help message
	@echo "$(CYAN)VEX V5 Robot Project$(RESET)"
	@echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
	@echo ""
	@echo "$(YELLOW)Usage:$(RESET) make <target>"
	@echo ""
	@echo "$(YELLOW)Targets:$(RESET)"
	@awk 'BEGIN {FS = ":.*##"} /^[a-zA-Z_-]+:.*##/ { printf "  $(GREEN)%-15s$(RESET) %s\n", $$1, $$2 }' $(MAKEFILE_LIST)
	@echo ""
	@echo "$(YELLOW)Note:$(RESET) VEX programs run on the V5 Brain, not locally."
	@echo "      Use VS Code + VEX Extension to download to robot."

# =============================================================================
# SETUP & INSTALLATION
# =============================================================================

venv: ## Create Python virtual environment
	@echo "$(CYAN)Creating virtual environment...$(RESET)"
	$(PYTHON) -m venv $(VENV)
	@echo "$(GREEN)✓ Virtual environment created$(RESET)"

install: venv ## Install VEX Python stubs for IntelliSense
	@echo "$(CYAN)Installing VEX Python stubs...$(RESET)"
	$(VENV_PIP) install --upgrade pip
	$(VENV_PIP) install git+https://github.com/GraderThan/vex-v5-python-interface.git
	@echo "$(GREEN)✓ VEX stubs installed$(RESET)"

setup: install ## Full setup: create venv and install all dependencies
	@echo ""
	@echo "$(GREEN)✓ Setup complete!$(RESET)"
	@echo ""
	@echo "$(YELLOW)Next steps:$(RESET)"
	@echo "  1. Open this folder in VS Code"
	@echo "  2. Install VEX Robotics extension"
	@echo "  3. Connect V5 Brain via USB-C"
	@echo "  4. Download src/main.py to robot"

# =============================================================================
# CODE QUALITY
# =============================================================================

lint: ## Run linter (ruff) on source files
	@if [ -f "$(VENV_BIN)/ruff" ]; then \
		echo "$(CYAN)Running ruff linter...$(RESET)"; \
		$(VENV_BIN)/ruff check src/; \
	else \
		echo "$(YELLOW)Installing ruff...$(RESET)"; \
		$(VENV_PIP) install ruff; \
		$(VENV_BIN)/ruff check src/; \
	fi

typecheck: ## Run type checker (pyright) on source files
	@if [ -f "$(VENV_BIN)/pyright" ]; then \
		echo "$(CYAN)Running pyright type checker...$(RESET)"; \
		$(VENV_BIN)/pyright src/; \
	else \
		echo "$(YELLOW)Installing pyright...$(RESET)"; \
		$(VENV_PIP) install pyright; \
		$(VENV_BIN)/pyright src/; \
	fi

format: ## Format code with ruff
	@if [ -f "$(VENV_BIN)/ruff" ]; then \
		echo "$(CYAN)Formatting code...$(RESET)"; \
		$(VENV_BIN)/ruff format src/; \
		echo "$(GREEN)✓ Code formatted$(RESET)"; \
	else \
		echo "$(YELLOW)Installing ruff...$(RESET)"; \
		$(VENV_PIP) install ruff; \
		$(VENV_BIN)/ruff format src/; \
	fi

check: lint typecheck ## Run all code quality checks

# =============================================================================
# TESTING
# =============================================================================

test: ## Run all tests with pytest
	@if [ -f "$(VENV_BIN)/pytest" ]; then \
		echo "$(CYAN)Running tests...$(RESET)"; \
		PYTHONPATH=src $(VENV_BIN)/pytest tests/ -v; \
	else \
		echo "$(YELLOW)Installing pytest...$(RESET)"; \
		$(VENV_PIP) install pytest; \
		PYTHONPATH=src $(VENV_BIN)/pytest tests/ -v; \
	fi

test-cov: ## Run tests with coverage report
	@if [ -f "$(VENV_BIN)/pytest" ] && [ -f "$(VENV_BIN)/coverage" ]; then \
		echo "$(CYAN)Running tests with coverage...$(RESET)"; \
		PYTHONPATH=src $(VENV_BIN)/pytest tests/ -v --cov=src --cov-report=term-missing; \
	else \
		echo "$(YELLOW)Installing pytest and coverage...$(RESET)"; \
		$(VENV_PIP) install pytest pytest-cov; \
		PYTHONPATH=src $(VENV_BIN)/pytest tests/ -v --cov=src --cov-report=term-missing; \
	fi

test-watch: ## Run tests in watch mode (re-run on file changes)
	@if [ -f "$(VENV_BIN)/ptw" ]; then \
		echo "$(CYAN)Running tests in watch mode...$(RESET)"; \
		PYTHONPATH=src $(VENV_BIN)/ptw tests/ -- -v; \
	else \
		echo "$(YELLOW)Installing pytest-watch...$(RESET)"; \
		$(VENV_PIP) install pytest-watch; \
		PYTHONPATH=src $(VENV_BIN)/ptw tests/ -- -v; \
	fi

test-unit: ## Run only unit tests (utils)
	@PYTHONPATH=src $(VENV_BIN)/pytest tests/test_utils.py -v

test-integration: ## Run integration tests (config, driver, autonomous)
	@PYTHONPATH=src $(VENV_BIN)/pytest tests/test_robot_config.py tests/test_driver_control.py tests/test_autonomous.py -v

# =============================================================================
# DEVELOPMENT
# =============================================================================

dev-install: install ## Install development dependencies (linting, formatting, testing)
	@echo "$(CYAN)Installing development tools...$(RESET)"
	$(VENV_PIP) install ruff pyright pytest pytest-cov
	@echo "$(GREEN)✓ Development tools installed$(RESET)"

# =============================================================================
# DOCUMENTATION
# =============================================================================

docs: ## Open tutorials in browser
	@echo "$(CYAN)Opening tutorials...$(RESET)"
	@if [ "$$(uname)" = "Darwin" ]; then \
		open docs/tutorials/README.md; \
	elif [ "$$(uname)" = "Linux" ]; then \
		xdg-open docs/tutorials/README.md 2>/dev/null || echo "Open docs/tutorials/README.md manually"; \
	else \
		echo "Open docs/tutorials/README.md in your browser"; \
	fi

docs-list: ## List all tutorial files
	@echo "$(CYAN)Tutorial Files$(RESET)"
	@echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
	@find docs/tutorials -name "*.md" -type f | sort | while read f; do \
		echo "  $$f"; \
	done
	@echo ""
	@echo "$(YELLOW)Total:$(RESET) $$(find docs/tutorials -name '*.md' -type f | wc -l | tr -d ' ') files"

# =============================================================================
# CLEANUP
# =============================================================================

clean: ## Remove Python cache files
	@echo "$(CYAN)Cleaning cache files...$(RESET)"
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete 2>/dev/null || true
	find . -type f -name "*.pyo" -delete 2>/dev/null || true
	find . -type f -name "*.v5python" -delete 2>/dev/null || true
	@echo "$(GREEN)✓ Cache cleaned$(RESET)"

clean-all: clean ## Remove venv and all generated files
	@echo "$(CYAN)Removing virtual environment...$(RESET)"
	rm -rf $(VENV)
	@echo "$(GREEN)✓ Full cleanup complete$(RESET)"

# =============================================================================
# INFORMATION
# =============================================================================

info: ## Show project information and status
	@echo "$(CYAN)VEX V5 Robot Project Status$(RESET)"
	@echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
	@echo ""
	@echo "$(YELLOW)Python:$(RESET)"
	@$(PYTHON) --version 2>/dev/null || echo "  Not found"
	@echo ""
	@echo "$(YELLOW)Virtual Environment:$(RESET)"
	@if [ -d "$(VENV)" ]; then \
		echo "  $(GREEN)✓ Created$(RESET) ($(VENV)/)"; \
		echo "  Python: $$($(VENV_PYTHON) --version 2>/dev/null)"; \
	else \
		echo "  $(YELLOW)✗ Not created$(RESET) (run 'make setup')"; \
	fi
	@echo ""
	@echo "$(YELLOW)VEX Stubs:$(RESET)"
	@if $(VENV_PIP) show vex >/dev/null 2>&1; then \
		echo "  $(GREEN)✓ Installed$(RESET)"; \
	else \
		echo "  $(YELLOW)✗ Not installed$(RESET) (run 'make install')"; \
	fi
	@echo ""
	@echo "$(YELLOW)Source Files:$(RESET)"
	@ls -1 src/*.py 2>/dev/null | while read f; do echo "  $$f"; done
	@echo ""
	@echo "$(YELLOW)Git:$(RESET)"
	@if [ -d ".git" ]; then \
		echo "  $(GREEN)✓ Initialized$(RESET)"; \
		echo "  Branch: $$(git branch --show-current 2>/dev/null || echo 'unknown')"; \
	else \
		echo "  $(YELLOW)✗ Not initialized$(RESET)"; \
	fi

tree: ## Show project structure
	@if command -v tree >/dev/null 2>&1; then \
		tree -a -I '.git|venv|__pycache__' --dirsfirst; \
	else \
		echo "$(YELLOW)tree command not found, using find:$(RESET)"; \
		find . -not -path './.git/*' -not -path './venv/*' -not -name '__pycache__' | sort; \
	fi
