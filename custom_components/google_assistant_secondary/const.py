"""Constants for Google Assistant Secondary."""

DOMAIN = "google_assistant_secondary"

GOOGLE_ASSISTANT_API_ENDPOINT = "/api/google_assistant_secondary"

CONF_ALIASES = "aliases"
CONF_CLIENT_EMAIL = "client_email"
CONF_ENTITY_CONFIG = "entity_config"
CONF_EXPOSE = "expose"
CONF_EXPOSE_BY_DEFAULT = "expose_by_default"
CONF_EXPOSED_DOMAINS = "exposed_domains"
CONF_PRIVATE_KEY = "private_key"
CONF_PROJECT_ID = "project_id"
CONF_REPORT_STATE = "report_state"
CONF_ROOM_HINT = "room"
CONF_SECURE_DEVICES_PIN = "secure_devices_pin"
CONF_SERVICE_ACCOUNT = "service_account"

DATA_CONFIG = "config"

DEFAULT_EXPOSE_BY_DEFAULT = True
DEFAULT_EXPOSED_DOMAINS = [
    "alarm_control_panel",
    "binary_sensor",
    "climate",
    "cover",
    "event",
    "fan",
    "group",
    "humidifier",
    "input_boolean",
    "input_select",
    "lawn_mower",
    "light",
    "lock",
    "media_player",
    "scene",
    "script",
    "select",
    "sensor",
    "switch",
    "vacuum",
    "valve",
    "water_heater",
]

SERVICE_REQUEST_SYNC = "request_sync"

# Reuse Google API URLs from the built-in integration
HOMEGRAPH_URL = "https://homegraph.googleapis.com/"
HOMEGRAPH_SCOPE = "https://www.googleapis.com/auth/homegraph"
HOMEGRAPH_TOKEN_URL = "https://accounts.google.com/o/oauth2/token"
REQUEST_SYNC_BASE_URL = f"{HOMEGRAPH_URL}v1/devices:requestSync"
REPORT_STATE_BASE_URL = f"{HOMEGRAPH_URL}v1/devices:reportStateAndNotification"

STORE_AGENT_USER_IDS = "agent_user_ids"
STORE_GOOGLE_LOCAL_WEBHOOK_ID = "local_webhook_id"

SOURCE_CLOUD = "cloud"
