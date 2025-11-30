# Using These Packages as Dependencies

This repository contains two packages that can be used as dependencies in other projects:

- `leapc_cffi` - Low-level CFFI bindings for LeapC
- `leap` - High-level Python API wrapper (depends on `leapc_cffi`)

## Installation from Git

### Option 1: Install the main package (recommended)

The `leap` package depends on `leapc_cffi`. Since both are in the same repository, you need to tell the package manager where to find `leapc_cffi`. Add this to your `pyproject.toml`:

```toml
[project]
dependencies = [
    "leap @ git+https://github.com/alexeden/leapc-python-bindings.git#subdirectory=leapc-python-api",
]

[tool.uv.sources]
leapc_cffi = { git = "https://github.com/alexeden/leapc-python-bindings.git", subdirectory = "leapc-cffi" }
```

Or using `uv pip` directly (you'll need to install both):

```bash
uv pip install "leapc_cffi @ git+https://github.com/alexeden/leapc-python-bindings.git#subdirectory=leapc-cffi"
uv pip install "leap @ git+https://github.com/alexeden/leapc-python-bindings.git#subdirectory=leapc-python-api"
```

### Option 2: Install both packages explicitly

If you need both packages separately:

```toml
[project]
dependencies = [
    "leapc_cffi @ git+https://github.com/alexeden/leapc-python-bindings.git#subdirectory=leapc-cffi",
    "leap @ git+https://github.com/alexeden/leapc-python-bindings.git#subdirectory=leapc-python-api",
]
```

### Option 3: Using a specific branch or tag

```toml
[project]
dependencies = [
    "leap @ git+https://github.com/alexeden/leapc-python-bindings.git@main#subdirectory=leapc-python-api",
]

[tool.uv.sources]
leapc_cffi = { git = "https://github.com/alexeden/leapc-python-bindings.git", rev = "main", subdirectory = "leapc-cffi" }
```

Or with a tag:

```toml
[project]
dependencies = [
    "leap @ git+https://github.com/alexeden/leapc-python-bindings.git@v1.0.0#subdirectory=leapc-python-api",
]
```

## Using with uv

If you're using `uv` for dependency management:

```bash
# Add to your pyproject.toml dependencies, then:
uv sync
```

Or install directly:

```bash
uv pip install "leap @ git+https://github.com/alexeden/leapc-python-bindings.git#subdirectory=leapc-python-api"
```

## Important Notes

1. **Leap SDK Required**: Both packages require the Ultraleap Hand Tracking SDK to be installed on your system. See the main README for installation instructions.

2. **Build Requirements**: The `leapc_cffi` package requires a C compiler and the Leap SDK headers/libraries to build. Make sure these are available when installing.

3. **Subdirectory Syntax**: The `#subdirectory=` syntax tells the package manager which subdirectory contains the package's `pyproject.toml`.

4. **Workspace Development**: If you're developing within this repository, the workspace configuration will automatically handle dependencies. The `[tool.uv.sources]` section in `leapc-python-api/pyproject.toml` is only used when working in the workspace.
