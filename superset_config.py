import os

SECRET_KEY = os.getenv("SUPERSET_SECRET_KEY", "fallback_secret_key")
# SQLALCHEMY_ENCRYPTION_KEY = "p9HQk12nIn9A7UFrQ-XYXq9AWFQFTMCmqq1h_zbPbFI="
SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")

FEATURE_FLAGS = {
    "EMBEDDED_SUPERSET": True,
    "ALERT_REPORTS": True,
    "DASHBOARD_NATIVE_FILTERS": True,
    "ENABLE_EXPLORE_DRAG_AND_DROP": True,
    "DASHBOARD_NATIVE_FILTERS_SET": True,
    "DASHBOARD_NATIVE_FILTERS_EDIT": True,
    "DASHBOARD_NATIVE_FILTERS_DEFAULT_FILTER_BOX": True,
    "DASHBOARD_CROSS_FILTERS": True,
    "DASHBOARD_NATIVE_FILTERS_URL_SYNC": True,
    "DASHBOARD_FILTERS_EXPERIMENTAL": True,
    "ENABLE_TEMPLATE_PROCESSING": True
}

HTTP_HEADERS={"X-Frame-Options":"ALLOWALL"}

ENABLE_CORS = True
WTF_CSRF_ENABLED = False

CORS_OPTIONS = {
    "supports_credentials": True,
    "allow_headers": "*",
    "expose_headers": "*",
    "resources": "*",
    "origins": "*"
}


GUEST_TOKEN_JWT_ISSUER = "my-org"
GUEST_TOKEN_JWT_SECRET = "jdUKxfAqehewp4ATSyRF-0QJ2MsXSx0I6dZADj9CkuMBVqdFJIGiy8uX0ppKTMOUYSt-wcF2wOUc1SkpC4tDoA"
GUEST_TOKEN_JWT_ALG = "HS256"

# Dashboard embedding 
GUEST_ROLE_NAME = "Gamma"  
GUEST_TOKEN_HEADER_NAME = "X-GuestToken" 
GUEST_TOKEN_JWT_EXP_SECONDS = 300 # 5 minutes
PUBLIC_ROLE_LIKE = "Gamma"


# In superset_config.py
SESSION_COOKIE_SAMESITE = "Lax"  # Allows cross-site cookie usage
SESSION_COOKIE_HTTPONLY = True    # Good security practice# In superset_config.py
TALISMAN_ENABLED = False
TALISMAN_CONFIG = {
    "content_security_policy": {
        "default-src": ["'self'"],
        "frame-ancestors": ["*"],
        "img-src": ["*", "data:"],
        "worker-src": ["'self'", "blob:"],
        "connect-src": ["*"],
        "script-src": ["'self'", "'unsafe-inline'", "'unsafe-eval'"],
        "style-src": ["'self'", "'unsafe-inline'"],
    },
    "force_https": False,
    "session_cookie_secure": False,
}








