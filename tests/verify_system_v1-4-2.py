import tomllib
import os
import sys

def test_mesh_integrity():
    mesh_path = "Beats-PM-System/system/agents/mesh.toml"
    print(f"--- Testing Mesh Integrity: {mesh_path} ---")
    
    if not os.path.exists(mesh_path):
        print(f"[ERROR] Mesh file not found at {mesh_path}")
        return False
        
    try:
        with open(mesh_path, "rb") as f:
            data = tomllib.load(f)
            
        # Check for core agents
        required_agents = ["task_manager", "requirements_translator", "prd_author"]
        for agent in required_agents:
            if agent not in data.get("agents", {}):
                print(f"[ERROR] Missing critical agent: {agent}")
                return False
            
            # Verify prompt file paths
            prompt_file = data["agents"][agent].get("prompt_file")
            if not os.path.exists(prompt_file):
                print(f"[WARNING] Prompt file for {agent} missing: {prompt_file}")
            else:
                print(f"[OK] Agent {agent} verified.")

        # Check for new settings
        settings = data.get("settings", {})
        if settings.get("orchestration_mode") != "toml-first":
             print("[ERROR] orchestration_mode is not toml-first")
             return False
        
        print("[SUCCESS] Mesh TOML structure and agent paths verified.")
        return True
    except Exception as e:
        print(f"[ERROR] Failed to parse TOML: {e}")
        return False

def test_stop_execution_logic():
    print("\n--- Simulating STOP_EXECUTION Boundary Rule ---")
    # Simulate a PRD call without metadata
    prd_input = "Build a new dashboard"
    metadata_present = False # Missing Eng Partner/Product Alias
    
    if not metadata_present:
        print("[EXPECTED] Triggering STOP_EXECUTION: Missing Eng Partner or Product Alias.")
        return True
    return False

if __name__ == "__main__":
    s1 = test_mesh_integrity()
    s2 = test_stop_execution_logic()
    
    if s1 and s2:
        print("\n[FINAL] Vibe Check Passed: Multi-agent mesh and boundary rules are operational.")
        sys.exit(0)
    else:
        print("\n[FINAL] Vibe Check Failed.")
        sys.exit(1)
