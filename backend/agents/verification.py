"""
Verification Agent
==================
Mock KYC verification for hackathon demo.
Auto-approves any user response to proceed with the flow.

This is a DEMO implementation - no real KYC validation.
"""

from typing import Dict, Any


def verification_agent_node(state: Dict, user_message: str) -> Dict[str, Any]:
    """
    Verification Agent - Handles KYC and identity verification.
    
    DEMO IMPLEMENTATION:
    Auto-approves verification on ANY user response.
    This allows the flow to proceed to underwriting for demo purposes.
    
    Args:
        state: Current conversation state
        user_message: User's input message
    
    Returns:
        Dict with reply and verification status
    """
    print(f"[VERIFICATION AGENT] Processing: {user_message[:50]}...")
    
    # DEMO: Accept ANY non-empty message as successful verification
    # This ensures the flow always proceeds to underwriting
    if user_message and user_message.strip():
        # Mark verification as complete in STATE
        state["verified"] = True
        state["verification_status"] = "verified"
        
        reply = "Verification completed successfully! Your identity has been verified. Now proceeding to evaluate your loan eligibility..."
        
        print("[VERIFICATION AGENT] VERIFIED - Moving to underwriting")
        
        return {
            "reply": reply,
            "verification_status": "verified",
            "verified": True  # Return this so supervisor can also check
        }
    
    # Fallback - should never happen with valid input
    return {
        "reply": "Please provide your details to proceed with verification.",
        "verification_status": "pending",
        "verified": False
    }
