# Web3.py v6 to v7 Migration Codemod

A production-grade, AST-driven codemod engine designed to safely migrate Python codebases from Web3.py v6 to v7. It combines pure Tree-Sitter AST determinism for standard API changes with a sandboxed Generative AI (NVIDIA NIM Llama-3) fallback to handle complex architectural middleware rewrites.

## Migration Scope

Web3.py v7 introduces massive breaking changes, particularly the complete deprecation of functional middleware in favor of class-based architectures, alongside sweeping renaming of core providers and namespaces.

This codemod automates ~90% of the required changes mathematically:

### Deterministic AST Layer (Zero False Positives)
We use `ast-grep` (Tree-Sitter) to safely target and replace the following patterns without risking substring collisions:
* **Provider Renaming:** `WebsocketProviderV2` -> `WebSocketProvider`
* **Namespace Transposition:** Automatically transposes `.ws` to `.socket` across all instances.
* **Exception Renames:** Safely handles single and tuple-based exception handling (e.g., `ABIEventFunctionNotFound` -> `ABIEventNotFound`).
* **Data Structures:** Safely strips deprecated `AttributeDict` imports and instantiations.
* **Deprecation Flags:** Explicitly flags entirely removed modules (`geth.miner`, `ethpm`) for manual review rather than blindly deleting code and breaking builds.

### Generative AI Sandbox (Middleware Translation)
Translating functional middleware into v7's new `Web3Middleware` classes cannot be predictably transpiled by standard AST tools because the internal business logic varies wildly per project. 

Where AST matching hits its limit, we dynamically extract the exact function body and its base indentation, and sandbox Llama-3-70B strictly to *translating that specific node* into a class structure.

## Usage

You can run this codemod directly via the Codemod CLI.

```bash
# (Optional) Export your NVIDIA NIM key to enable the AI middleware translation
export NVIDIA_NIM_API_KEY="your-api-key"

# Run the codemod
npx codemod web3py-v6-to-v7 ./src
```

### Safety Notes
* **Dry Run:** You can append `--dry-run` to the command to see the proposed AST and AI changes without writing to disk.
* **Idempotency:** Custom middleware blocks converted to classes will not be double-processed on subsequent runs.
* **CI/Offline Mode:** If you do not provide `NVIDIA_NIM_API_KEY`, the codemod gracefully skips the network call, leaving a mock placeholder class to prevent namespace collisions, allowing your test suite to run safely.
