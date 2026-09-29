from fastapi import Depends, Header, HTTPException, status
from fastapi import FastAPI
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import supabase


app = FastAPI()
security = HTTPBearer()

def verify_supabase_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    """
    Dependency that extracts the Bearer token and verifies it with Supabase.
    If invalid, expired, or tampered with, it rejects the request with 401.
    """
    token = credentials.credentials
    try:
        # Ask Supabase if the token is valid
        user_response = supabase.auth.get_user(token)
        if not user_response or not user_response.user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid or expired token"
            )
        return user_response.user
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token"
        )

@app.get("/public/info", status_code=status.HTTP_200_OK)
def public_info():
    """A public lobby endpoint that requires no authentication."""
    return {"message": "Welcome stranger! This info is public."}

@app.get("/protected/profile", status_code=status.HTTP_200_OK)
def protected_profile(current_user = Depends(verify_supabase_token)):
    """
    A protected endpoint. Requires a valid Bearer token.
    FastAPI automatically injects the verified user object here.
    """
    return {
        "message": "Access granted to protected profile!",
        "user_id": current_user.id,
        "email": current_user.email,
        "created_at": current_user.created_at
    }
@app.get("/protected/dashboard", status_code=status.HTTP_200_OK)
def protected_dashboard(current_user = Depends(verify_supabase_token)):
    """
    A second protected route reusing the exact same middleware/dependency guard.
    """
    return {
        "message": "Welcome to your secure dashboard!",
        "email": current_user.email
    }

@app.post("/auth/logout", status_code=status.HTTP_204_NO_CONTENT)
def logout(current_user = Depends(verify_supabase_token)):
    """
    Logs out the user session via Supabase. 
    Protected by the guard so only authenticated users can trigger a logout.
    """
    try:
        # Note: supabase-py sign_out might require passing the token or session depending on the version, 
        # but calling sign_out() terminates the active session context.
        supabase.auth.sign_out()
        return None
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )